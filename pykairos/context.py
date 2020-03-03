#    This file is part of Kairos.
#
#    Kairos is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Kairos is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Kairos.  If not, see <http://www.gnu.org/licenses/>.

import logging, shutil, os, binascii, urllib, json, multiprocessing, zipfile, io, sys, re, pandas, plotly, hashlib, subprocess
from collections import *
from datetime import datetime
from pykairos.repository import Repository
from pykairos.arcfile import Arcfile
from pykairos.analyzer import Analyzer
from pykairos.parallel import Parallel
from contextlib import suppress

#  Lambdas

getdatabases = lambda repository: [row['datname'] for row in repository.execute("select datname from pg_database")]
getnextid = lambda repository: [row['objid'] for row in repository.execute("select nextval('objid') as objid")][0]
getdbsizes = lambda repository: {row['datname']:row['size'] for row in repository.execute("select datname, pg_database_size(datname) as size from pg_database where datname like 'kairos_%'")}
getgroupdatabases = lambda repository, user: ['kairos_group_' + row['groname'] for row in repository.execute("select groname from pg_group,pg_user where usesysid = any(grolist) and usename='" + user + "'")]
getdefaultnodename = lambda repository: [row['name'] for row in repository.execute("select to_char(now(), 'YYYY-MM-DD HH24:MI:SS.MS') as name")][0]
getnodeparentid = lambda repository, id: [row['pid'] for row in repository.execute("select parent as pid from nodes where id = " + str(id))][0]
getrootid = lambda repository: [row['rid'] for row in repository.execute("select id as rid from nodes where parent is null")][0]
getprogeny = lambda repository, id:  [row['rid'] for row in repository.execute("with recursive tree as (select id, parent from nodes where id = " + str(id) + " union all select p.id, p.parent from nodes p join tree c on p.parent = c.id) select id as rid from tree where id != " + str(id))]
getancestors = lambda repository, id:  [x for x in reversed([row['rid'] for row in repository.execute("with recursive tree as (select id, parent from nodes where id = " + str(id) + " union all select p.id, p.parent from nodes p join tree c on p.id = c.parent) select id as rid from tree where id != " + str(id))])]
fff1 = lambda repository, id, name: [row['rid'] for row in repository.execute("select id as rid from nodes where parent = " + str(id) + " and name = '" + name + "'")]
getnodesidfromp = lambda repository, id: [row['rid'] for row in repository.execute("select id as rid from nodes where parent = " + str(id))]
getnodeidfrompn = lambda repository, id, name: fff1(repository, id, name)[0] if len(fff1(repository, id, name)) > 0 else None
getpath = lambda context, repository, id: ('/'.join([x['name'] for x in [context.getnode(i) for i in getancestors(repository, id)]]) + '/' + context.getnode(id)['name'])[1:]
ftype = lambda x: x['icon']
getkey = lambda x: x['text']
ficon = lambda node: ("fa fa-trash btnt", "fa fa-trash-o btnt", "fa fa-trash btnt") if node['icon'] == 'T' else ("fa fa-folder btnb", "fa fa-folder-open btnb", "fa fa-folder btnb") if node['icon'] == 'B' else ("fa fa-folder btna", "fa fa-folder-open btna", "fa fa-folder btna") if node['icon'] == 'A' else ("fa fa-folder btnc", "fa fa-folder-open btnc", "fa fa-folder btnc") if node['icon'] == 'C' else ("fa fa-folder btnl", "fa fa-folder-open btnl", "fa fa-folder btnl") if node['icon'] == 'L' else ("fa fa-database btnd", "fa fa-database btnd", "fa fa-database btnd") if node['icon'] == 'D' else ("fa fa-folder btnn", "fa fa-folder-open btnn", "fa fa-folder btnn")
depthp = lambda d, n: 0 if d[n] == None else depthp(d, d[n]) + 1
nullistener = lambda col, d, v, n: None
getchartproducers = lambda node: [k['path'] for k in node['datasource']['producers']] if 'producers' in node['datasource'] and node['datasource']['type'] == 'C' else []
getcolor = lambda colors, x: colors[x] if x in colors else '#' + hashlib.md5(x.encode('utf-8')).hexdigest()[0:6]

def getfontsize(width, binf=1000, bsup=2000, vinf=0, vsup=0):
    if width <= binf: return int(vinf)
    if width >= bsup: return int(vsup)
    return int(vinf + ((vsup - vinf) / (bsup - binf)) * (width - binf))

def getyposition(yaxis, width, numleftyaxis=1, binf=1000, bsup=2000, vinf=0.08, vsup=0.05, rows=1):
    begposition = yaxis['position']
    if begposition == 0: return begposition
    if begposition == 0.05 and numleftyaxis / rows == 1: return 0
    if begposition == 0.05:
        if width <= binf: return vinf
        if width >= bsup: return vsup
        return vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))
    if begposition == 0.90:
        if width <= binf: return 1 - (2 * vinf)
        if width >= bsup: return 1 - (2 * vsup)
        return 1 - (2 * (vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))))
    if begposition == 0.95:
        if width <= binf: return 1 - vinf
        if width >= bsup: return 1 - vsup
        return 1 - (1 * (vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))))

def getaposition(width, index=0, numleftyaxis=1, numrightyaxis=0, numxaxis=1, binf=1000, bsup=2000, vinf=0.08, vsup=0.05, rows=1):
    if rows == 1:
        cols = numxaxis
        nbseparators = cols - 1
        lengthseparator = 0.02
        lengthseparators = lengthseparator * nbseparators
        lengthaxis = vinf if width <= binf else vsup if width >= bsup else vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))
        lengthaxis = 0 if numleftyaxis + numrightyaxis == 0 else lengthaxis
        availablespace = 1 - ((numleftyaxis + numrightyaxis - 1) * lengthaxis) - 2 * lengthseparator
        lengthdomain = (availablespace - lengthseparators) / cols 
        positiondomain = (numleftyaxis - 1) * lengthaxis + lengthseparator + index * (lengthdomain + lengthseparator) 
        return positiondomain + lengthdomain / 2
    else:
        nbseparators = rows - 1
        lengthseparator = 0.02
        lengthseparators = lengthseparator * nbseparators
        availablespace = 1 - lengthseparators
        lengthdomain = (availablespace - lengthseparators) / rows
        positiondomain = lengthdomain + index * (lengthdomain + lengthseparator * 2)
        return positiondomain

def getdomain(width, index=0, numleftyaxis=1, numrightyaxis=0, numxaxis=1, binf=1000, bsup=2000, vinf=0.08, vsup=0.05, rows=1):
    cols = numxaxis if rows == 1 else 1
    nbseparators = cols - 1
    lengthseparator = 0.02
    lengthseparators = lengthseparator * nbseparators
    lengthaxis = vinf if width <= binf else vsup if width >= bsup else vinf + ((vsup -vinf) / (bsup - binf) * (width - binf))
    lengthaxis = 0 if numleftyaxis + numrightyaxis == 0 else lengthaxis
    availablespace = 1 - ((numleftyaxis / rows + numrightyaxis / rows  - 1) * lengthaxis) - 2 * lengthseparator
    lengthdomain = (availablespace - lengthseparators) / cols 
    positiondomain = (numleftyaxis / rows  - 1) * lengthaxis + lengthseparator + index * (lengthdomain + lengthseparator)
    return [positiondomain, positiondomain+lengthdomain]

def replaceeval(obj, contextvariables, recursive=False):
    if not recursive:
        for e in obj:
            obj[e] = replaceeval(obj[e], contextvariables, recursive=True)
    if type(obj) == type('a'):
        with suppress(Exception): obj = obj % contextvariables
    elif type(obj) == type([]):
        i=0
        for e in obj:
            obj[i] = replaceeval(e, contextvariables, recursive=True)
            i+=1
    elif type(obj) == type({}):
        for e in obj:
            obj[e] = replaceeval(obj[e], contextvariables, recursive=True)
    else: pass
    return obj


def gettimestampdf(d, co, plotorientation):
    converttime = lambda x: datetime.strptime(x, '%Y%m%d%H%M%S%f')
    if  'timestamp' not in d[0] and plotorientation == 'horizontal':
        co['cols'] = len(d)
        co['isarray'] = True
    if  'timestamp' not in d[0] and plotorientation == 'vertical': 
        co['rows'] = len(d)
        co['isarray'] = True
    ret = []
    if co['isarray']:
        for x in d:
            r = pandas.DataFrame(data=x)
            r['timestamp'] = r['timestamp'].apply(converttime)
            r = r.set_index('timestamp').sort_index()
            ret.append(r)
    else:
        r = pandas.DataFrame(data=d)
        r['timestamp'] = r['timestamp'].apply(converttime)
        r = r.set_index('timestamp').sort_index()
        ret.append(r)
    return ret

def getnewaxis(co, reftimedf, template, axistype=None, options=None, index=0):
    if axistype == 'y' and index not in co['alreadyright']: co['alreadyright'][index] = False
    if axistype == 'y' and index not in co['alreadyleft']: co['alreadyleft'][index] = False
    d = co['yaxis'] if axistype == 'y' else co['xaxis']
    l = len(d)
    d[l] = dict()
    d[l]['name'] = axistype + 'axis' if l == 0 else  axistype + 'axis' + str(l + 1)
    d[l]['smallname'] = axistype if l == 0 else axistype + str(l + 1)
    if axistype == 'y':
        for e in template['yaxis']: d[l][e] = template['yaxis'][e].copy() if type(template['yaxis'][e]) == type(dict()) else template['yaxis'][e]
        d[l]['options']['title'] = options['title']
        if 'properties' in options and 'line' in options['properties'] and 'stroke' in options['properties']['line']: 
            d[l]['options']['tickfont'] = dict(color = options['properties']['line']['stroke'])
            d[l]['options']['color'] = options['properties']['line']['stroke']
            d[l]['options']['linecolor'] = options['properties']['line']['stroke']
        if 'properties' in options and 'text' in options['properties'] and 'fill' in options['properties']['text']: 
            d[l]['options']['titlefont'] = dict(color = options['properties']['text']['fill'])
        d[l]['options']['side'] = options['position'].lower()
        if d[l]['options']['side'] == 'left' and not co['alreadyleft'][index]: d[l]['options']['position'] = 0.05
        if d[l]['options']['side'] == 'left' and co['alreadyleft'][index]: 
            d[l]['options']['position'] = 0.00
            d[l]['options']['overlaying'] = 'y' if index == 0 else 'y' + str(index + 1)
        if d[l]['options']['side'] == 'right' and not co['alreadyright'][index]: 
            d[l]['options']['overlaying'] = 'y' if index == 0 else 'y' + str(index + 1)
            d[l]['options']['position'] = 0.95
        if d[l]['options']['side'] == 'right' and co['alreadyright'][index]: 
            d[l]['options']['overlaying'] = 'y' if index == 0 else 'y' + str(index + 1)
            d[l]['options']['position'] = 0.90
        if d[l]['options']['side'] == 'left': co['alreadyleft'][index] = True
        if d[l]['options']['side'] == 'right': co['alreadyright'][index] = True
        rows = co['rows']
        nbseparators = rows - 1
        lengthseparator = 0.02
        lengthseparators = lengthseparator * nbseparators
        lengthdomain = (1 - lengthseparators) / rows 
        positiondomain = 0.0 + index * (lengthdomain + lengthseparator)
        d[l]['options']['domain'] = [positiondomain, positiondomain + lengthdomain]
    else:
        for e in template['xaxis']: d[l][e] = template['xaxis'][e].copy() if type(template['xaxis'][e]) == type(dict()) else template['xaxis'][e]
        cols = co['cols']
        nbseparators = cols - 1
        lengthseparator = 0.02
        lengthseparators = lengthseparator * nbseparators
        lengthdomain = (0.8 - lengthseparators) / cols 
        positiondomain = 0.1 + index * (lengthdomain + lengthseparator)
        d[l]['options']['domain'] = [positiondomain, positiondomain + lengthdomain]
        d[l]['options']['range'] = [reftimedf[index].index.min(),reftimedf[index].index.max()]
    logging.debug('Axis index: ' + str(index) + ', options: ' + str(d[l]))
    return l

def paddeddf(t, d):
    r = t.copy()
    r['a'] = 0
    r['b'] = d['value']
    r['value'] = r['a'] + r['b'].fillna(0)
    return r

def settrace(co, r, dataframe=None, label=None, yaxisindex=0, index=0, alreadyinlegend = None, groupname=None, plotorientation=None, colors=None):
    param = dict()
    param['x'] = dataframe.index
    param['y'] = dataframe['value']
    param['name'] = label
    param['legendgroup'] = label
    param['showlegend'] = True if label not in alreadyinlegend else False
    alreadyinlegend[label] = True
    if r['type'] == 'L': 
        param['line'] = dict(color=(getcolor(colors, label)), shape='spline')
        trace = plotly.graph_objs.Scatter(**param)
    if r['type'] == 'A': 
        param['mode'] = 'lines'
        param['fill'] = 'tozeroy'
        param['fillcolor'] = getcolor(colors, label)
        param['line'] = dict(color=(getcolor(colors, label)), shape='spline')
        trace = plotly.graph_objs.Scatter(**param)
    if r['type'] == 'SA':  
        param['line'] = dict(color=(getcolor(colors, label)), shape='spline')
        param['mode'] = 'lines'
        param['stackgroup'] = groupname
        param['fillcolor'] = getcolor(colors, label)
        trace = plotly.graph_objs.Scatter(**param)
    if r['type'] == 'C': 
        param['marker']=dict(color=getcolor(colors, label))
        trace = plotly.graph_objs.Bar(**param)
        co['layoutoptions']['barmode'] = 'group'
    if r['type'] == 'CC': 
        param['marker']=dict(color=getcolor(colors, label))
        trace = plotly.graph_objs.Bar(**param)
        co['layoutoptions']['barmode'] = 'group'
    if r['type'] == 'SC':
        param['marker']=dict(color=getcolor(colors, label))
        trace = plotly.graph_objs.Bar(**param)
        co['layoutoptions']['barmode'] = 'stack'
    l = len(co['traces'])
    xaxis = index if co['shared_yaxes'] else 0
    yaxis = yaxisindex
    row = 1 if plotorientation=='horizontal' else index+1
    col = index+1 if plotorientation=='horizontal' else 1
    logging.debug('settrace, xaxis: ' + str(xaxis) + ', yaxis: ' + str(yaxis) + ', row: ' + str(row) + ', col:' + str(col) + ', label: ' + str(label))
    co['traces'][l] = dict(trace=trace, yaxis=yaxis, xaxis=xaxis, row=row, col=col)

class Object: pass


class Status:
    def __init__(s):
        s.errors = 0
        s.errormessages = []
    
    def pusherrmessage(s, m):
        logging.error(m)
        s.errormessages.append(m)
        s.errors = s.errors + 1

class Context:
    
    def __init__(s, nodesdb=None, systemdb=None, postgres=False, autocommit=True):
        s.nodesdb = nodesdb
        s.systemdb = systemdb
        s.postgresdb = postgres
        s.removecollections  = []
        s.createcollections  = []
        s.grepo = Repository() if postgres else None
        s.nrepo = Repository(nodesdb) if nodesdb else None
        s.srepo = Repository(systemdb) if systemdb else None
        s.cache = dict(nodes=dict(), objects=dict(chart=dict(), query=dict(), analyzer=dict(), liveobject=dict(), template=dict(), color=dict(), aggregator=dict(), function=dict(), layout=dict(), choice=dict()))
        s.status = Status()
        s.variables = dict()
        s.nocache = False
    
    def free(s):
        if s.postgresdb: s.grepo.disconnect()
        if s.nodesdb: s.nrepo.disconnect()
        if s.systemdb: s.srepo.disconnect()
        if s.status.errors > 0:
            for m in s.status.errormessages: logging.error(m)

    def setschema(s, schema=None):
        s.nrepo.setschema(schema)

    def createsystem(s):
        r = s.grepo
        databases = getdatabases(r)
        if 'kairos_system_system' in databases: return
        r.execute("create database kairos_system_system with encoding 'utf8'")
        s.systemdb = 'kairos_system_system'
        s.srepo = Repository(s.systemdb)
        r = s.srepo
        r.execute("create language plpython3u")
        r.execute("create sequence objid start 1")
        r.execute("create table objects(rid integer primary key, id text, type name, created timestamp, filename text, stream bytea)")
        r.execute("create unique index iobjects on objects(type, id)")        

    def createuser(s, user, skiperror=False):
        curdatabase = "kairos_user_" + user
        r = s.grepo
        databases = getdatabases(r)
        if curdatabase in databases:
            if not skiperror: s.status.pusherrmessage(user + ' user already exists!')
            return dict()
        r.execute("create database kairos_user_" + user + " with encoding 'utf8'")
        r.execute("create user " + user + " password '" + user + "'")
        s.nodesdb = curdatabase
        s.nrepo = Repository(s.nodesdb)
        r = s.nrepo
        r.execute("create language plpython3u")
        r.execute("create extension oracle_fdw")
        r.execute("create extension postgres_fdw")
        r.execute("create sequence objid start 1")
        r.execute("create table objects(rid integer primary key, id text, type name, created timestamp, filename text, stream bytea)")
        r.execute("create unique index iobjects on objects(type, id)")        
        r.execute("create table nodes(id integer primary key, parent integer, name text, type text, created timestamp, status text, liveobject text, aggregatorselector text, aggregatorsort text, aggregatortake integer, aggregatorskip integer, aggregatormethod text, aggregatortimefilter text, aggregated timestamp, producers text)")
        r.execute("create table settings(colors text, logging text, nodesdb text, plotorientation text, systemdb text, template text, top integer, wallpaper text)")
        r.execute("create table sources(id integer primary key, created timestamp, collections text, stream bytea)")
        r.execute("create table caches(id integer primary key, name text, created timestamp, queries text, collections text)")
        r.execute("insert into settings(colors, logging, nodesdb, plotorientation, systemdb, template, top, wallpaper) values ('COLORS', 'info', 'kairos_user_" + user + "', 'horizontal', 'kairos_system_system', 'DEFAULT', 15, 'DEFAULT')")
        rootid = getnextid(r)
        r.execute("insert into nodes(id, parent, name, type, created, status) values (" + str(rootid) + ", null, '/', 'N', now(), 'ACTIVE')")
        trashid = getnextid(r)
        r.execute("insert into nodes(id, parent, name, type, created, status) values (" + str(trashid) + ", " + str(rootid) + ", 'Trash', 'T', now(), 'DELETED')")
        with suppress(Exception): shutil.rmtree('/autoupload/' + curdatabase)
        os.mkdir('/autoupload/' + curdatabase)
        return dict(data=dict(msg=user + " user has been successfully created!"))
        
    def createrole(s, role):
        curdatabase = "kairos_group_" + role
        r = s.grepo
        databases = getdatabases(r)
        if curdatabase in databases:
            s.status.pusherrmessage(role + ' role already exists!')
            return dict()
        r.execute("create database kairos_group_" + role + " with encoding 'utf8'")
        r.execute("create role " + role)
        s.nodesdb = curdatabase
        s.nrepo = Repository(s.nodesdb)
        r = s.nrepo
        r.execute("create language plpython3u")
        r.execute("create extension oracle_fdw")
        r.execute("create extension postgres_fdw")
        r.execute("create sequence objid start 1")
        r.execute("create table objects(rid integer primary key, id text, type name, created timestamp, filename text, stream bytea)")
        r.execute("create unique index iobjects on objects(type, id)")        
        r.execute("create table nodes(id integer primary key, parent integer references nodes(id), name text, type text, created timestamp, status text, liveobject text, aggregatorselector text, aggregatorsort text, aggregatortake integer, aggregatorskip integer, aggregatormethod text, aggregatortimefilter text, aggregated timestamp, producers text)")
        r.execute("create table sources(id integer primary key, created timestamp, collections text, stream bytea)")
        r.execute("create table caches(id integer primary key, name text, created timestamp, queries text, collections text)")
        rootid = getnextid(r)
        r.execute("insert into nodes(id, parent, name, type, created, status) values (" + str(rootid) + ", null, '/', 'N', now(), 'ACTIVE')")
        trashid = getnextid(r)
        r.execute("insert into nodes(id, parent, name, type, created, status) values (" + str(trashid) + ", " + str(rootid) + ", 'Trash', 'T', now(), 'DELETED')")
        with suppress(Exception): shutil.rmtree('/autoupload/' + curdatabase)
        os.mkdir('/autoupload/' + curdatabase)
        return dict(data=dict(msg=role + " role has been successfully created!"))

    def deleteuser(s, user):
        if user=='admin': 
            s.status.pusherrmessage('admin user cannot be removed!')
            return dict()
        dbuser = "kairos_user_" + user
        r = s.grepo
        r.execute("drop database " + dbuser)
        r.execute("drop user " + user)
        return dict(data=dict(msg=user + " user has been successfully removed!"))

    def deleterole(s, role):
        dbgroup = "kairos_group_" + role
        r = s.grepo
        r.execute("drop database " + dbgroup)
        r.execute("drop role " + role)
        return dict(data=dict(msg=role + " role has been successfully removed!"))

    def creategrant(s, user, role):
        r = s.grepo
        databases = getdatabases(r)
        dbgroup = "kairos_group_" + role
        dbuser = "kairos_user_" + user
        if dbgroup not in databases:
            s.status.pusherrmessage(role + " role doesn't exist!")
            return dict()
        if dbuser not in databases:
            s.status.pusherrmessage(user + " user doesn't exist!")
            return dict()
        x = r.execute("select groname,usename from pg_group,pg_user where usesysid = any(grolist) and groname='" + role + "' and usename='" + user + "'")
        if len([row for row in x.fetchall()]) > 0:
            s.status.pusherrmessage(user + " user is already granted with " + role + " role!")
            return(dict())
        for row in x.fetchall(): data.append(dict(_id=row['usename'] + ':' + row['groname'], user=row['usename'], role=row['groname']))
        r.execute("grant " + role + " to " + user)
        return dict(data=dict(msg=role + " role has been successfully granted to " + user + " user!"))

    def deletegrant(s, user, role):
        r = s.grepo
        r.execute("revoke " + role + " from " + user)
        return dict(data=dict(msg=user + " user has been successfully revoked from " + role + " role!"))

    def resetpassword(s, user):
        if user=='admin':
            s.status.pusherrmessage('admin password cannot be reset!')
            return dict()
        dbuser = "kairos_user_" + user
        r = s.grepo
        r.execute("alter user " + user + " password '" + user + "'")
        return dict(data=dict(msg=user + " password has been successfully reset!"))

    def changepassword(s, user, password):
        r = s.grepo
        r.execute("alter user " + user + " password '" + password + "'")

    def getsettings(s):
        r = s.nrepo
        y = r.execute("select top, colors, logging, nodesdb, systemdb, template, wallpaper, plotorientation from settings")
        settings = dict()
        for row in y.fetchall():
            for x in row.keys(): settings[x] = row[x]
        return settings

    def updatesettings(s, newsettings):
        r = s.nrepo
        r.execute("delete from settings")
        r.execute("insert into settings(colors, logging, nodesdb, plotorientation, systemdb, template, top, wallpaper) values ('" + newsettings['colors'] +"', '" + newsettings['logging'] +"', '" + newsettings['nodesdb'] +"', '" + newsettings['plotorientation'] + "', '" + newsettings['systemdb'] + "', '" + newsettings['template'] + "', " + str(newsettings['top']) + ", '" + newsettings['wallpaper'] + "')")

    def listdatabases(s, user, adminrights):
        r = s.grepo
        data = []
        databases = getdbsizes(r)
        groups = getgroupdatabases(r, user)
        for k in databases:
            if adminrights:
                data.append(dict(name=k, size=databases[k] * 1.0 / 1024 / 1024))
            else:
                if k == 'kairos_user_' + user:
                    data.append(dict(name=k, size=databases[k] * 1.0 / 1024 / 1024))
                if 'kairos_group_' in k:
                    if k in groups:
                        data.append(dict(name=k, size=databases[k] * 1.0 / 1024 / 1024))
        return data
    
    def listroles(s):
        r = s.grepo
        databases = getdatabases(r)
        data = [dict(_id=k.replace('kairos_group_',''), role=k.replace('kairos_group_','')) for k in databases if 'kairos_group_' in k]
        return data
    
    def listusers(s):
        r = s.grepo
        databases = getdatabases(r)
        data = [dict(_id=k.replace('kairos_user_',''), user=k.replace('kairos_user_','')) for k in databases if 'kairos_user_' in k]
        return data

    def listgrants(s):
        r = s.grepo
        data = [dict(_id=row['usename'] + ':' + row['groname'], user=row['usename'], role=row['groname']) for row in r.execute("select groname,usename from pg_group,pg_user where usesysid = any(grolist)")]
        return data

    def listsystemdb(s):
        r = s.grepo
        databases = getdatabases(r)
        data = [dict(name=k) for k in databases if 'kairos_system_' in k]
        return data

    def listnodesdb(s, user):
        r = s.grepo
        databases = getdatabases(r)
        groupdb = getgroupdatabases(r, user)
        data = [dict(name=k) for k in databases if k == 'kairos_user_' + user or k in groupdb]
        return data

    def listobjects(s, where):
        data = []
        listdb = []
        if s.nodesdb: listdb.append(s.nodesdb)
        if s.systemdb: listdb.append(s.systemdb)
        for db in listdb:
            r = s.nrepo if db == s.nodesdb else s.srepo
            for row in r.execute("select rid, id, type, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created from objects " + where):
                item = dict()
                for x in row.keys(): item[x] = row[x]
                item['origin'] = db
                data.append(item)
        return data
    
    def readobjects(s, where, evalobject=True, allbases=False):
        data = []
        interrupt = False
        for db in [s.nodesdb, s.systemdb]:
            if interrupt and not allbases: break
            r = s.nrepo if db == s.nodesdb else s.srepo
            for row in r.execute("select filename, stream as content, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created from objects " + where):
                source = binascii.a2b_base64(row['content'])
                filename = row['filename']
                created = row['created']
                p = compile(source, filename, 'exec')
                #locals()['kairos'] = s.variables
                true = True
                false = False
                null = None
                exec(p, locals())
                obj = locals()['UserObject']()
                obj['origin'] = db
                obj['created'] = created
                if evalobject: obj = replaceeval(obj, s.variables)
                data.append(obj)
                interrupt = True
        return data

    def getobject(s, id, typeobj):
        if id not in s.cache['objects'][typeobj]:
            objs = s.readobjects("where id='" + id + "' and type='" + typeobj + "'")
            if len(objs) == 0: return None
            s.cache['objects'][typeobj][id]= objs[0]
        return s.cache['objects'][typeobj][id]

    def getanalyzer(s, id): 
        analyzer = s.getobject(id, 'analyzer')
        if analyzer == None: s.status.pusherrmessage("Analyzer '" + id +"' doesn't exist!")
        return analyzer

    def getliveobject(s, id): 
        liveobject = s.getobject(id, 'liveobject')
        if liveobject == None: s.status.pusherrmessage("Liveobject '" + id +"' doesn't exist!")
        return liveobject

    def gettemplate(s, id): 
        template = s.getobject(id, 'template')
        if template == None: s.status.pusherrmessage("Template '" + id +"' doesn't exist!")
        return template

    def getcolors(s, id): 
        colors = s.getobject(id, 'color')
        if colors == None: s.status.pusherrmessage("Colors '" + id +"' doesn't exist!")
        return colors

    def getchart(s, id): 
        chart = s.getobject(id, 'chart')
        if chart == None: s.status.pusherrmessage("Chart '" + id +"' doesn't exist!")
        return chart

    def getaggregator(s, id): 
        aggregator = s.getobject(id, 'aggregator')
        if aggregator == None: s.status.pusherrmessage("Aggregator '" + id +"' doesn't exist!")
        return aggregator

    def getfunction(s, id): 
        function = s.getobject(id, 'function')
        if function == None: s.status.pusherrmessage("Function '" + id +"' doesn't exist!")
        return function

    def getlayout(s, id): 
        layout = s.getobject(id, 'layout')
        if layout == None: s.status.pusherrmessage("Layout '" + id +"' doesn't exist!")
        return layout

    def getchoice(s, id): 
        choice = s.getobject(id, 'choice')
        if choice == None: s.status.pusherrmessage("Choice '" + id +"' doesn't exist!")
        return choice

    def getquery(s, id): 
        query = s.getobject(id, 'query')
        return query

    def getmenus(s):
        return s.readobjects("where type='menu'", allbases=True)

    def writeobject(s, source):
        r = s.nrepo
        p = compile(source, 'stream', 'exec')
        kairos = dict()
        true = True
        false = False
        null = None
        exec(p, locals())
        obj = locals()['UserObject']()
        typeobj = obj['type']
        id = obj['id']
        filename = id.lower() + '.py'
        content = binascii.b2a_base64(source.encode())
        r.execute("delete from objects where id='" + str(id) + "' and type='" + typeobj +"'")
        objid = getnextid(r)
        r.executep("insert into objects(rid, id, type, created, filename, stream) values (%s, %s, %s, now(), %s, %s)", (objid, id, typeobj, filename, content))
        return (id, typeobj)

    def getobjectstream(s, id, otype):
        r = s.nrepo
        result = dict()
        for row in r.execute("select filename, stream from objects where id='" + str(id) +"' and type = '" + otype + "'"):
            for x in row.keys(): result[x] = row[x]
        return (result['filename'], binascii.a2b_base64(result['stream']))

    def uploadobject(s, multipart):
        upload = multipart['file']
        filename = upload.filename
        content = upload.file.read()
        uploadtype = upload.content_type
        if uploadtype == 'image/jpeg':
            typeobj = 'wallpaper'
            id = filename.replace('.jpg', '')
        else:
            p = compile(content, filename, 'exec')
            kairos = dict()
            true = True
            false = False
            null = None
            exec(p, locals())
            obj = locals()['UserObject']()
            typeobj = obj['type']
            id = obj['id']
        content = binascii.b2a_base64(content)
        r = s.nrepo
        r.execute("delete from objects where id='" + str(id) + "' and type='" + typeobj +"'")
        objid = getnextid(r)
        r.executep("insert into objects(rid, id, type, created, filename, stream) values (%s, %s, %s, now(), %s, %s)", (objid, id, typeobj, filename, content))
        return (id, filename, typeobj)
    
    def deleteobject(s, id, typeobj):
        r = s.nrepo
        r.execute("delete from objects where id='" + str(id) + "' and type='" + typeobj + "'")

    def deletesource(s, id):
        r = s.nrepo
        r.execute("delete from sources where id=" + str(id))

    def createsource(s, nid, stream, filename):
        filepath = '/tmp/' + s.nodesdb + '_' + str(nid) + '.zip'
        infile = Arcfile(stream, 'r')
        ziparchive = Arcfile(filepath, 'w:zip')
        for m in infile.list(): ziparchive.write(m, infile.read(m))
        ziparchive.close()
        collections = dict()
        def listener(col, d, v, n):
            for x in v['collections']:
                if x not in collections: collections[x] = dict(analyzer=v['analyzer'],members=[])
                collections[x]['members'].append(v['member'])
        analmain = s.getanalyzer('ANALMAIN')
        analyzer = Analyzer(analmain, {}, listener, None)
        def do(member):
            analyzer.analyze(ziparchive.read(member), member)
            return None
        ziparchive = Arcfile(filepath, 'r')
        for member in ziparchive.list(): do(member)
        ziparchive.close()
        r = s.nrepo
        f=open(filepath, 'rb')
        content = binascii.b2a_base64(f.read())
        f.close()
        os.unlink(filepath)
        r.executep("insert into sources (id, created, collections, stream) values(%s, now(), %s, %s)", (nid, json.dumps(collections), content))
        r.execute("update nodes set type = 'B' where id = " + str(nid))

    def readnode(s, id):
        r = s.nrepo
        projection = "id as rid, type, name, status, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created, liveobject, aggregatorselector, aggregatorsort, aggregatortake, aggregatorskip, aggregatormethod, aggregatortimefilter, to_char(aggregated, 'YYYY-MM-DD HH24:MI:SS.MS') as aggregated, producers"
        selectednodes = [row for row in r.execute("select " + projection + " from nodes where id = " + str(id))]
        nodes=[]
        for row in selectednodes:
            node = dict(datasource=dict(cache=dict()))
            node['id'] = row['rid']
            node['name'] = row['name']
            node['icon'] = row['type']
            node['status'] = row['status']
            node['created'] = row['created']
            node['datasource']['type'] = row['type']
            node['datasource']['producers'] = json.loads(row['producers']) if 'producers' in row  and row['producers'] else []
            if row['type'] in ['A', 'L']:
                node['datasource']['aggregated'] = row['aggregated'] if 'aggregated' in row and row['aggregated'] else None
                node['datasource']['aggregatorselector'] = row['aggregatorselector'] if 'aggregatorselector' in row and row['aggregatorselector'] else '/'
                node['datasource']['aggregatorsort'] = row['aggregatorsort'] if 'aggregatorsort' in row and row['aggregatorsort'] else 'desc'
                node['datasource']['aggregatortake'] = row['aggregatortake'] if 'aggregatortake' in row and row['aggregatortake'] else 1
                node['datasource']['aggregatorskip'] = row['aggregatorskip'] if 'aggregatorskip' in row and row['aggregatorskip'] else 0
                node['datasource']['aggregatormethod'] = row['aggregatormethod'] if 'aggregatormethod' in row and row['aggregatormethod'] else '$none'
                node['datasource']['aggregatortimefilter'] = row['aggregatortimefilter'] if 'aggregatortimefilter' in row and row['aggregatortimefilter'] else '.'
            if row['type'] in ['D']:
                node['datasource']['liveobject'] = row['liveobject']
                d = dict()
                with suppress(Exception):
                    liveobject = s.getliveobject(row['liveobject'])
                    for e in liveobject['tables']: d[e] = True
                node['datasource']['collections'] = d
            nodes.append(node)
        return nodes
    
    def countchildren(s, node):
        r = s.nrepo
        for row in r.execute("select count(*) as count from nodes where parent = " + str(node['id'])): node['kids'] = row['count']

    def getnode(s, id):
        r = s.nrepo
        if id not in s.cache['nodes']:
            lnodes = s.readnode(id)
            if len(lnodes) == 0: return None
            s.cache['nodes'][id] = lnodes[0]
        return s.cache['nodes'][id]

    def deletenode(s, id):
        r = s.nrepo
        node = s.getnode(id)
        if node == None:
            s.status.pusherrmessage('Node with id: ' + str(id) + " doesn't exist!")
            return
        s.getcache(node)
        s.getsource(node)
        rootid = getrootid(r)
        trashid = getnodeidfrompn(r, rootid, 'Trash')
        if rootid == node['id']: 
            s.status.pusherrmessage('Root node cannot be removed!')
            return
        if trashid == node['id']: 
            s.status.pusherrmessage('A trash cannot be removed!')
            return
        listnodes = getprogeny(r, id)
        listnodes.append(id)
        if node['status'] == 'DELETED':
            for rid in listnodes:
                s.deletesource(rid)
                s.deletecache(rid)
                r.execute("delete from nodes where id = " + str(rid))
        else:
            r.execute("update nodes set parent = " + str(trashid) + " where id = " + str(id))
            for rid in listnodes: r.execute("update nodes set status = 'DELETED' where id = " + str(rid))
    
    def uploadnode(s, id, multipart):
        r = s.nrepo
        upload = multipart['file']
        filename = urllib.parse.unquote(upload.filename)
        id = getrootid(r) if id == None else id
        node = s.getnode(id)
        (base, ext) = os.path.splitext(filename)
        while ext != '': (base, ext) = os.path.splitext(base)
        nodes = base.split('_')
        for d in nodes:
            nid = getnodeidfrompn(r, node['id'], d)
            if nid == None:
                child = s.createnode(node['id'], d)
                node = s.getnode(child)
            else:
                node = s.getnode(nid)
        id = node['id']
        s.deletesource(id)
        s.createsource(id, upload.file, filename)
        return filename
    
    def createnode(s, pid, name=None):
        r = s.nrepo
        name = getdefaultnodename(r) if not name else name
        objid = getnextid(r)
        r.execute("insert into nodes(id, parent, name, type, created, status) values (" + str(objid) + ", " + str(pid) + ", '" + name + "', 'N', now(), 'ACTIVE')")
        return objid

    def renamenode(s, id, new):
        r = s.nrepo
        node = s.getnode(id)
        rootid = getrootid(r)
        if rootid == node['id']:
            s.status.pusherrmessage('Root node cannot be renamed!')
            return node
        if node['datasource']['type'] == 'T':
            s.status.pusherrmessage('A trash cannot be renamed!')
            return node
        pid = getnodeparentid(r, id)
        parent = s.getnode(pid)
        x = getnodeidfrompn(r, pid, new)
        if x!= None:
            s.status.pusherrmessage(new + " is already a child for node: " + parent['name'])
            return node
        r.execute("update nodes set name = '" + new + "' where id = " + str(id))
        del s.cache['nodes'][id]
        node = s.getnode(id)
        return node
    
    def movenode(s, pfrom, pto):
        r = s.nrepo
        fromnode = s.getnode(pfrom)
        if fromnode['datasource']['type'] == 'T':
            s.status.pusherrmessage('A trash cannot be moved!')
            return fromnode
        tonode = s.getnode(pto)
        r.execute("update nodes set parent = " + str(pto) + " where id = "  + str(pfrom))
        status = [row['status'] for row in r.execute("select status from nodes where id = " + str(pto))][0]
        listnodes = getprogeny(r, pfrom)
        for rid in listnodes: r.execute("update nodes set status = '" + status + "' where id = " + str(rid))
        del s.cache['nodes'][pfrom]
        node = s.getnode(pfrom)
        return node

    def compareaddnode(s, fid, tid):
        r = s.nrepo
        fnode = s.getnode(fid)
        tnode = s.getnode(tid)
        if fnode['status'] == 'DELETED' or tnode['status'] == 'DELETED':
            s.status.pusherrmessage('A deleted element cannot be part of a compare operation!')
            return tnode
        for e in tnode['datasource']['producers']:
            if fid == e['id']:
                s.status.pusherrmessage(str(fid) + ": this node is already included in the list of producers!")
                return tnode
        producers = tnode['datasource']['producers']
        producers.append(dict(path=getpath(s, r, fid), id=fid))
        s.getsource(tnode)
        r.execute("update nodes set type='C', producers='" + json.dumps(producers) + "' where id =" + str(tid))
        del s.cache['nodes'][tid]
        tnode = s.getnode(tid)
        s.getsource(tnode)
        return tnode

    def aggregateaddnode(s, fid, tid):
        r = s.nrepo
        fnode = s.getnode(fid)
        tnode = s.getnode(tid)
        if fnode['status'] == 'DELETED' or tnode['status'] == 'DELETED':
            s.status.pusherrmessage('A deleted element cannot be part of an aggreagte operation!')
            return tnode
        for e in tnode['datasource']['producers']:
            if fid == e['id']:
                s.status.pusherrmessage(str(fromid) + ": this node is already included in the list of producers!")
                return tnode
        producers = tnode['datasource']['producers']
        producers.append(dict(path=getpath(s, r, fid), id=fid))
        s.getsource(tnode)
        if 'aggregatorselector' not in tnode['datasource']:
            r.execute("update nodes set type='A', producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + getpath(s, r, fid) + '$' + "', aggregatortake=1, aggregatortimefilter='.', aggregatorskip=0, aggregatorsort='desc', aggregatormethod='$none' where id =" + str(tid))
        else:
            r.execute("update nodes set producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + tnode['datasource']['aggregatorselector'] + '|' + getpath(s, r, fid) + '$' +"', aggregatortake=" + str(int(tnode['datasource']['aggregatortake']) +  1) + " where id =" + str(tid))
        del s.cache['nodes'][tid]
        tnode = s.getnode(tid)
        s.getsource(tnode)
        return tnode
    
    def applyaggregator(s, id, aggregatorselector, aggregatortake, aggregatorskip, aggregatortimefilter, aggregatorsort, aggregatormethod):
        r = s.nrepo
        node = s.getnode(id)
        if node['datasource']['type'] in ['A']:
            if node['datasource']['aggregatormethod'] != aggregatormethod or node['datasource']['aggregatortimefilter'] != aggregatortimefilter:
                logging.info("Node: " + str(id) + ", Type: " + node['datasource']['type'] + ", deleting cache ...")
                s.deletecache(id)
        if node['datasource']['type'] in ['A', 'N']:  
            producers = s.expand(aggregatorselector, aggregatorsort, aggregatortake, aggregatorskip)
            for pid in [p['id'] for p in producers]:
                pnode = s.getnode(pid)
                ds = pnode['datasource']
                if pnode['datasource']['type'] in ['A']: s.applyaggregator(pid, ds['aggregatorselector'], ds['aggregatortake'], ds['aggregatorskip'], ds['aggregatortimefilter'], ds['aggregatorsort'], ds['aggregatormethod'])
            s.getsource(node)
            r.execute("update nodes set type='A', producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + aggregatorselector + "', aggregatortake=" + str(aggregatortake) + ", aggregatortimefilter='" + aggregatortimefilter + "', aggregatorskip=" + str(aggregatorskip) + ", aggregatorsort='" + aggregatorsort + "', aggregatormethod='" + aggregatormethod + "' where id =" + str(id))
        if node['datasource']['type'] in ['L']:
            cproducers = dict()
            producers = s.expand(aggregatorselector, aggregatorsort, aggregatortake, aggregatorskip)
            r.execute("update nodes set type='L', producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + aggregatorselector + "', aggregatortake=" + str(aggregatortake) + ", aggregatortimefilter='" + aggregatortimefilter + "', aggregatorskip=" + str(aggregatorskip) + ", aggregatorsort='" + aggregatorsort + "', aggregatormethod='" + aggregatormethod + "' where id =" + str(id))
            for p in producers:
                pchilds = getnodesidfromp(r, p['id'])
                for c in pchilds:
                    child = s.getnode(c)
                    if child['datasource']['type'] in ['B','D']:
                        if child['name'] not in cproducers:
                            cproducers[child['name']] = [dict(id=child['id'], path=getpath(s, r, child['id']))]
                        else:
                            cproducers[child['name']].append(dict(id=child['id'], path=getpath(s, r, child['id'])))
            nchilds = [s.getnode(x) for x in getnodesidfromp(r, id)]
            pnames = {x for x in cproducers.keys()}
            nnames = {x['name'] for x in nchilds}
            dids = {x['id'] for x in nchilds if x['name'] not in pnames}
            for e in dids:
                logging.info("Node: " + str(id) + ", Type: " + node['datasource']['type'] + ", deleting obsolete child: '" + str(e) + "' ...")
                s.deletenode(e)
            for n in pnames - nnames:
                logging.info("Node: " + str(id) + ", Type: " + node['datasource']['type'] + ", creating new child: '" + n + "' ...")
                s.createnode(node['id'], n)
            nchilds = [s.getnode(x) for x in getnodesidfromp(r, id)]
            for c in nchilds:
                if 'aggregatormethod' in c['datasource'] and 'aggregatortimefilter' in c['datasource']:
                    if c['datasource']['aggregatormethod'] != aggregatormethod or c['datasource']['aggregatortimefilter'] != aggregatortimefilter:
                        logging.info("Node: " + str(c['id'])+ ", Type: " + c['datasource']['type'] + ", deleting cache if exists ...")
                        s.deletecache(c['id'])
                tpath = [x['path'] for x in cproducers[c['name']]]
                aggregatorselector = '|'.join(tpath)
                r.execute("update nodes set type='A', producers='" + json.dumps(cproducers[c['name']]) + "', aggregated=now(), aggregatorselector='" + aggregatorselector + "', aggregatortake=" + str(aggregatortake) + ", aggregatortimefilter='" + aggregatortimefilter + "', aggregatorskip=" + str(aggregatorskip) + ", aggregatorsort='" + aggregatorsort + "', aggregatormethod='" + aggregatormethod + "' where id =" + str(c['id']))
        del s.cache['nodes'][id]
        node = s.getnode(id)
        s.getsource(node)
        return node

    def linkfathernode(s, fid, tid):
        r = s.nrepo
        fnode = s.getnode(fid)
        tnode = s.getnode(tid)
        fpath = getpath(s, r, fid)
        if fnode['status'] == 'DELETED' or tnode['status'] == 'DELETED':
            s.status.pusherrmessage('A trash cannot be part of a link operation!')
            return tnode
        producers = tnode['datasource']['producers']
        if fid in [producer['id'] for producer in producers]:
            s.status.pusherrmessage(fpath + ': this node is already included in the list of producers!')
            return tnode
        producers.append(dict(path=getpath(s, r, fid), id=fid))
        if 'aggregatorselector' not in tnode['datasource']: r.execute("update nodes set type='L', producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + getpath(s, r, fid) + '$' + "', aggregatortake=1, aggregatortimefilter='.', aggregatorskip=0, aggregatorsort='desc', aggregatormethod='$none' where id =" + str(tid))
        else: r.execute("update nodes set producers='" + json.dumps(producers) + "', aggregated=now(), aggregatorselector='" + tnode['datasource']['aggregatorselector'] + '|' + getpath(s, r, fid) + '$' +"', aggregatortake=" + str(int(tnode['datasource']['aggregatortake']) +  1) + " where id =" + str(tid))
        del s.cache['nodes'][tid]
        tnode = s.getnode(tid)
        return tnode
    
    def applyliveobject(s, id, loname):
        r = s.nrepo
        liveobject = s.getliveobject(loname)
        node = s.getnode(id)
        if node['datasource']['type'] in ['D']: s.deletecache(id)
        s.createcache(id)
        cache = s.readcache(id)
        s.setschema(cache.name)
        extension = liveobject['extension']
        server = liveobject['id']
        options = liveobject['options']
        r.execute('drop server if exists ' + server + ' cascade')
        r.execute('create server ' + server + ' foreign data wrapper ' + extension + " options (" + options + ")")
        r.execute('grant usage on foreign server ' + server + ' to postgres')
        user = liveobject['user']
        password = liveobject['password']
        r.execute('create user mapping for postgres server ' + server + " options (user '" + user + "', password '" + password + "')")
        collections = []
        for t in liveobject['tables']:
            description = liveobject['tables'][t]['description']
            if extension == 'oracle_fdw': request = liveobject['tables'][t]['request']
            if extension == 'postgres_fdw': schema = liveobject['tables'][t]['schema']
            desc = ", ".join(["%(k)s %(v)s" % dict(k=d, v=description[d]) for d in description])
            if extension == 'oracle_fdw': r.execute('create foreign table foreign_' + t + '(' + desc + ') server ' + server + " options (table '(" + request.replace("'", "''").replace('kairos_nodeid_to_be_replaced', str(id)) + ")')")
            if extension == 'postgres_fdw': r.execute('create foreign table foreign_' + t + '(' + desc + ') server ' + server + " options (schema_name '" + schema + "', table_name '" + t + "')")
            collections.append(t)
        s.setschema()
        r.execute("update nodes set type='D', aggregated=now(), liveobject='" + loname + "' where id = " + str(id))
        del s.cache['nodes'][id]
        node = s.getnode(id)
        return node

    def emptytrash(s):
        r = s.nrepo
        rootid = getrootid(r)
        trashid = getnodeidfrompn(r, rootid, 'Trash')
        for rid in getprogeny(r, trashid):
            if rid != trashid:
                s.deletesource(rid)
                s.deletecache(rid)
                r.execute("delete from nodes where id = " + str(rid))
    
    def expand(s, pattern, sort, take, skip):
        r = s.nrepo
        skip=int(skip)
        take=int(take)
        d=dict()
        rootid = getrootid(r)
        rootnode = s.getnode(rootid)
        for i in pattern.split('|'):
            nodes = [rootnode]
            for p in i.split('/')[1:]:
                newnodes = []
                for n in nodes:
                    for e in [s.getnode(x) for x in getnodesidfromp(r, n['id'])]:
                        if re.match(p, e['name']):
                            ds = e['datasource']
                            if e['datasource']['type'] == 'L': e = s.applyaggregator(e['id'], ds['aggregatorselector'], ds['aggregatortake'], ds['aggregatorskip'], ds['aggregatortimefilter'], ds['aggregatorsort'], ds['aggregatormethod'])
                            newnodes.append(e)
                nodes = newnodes
            for n in nodes: d[getpath(s, r, n['id'])] = n['id']
        result = [dict(path=k, id=d[k]) for k in sorted(d.keys())] if sort != 'desc' else [dict(path=k, id=d[k]) for k in sorted(d.keys(), reverse=True)][skip:skip+take]
        return result


    def getsource(s, node, getstream=False):
        if node['datasource']['type'] == 'B':
            if 'collections' not in node['datasource']: 
                source = s.readsource(node['id'], stream=getstream)
                if hasattr(source, 'rid'):
                    node['datasource']['uploaded'] = source.created
                    node['datasource']['collections'] = source.collections
                    if getstream: node['datasource']['stream'] = source.stream
            if 'stream' not in node['datasource'] and getstream:
                source = s.readsource(node['id'], stream=getstream)
                node['datasource']['stream'] = source.stream
        if node['datasource']['type'] in ['A', 'C']:
            if 'collections' not in node['datasource']:
                allparts = s.getallparts(node['id'])
                collections = set()
                for p in allparts:
                    pnode = s.getnode(p)
                    if pnode['datasource']['type'] in ['B', 'D']:
                        s.getsource(pnode)
                        collections = collections.union(set(pnode['datasource']['collections']))
                node['datasource']['collections'] = dict()
                for c in collections: node['datasource']['collections'][c] = dict()
    
    def readsource(s, id, stream=False):
        r = s.nrepo
        if stream: x = r.execute("select id as rid, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created, collections, stream from sources where id = " + str(id))
        else: x = r.execute("select id as rid, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created, collections from sources where id = " + str(id))
        o = Object()
        for rx in x:
            o.rid = rx['rid']
            o.created = rx['created']
            o.collections = json.loads(rx['collections'])
            if stream: o.stream = binascii.a2b_base64(rx['stream'])
        return o
    
    def downloadsource(s, id):
        r = s.nrepo
        node = s.getnode(id)
        s.getsource(node, getstream=True)
        filename = getpath(s, r, id)[1:].replace('/','_') + '.zip'
        return (filename, node['datasource']['stream'])

    def unload(s, id):
        r = s.nrepo
        logging.info("Unloading node: " + str(id) + " ...")
        path = getpath(s, r, id)
        archive = path.replace('/', '_')[1:] + '-unload.zip'
        fname = '/tmp/' + archive
        zip = Arcfile(fname, 'w:zip')
        cut = 10000
        s.buildcollectioncache(id, {'*'})
        node = s.getnode(id)
        s.getsource(node)
        s.getcache(node)
        schema = node['datasource']['cache']['name']
        s.setschema(schema)
        for collection in node['datasource']['collections']:
            logging.info("Unloading collection: " + collection + " ...")
            d = dict(collection=collection, desc=dict(), data=[])
            desc = OrderedDict()
            x = r.execute("select column_name, data_type from information_schema.columns where table_name = '" + collection.lower() + "' and table_schema = '" + schema + "'")
            for row in x.fetchall(): desc[row['column_name']] = row['data_type']
            request = 'select '
            for k in desc:
                if k != 'kairos_nodeid':
                    d['desc'][k] = desc[k]
                    request += k + ', '
            request = request[:-2] + ' from ' + collection
            recordset = 0
            nbrec = 0
            if len(desc) != 0:
                for x in r.execute(request):
                    nbrec += 1
                    res = dict()
                    for k in desc:
                        if k != 'kairos_nodeid': res[k] = x[k]
                    d['data'].append(res)
                    if nbrec == cut:
                        logging.info("Writing file: " + collection + str(recordset) + " ...")
                        zip.write(collection + str(recordset), json.dumps(d, sort_keys=True, indent=4))
                        recordset += 1
                        d['data']=[]
                        nbrec = 0
            if nbrec > 0: 
                logging.info("Writing file: " + collection + str(recordset) + " ...")
                zip.write(collection + str(recordset), json.dumps(d, sort_keys=True, indent=4))
        zip.close()
        logging.info("Unloading node: " + id + ", file is ready to download !")
        return (archive, open(fname, 'rb').read())

    def createcache(s, nid):
        r = s.nrepo
        schname = 'cache_' + str(nid)
        r.execute("create schema " + schname)
        r.execute("insert into caches (id, name, created, queries, collections) values(%s, %s, now(), %s, %s)", (nid, schname, json.dumps(dict()), json.dumps(dict())))
    
    def deletecache(s, nid):
        r = s.nrepo
        logging.info("Node: " + str(nid) + ", deleting cache: cache_" + str(nid) + "...")
        r.execute("delete from caches where id = " + str(nid))
        with suppress(Exception): r.execute("drop schema cache_" + str(nid) + " cascade")

    def getcache(s, node):
        if node['icon'] in ['A', 'B', 'C', 'D']:
            if 'name' not in node['datasource']['cache']:
                cache = s.readcache(node['id'])
                if hasattr(cache, 'rid'):
                    node['datasource']['cache']['collections'] = cache.collections
                    node['datasource']['cache']['queries'] = cache.queries
                    node['datasource']['cache']['name'] = cache.name

    def readcache(s, id):
        r = s.nrepo
        o = Object()
        for rx in r.execute("select id as rid, name, queries, to_char(created, 'YYYY-MM-DD HH24:MI:SS.MS') as created, collections from caches where id = " + str(id)):
            o.rid = rx['rid']
            o.name = rx['name']
            o.queries = json.loads(rx['queries'])
            o.created = rx['created']
            o.collections = json.loads(rx['collections'])
        return o

    def gettree(s, pid):
        r = s.nrepo
        root = True if pid == '0' else False
        if root:
            rootid = getrootid(r)
            root = s.getnode(rootid)
            (icon_file, icon_opened, icon_closed) = ficon(root)
            result = [dict(kids=True, id=root['id'], text='/', userdata=dict(type=ftype(root)), icons=dict(file=icon_file, folder_opened=icon_opened, folder_closed=icon_closed))]
        else:
            children = []
            for nid in getnodesidfromp(r, pid):
                node = s.getnode(nid)
                s.countchildren(node)
                (icon_file, icon_opened, icon_closed) = ficon(node)
                kids = True if node['kids'] > 0 else False
                children.append(dict(kids=kids, id=node['id'], text=node['name'], userdata=dict(type=ftype(node)), icons=dict(file=icon_file, folder_opened=icon_opened, folder_closed=icon_closed)))
            result = [dict(id=pid, items=sorted(children, key=getkey))]
        return result
    
    def getcollections(s, id):
        node = s.getnode(id)
        s.getsource(node)
        data = []
        if node['datasource']['type'] == 'D':
            loname = node['datasource']['liveobject']
            liveobject = s.getliveobject(loname)
            for t in liveobject['tables']: data.append(dict(label=t))
        else:
            for collection in node['datasource']['collections']: data.append(dict(label=collection))
        return data

    def executequery(s, id, qname, limit):
        operations = s.schedulecacheoperations(id, 'query', qname)
        if s.status.errors > 0: return
        s.executecacheoperations(operations)
        if s.status.errors > 0: return
        result = s.queryexecute(id, qname, limit)
        return result

    def queryexecute(s, nid, qid, limit):
        r = s.nrepo
        node = s.getnode(nid)
        ntype = node['datasource']['type']
        logging.info("Node: " + str(nid) + ", Type: " + ntype + ", executing query: '" + qid + "' ...")
        s.getcache(node)
        result = []
        if ntype in ['C', 'L']:
            for producer in node['datasource']['producers']:
                pid = producer['id']
                iresult = s.queryexecute(pid, qid, limit)
                if ntype in ['L']: result = iresult
                else: result.append(iresult)
        else:
            query = s.getquery(qid)
            query = dict(id=qid) if query==None else query
            if 'name' not in node['datasource']['cache']: 
                s.status.pusherrmessage('Cache for node id: ' + str(nid) + " doesn't exist!")
                return
            s.setschema(node['datasource']['cache']['name'])
            table = qid.lower()
            for b in r.execute("select exists(select * from information_schema.tables where table_schema = current_schema() and table_name = '" + table + "') foo"): existstable = b['foo']
            if existstable: 
                if 'filterable' in query and query['filterable']:
                    for x in r.execute("select * from " + table + " where label in (select label from (select label, sum(value) weight from " + table + " group by label order by weight desc limit " + str(limit) + ") as foo)"):
                        result.append(x)
                else:
                    for x in r.execute("select * from " + table):
                        result.append(x)
            else: s.status.pusherrmessage('Table ' + table.upper() + " doesn't exist within schema " + node['datasource']['cache']['name'])
        return result
    
    def displaycollection(s, id, collection):
        s.buildcollectioncache(id, {collection})
        if s.status.errors > 0: return
        result = s.queryexecute(id, collection, 0)
        return result
    
    def exportdatabases(s, nodesdb):
        r = s.grepo
        if len(nodesdb) == 0:
            databases = getdatabases(r)
            nodesdb = [databases[x] for x in databases if 'kairos_user_' in x or 'kairos_group_' in x]
        for db in nodesdb:
            with suppress(Exception): shutil.rmtree('/export/' + db)
            os.mkdir('/export/' + db)
            os.chmod('/export/' + db, 0o777)
            ag = subprocess.run(['su', '-', 'postgres', '-c', 'pg_dump -F c -f /export/' + db + '/database.dump ' + db], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if  ag.returncode: s.status.pusherrmessage("Unable to export database: " + db + " for an uknown reason!")
    
    def importdatabases(s, nodesdb):
        r = s.grepo
        if len(nodesdb) == 0:
            for d in os.listdir('/export'):
                wdir = '/export/' + d
                if 'kairos_' in d and os.path.isdir(wdir): nodesdb.append(d)
        for db in nodesdb:
            r.execute("UPDATE pg_database SET datallowconn = 'false' WHERE datname = '" + db +"'")
            r.execute("SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '" + db + "'")
            ag = subprocess.run(['su', '-', 'postgres', '-c', 'psql -c "drop database ' + db + '"'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if  ag.returncode:
                s.status.pusherrmessage("Unable to drop database: " + db + " during import!")
                continue
            ag = subprocess.run(['su', '-', 'postgres', '-c', 'psql -c "create database ' + db + '"'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if  ag.returncode:
                s.status.pusherrmessage("Unable to create database: " + db + " during import!")
                continue
            ag = subprocess.run(['su', '-', 'postgres', '-c', 'pg_restore -d ' + db + ' /export/' + db + '/database.dump'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if  ag.returncode:
                s.status.pusherrmessage("Error during import of database: " + db)

    def clearprogenycaches(s, id):
        r = s.nrepo
        for nid in getprogeny(r, id): s.deletecache(nid)

    def buildprogenycaches(s, id):
        r = s.nrepo
        for nid in getprogeny(r, id): s.buildcollectioncache(nid , {'*'})

    def buildcollectioncache(s, id, collections):
        node = s.getnode(id)
        ntype = node['datasource']['type']
        if ntype in ['N', 'L', 'C']: return
        s.getsource(node)

        if '*' in collections: collections = {k for k in node['datasource']['collections']}
        operations = s.schedulecacheoperations(id, 'buildcollectioncache', collections)
        if s.status.errors > 0: return
        s.executecacheoperations(operations)

    def dropcollectioncache(s, id, collections):
        node = s.getnode(id)
        s.getcache(node)
        operations = s.schedulecacheoperations(id, 'dropcollectioncache', collections)
        if s.status.errors > 0: return
        s.executecacheoperations(operations)

    def buildquerycache(s, nid, qid):
        r = s.nrepo
        node = s.getnode(nid)
        query = s.getquery(qid)
        if query == None: return
        s.getcache(node)
        ntype = node['datasource']['type']
        logging.info("Node: " + str(nid) + ", Type: " + ntype + ", checking query cache: '" + qid + "' ...")
        if ntype in ['A', 'B', 'D']:
            todo = True if qid not in node['datasource']['cache']['queries'] else False
            todo = True if "nocache" in query and query["nocache"] else todo            
            for collection in query['collections']:
                for part in node['datasource']['cache']['collections'][collection]:
                    todo = True if qid in node['datasource']['cache']['queries'] and node['datasource']['cache']['queries'][qid] < node['datasource']['cache']['collections'][collection][part] else todo
            if todo:
                s.setschema(node['datasource']['cache']['name'])
                table = qid
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", removing old query cache: '" + qid + "' ...")
                r.execute("drop table if exists " + table)
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", building new query cache: '" + qid + "' ...")
                if 'userfunctions' in query:
                    for ufn in query['userfunctions']:
                        s.setschema()
                        uf = s.getfunction(ufn)
                        s.setschema(node['datasource']['cache']['name'])
                        r.execute(uf["function"])
                try: r.execute("create table " + table + " as select * from (" + query['request'] + ") as foo")
                except: 
                    s.status.pusherrmessage('Check if data exists for collections: ' + str(query['collections']))
                    return
                node['datasource']['cache']['queries'][qid] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", updating cache with query info: '" + qid + "' ...")
                s.setschema()
                r.execute("update caches set queries = '" + json.dumps(node['datasource']['cache']['queries']) + "' where id = " + str(nid))
            else: logging.info("Node: " + str(nid) + ", Type: " + ntype + ", nothing to do for query cache: '" + qid + "' ...")
    
    def getallparts (s, id, v=None):
        d = dict()
        node = s.getnode(id)
        s.getcache(node)
        d[id] = v
        if node['datasource']['type'] in ['A', 'C']:
            producers = node['datasource']['producers']
            for p in producers:
                d[p['id']] = id
                dp = s.getallparts(p['id'], id)
                for x in dp: d[x] = dp[x]
        return d
    
    def schedulecacheoperations(s, id, type, name, recursive=False):
        operations = []
        r = s.nrepo
        node = s.getnode(id)
        ntype = node['datasource']['type']

        if type == 'buildcollectioncache':
            collections = name
            oldparts = s.getallparts(id)
            ds = node['datasource']
            if ntype in ['A']: node = s.applyaggregator(id, ds['aggregatorselector'], ds['aggregatortake'], ds['aggregatorskip'], ds['aggregatortimefilter'], ds['aggregatorsort'], ds['aggregatormethod'])
            newparts = s.getallparts(id)
            for p in set(oldparts) - set(newparts): 
                operations.append(dict(operation='removepart', nid=oldparts[p], part=p, collections=collections))
            ranks = dict()
            for p in set(newparts):
                dp = depthp(newparts, p)
                if dp not in ranks: ranks[dp] = [p]
                else: ranks[dp].append(p)
            for r in sorted(set(ranks), reverse=True):
                for p in ranks[r]:
                    node = s.getnode(p)
                    if node['datasource']['type'] in ['A']:
                        for x in [e['id'] for e in node['datasource']['producers']]:
                            if p not in set(newparts) - set(oldparts):
                                operations.append(dict(operation='checkpart', nid=p, part=x, collections=collections))
                                operations.append(dict(operation='removepart', nid=p, part=x, collections=None))
                                operations.append(dict(operation='createpartA', nid=p, part=x, collections=None))
                            else:
                                operations.append(dict(operation='createpartA', nid=p, part=x, collections=collections))
                    if node['datasource']['type'] in ['B', 'D']:
                        operations.append(dict(operation='checkpart', nid=p, part=p, collections=collections))
                        operations.append(dict(operation='removepart', nid=p, part=p, collections=None))
                        operations.append(dict(operation='createpart' + node['datasource']['type'], nid=p, part=p, collections=None))

        if type == 'dropcollectioncache':
            collections = name
            operations.append(dict(operation='removetable', nid=id, part=id, collections=collections))

        if type == 'query':
            query = s.getquery(name)
            if query == None: return
            collections = set(query['collections'])
            operations = s.schedulecacheoperations(id, 'buildcollectioncache', collections, recursive=True)
            operations.append(dict(operation='buildquerycache', nid=id, qid=name))

        if type == 'chart':
            chart = s.getchart(name)
            if chart == None: return
            queries = set()
            queries.add(chart['reftime'])
            for y in chart['yaxis']:
                for r in y['renderers']:
                    for d in r['datasets']:
                        queries.add(d['query'])
            collections = set()
            for q in queries:
                query = s.getquery(q)
                if query == None:
                    s.status.pusherrmessage('Query "' + str(q) + '"' + " doesn't exist!")
                    return
                if 'nocache' in query and query['nocache']: s.nocache = True
                for e in query['collections']: collections.add(e)
            operations = s.schedulecacheoperations(id, 'buildcollectioncache', collections, recursive=True)
            for q in queries:
                if ntype in 'C':
                    for p in node['datasource']['producers']:
                        operations.append(dict(operation='buildquerycache', nid=p['id'], qid=q))
                else: operations.append(dict(operation='buildquerycache', nid=id, qid=q))

        if not recursive:
            logging.info('Sheduled operations:')
            for operation in operations:
                if operation['operation'] in ['checkpart', 'removepart', 'removetable', 'createpartA', 'createpartB', 'createpartD']: logging.info('Node: ' + str(operation['nid']) + ', Operation: ' + operation['operation'] + ', Partition: ' + str(operation['part']) + ', Collections: ' + str(operation['collections']))
                if operation['operation'] in ['buildquerycache']: logging.info('Node: ' + str(operation['nid']) + ', Operation: ' + operation['operation'] + ', Query: ' + str(operation['qid']))
        return operations
    
    def executecacheoperations(s, operations):
        for operation in operations:
            if operation['operation'] == 'checkpart': s.checkpart(operation['nid'], operation['part'], operation['collections'])
            if operation['operation'] == 'removepart': s.removepart(operation['nid'], operation['part'], operation['collections'])
            if operation['operation'] == 'removetable': s.removetable(operation['nid'], operation['part'], operation['collections'])
            if operation['operation'] == 'createpartA': s.createpartA(operation['nid'], operation['part'], operation['collections'])
            if operation['operation'] == 'createpartB': s.createpartB(operation['nid'], operation['part'], operation['collections'])
            if operation['operation'] == 'createpartD': s.createpartD(operation['nid'], operation['part'], operation['collections'])
            if operation['operation'] == 'buildquerycache': s.buildquerycache(operation['nid'], operation['qid'])
            if s.status.errors > 0: 
                logging.error('Breaking scheduled operations!')
                break

    def checkpart(s, nid, part, collections):
        node = s.getnode(nid)
        s.getcache(node)
        nodecache = node['datasource']['cache']
        if 'name' not in nodecache: s.createcache(nid)
        s.getcache(node)
        cachecol = node['datasource']['cache']['collections']
        ntype = node['datasource']['type']
        s.removecollections = set()
        s.createcollections = set()
        pnode = s.getnode(part)
        s.getcache(pnode)
        pcachecol = pnode['datasource']['cache']['collections']

        if ntype in ['A']:
            for collection in collections:
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", checking partition cache: " + str(part) + " for collection: '" + collection + "' ...")
                todo = False
                if collection not in pnode['datasource']['collections']: continue
                datepart = cachecol[collection][str(part)] if collection in cachecol and str(part) in cachecol[collection] else None
                if collection not in pcachecol: continue
                datesource = max([pcachecol[collection][x]  for x in  pcachecol[collection]])
                todo = True if datepart == None else todo
                todo = True if datepart != None and datepart < datesource else todo
                if todo: 
                    s.removecollections.add(collection)
                    s.createcollections.add(collection)

        if ntype in ['B']:
            s.getsource(node)
            for collection in collections:
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", checking collection cache: '" + collection + "' ...")
                if collection not in node['datasource']['collections']: continue
                analyzername = node['datasource']['collections'][collection]['analyzer']
                analyzer = s.getanalyzer(analyzername)
                datepart = cachecol[collection][str(nid)] if collection in cachecol and str(nid) in cachecol[collection] else None
                todo = False
                todo = True if datepart == None else todo
                todo = True if datepart != None and node['datasource']['uploaded'] > datepart else todo
                todo = True if datepart != None and analyzer['created'] > datepart else todo
                if todo: 
                    s.removecollections.add(collection)
                    s.createcollections.add(collection)

        if ntype in ['D']:
            liveobject = s.getliveobject(node['datasource']['liveobject'])
            try: timeout = liveobject['retention']
            except: timeout = 60
            for collection in collections:
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", checking collection cache: '" + collection + "' ...")
                todo = False
                datepart = cachecol[collection][str(nid)] if collection in cachecol and str(nid) in cachecol[collection] else None
                todo = True if datepart == None else todo
                todo = True if datepart != None and (datetime.now() - datetime.strptime(datepart, '%Y-%m-%d %H:%M:%S.%f')).seconds > timeout else todo
                if todo: 
                    s.removecollections.add(collection)
                    s.createcollections.add(collection)

    def removetable(s, nid, part, collections):
        r = s.nrepo
        node = s.getnode(nid)
        s.getcache(node)
        ntype = node['datasource']['type']
        if collections == None: collections = s.removecollections
        if 'name' in node['datasource']['cache']:
            s.setschema(node['datasource']['cache']['name'])
            for collection in collections:
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", removing table: " + str(nid) + " for collection: '" + collection + "' ...")
                r.execute("drop table if exists " + collection)
        if 'collections' in node['datasource']['cache']:
            for collection in collections:
                if collection in node['datasource']['cache']['collections']: del node['datasource']['cache']['collections'][collection]
            s.setschema()
            r.execute("update caches set collections = '" + json.dumps(node['datasource']['cache']['collections']) + "' where id = " + str(nid))

    def removepart(s, nid, part, collections):
        r = s.nrepo
        node = s.getnode(nid)
        s.getcache(node)
        ntype = node['datasource']['type']
        if collections == None: collections = s.removecollections
        if 'name' in node['datasource']['cache']:
            s.setschema(node['datasource']['cache']['name'])
            for collection in collections:
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", removing partition: " + str(part) + " for collection: '" + collection + "' ...")
                if ntype in ['A']:
                    partition = collection + '_' + str(part)
                    r.execute("drop table if exists " + partition)
                else:
                    r.execute("drop table if exists " + collection)
        if 'collections' in node['datasource']['cache']:
            for collection in collections:
                if collection in node['datasource']['cache']['collections']:
                    if part in node['datasource']['cache']['collections'][collection]: del node['datasource']['cache']['collections'][collection][part]
            s.setschema()
            r.execute("update caches set collections = '" + json.dumps(node['datasource']['cache']['collections']) + "' where id = " + str(nid))

    def createpartA(s, nid, part, collections):
        if collections == None: collections = s.createcollections
        if len(collections) == 0: return
        r = s.nrepo
        nodesdb = s.nodesdb
        node = s.getnode(nid)
        s.getcache(node)
        ntype = node['datasource']['type']
        logging.info("Node: " + str(nid) + ", Type: " + ntype + ", building new partition cache: " + str(part) + " for collections '" + str(collections) + "' ...")
        s.setschema()
        function = s.getaggregator(node['datasource']['aggregatormethod'])
        meet = s.getfunction('meet')
        x = r.execute("select distinct table_name from information_schema.columns where table_schema='" + node['datasource']['cache']['name'] + "'")
        schdesc = [row['table_name'] for row in x.fetchall()]
        pnode = s.getnode(part)
        s.getcache(pnode)
        inschname = pnode['datasource']['cache']['name']
        x = r.execute("select distinct table_name from information_schema.columns where table_schema='" + inschname + "'")
        inschdesc = [row['table_name'] for row in x.fetchall()]
        queues = dict()
        tabledesc = dict()
        queues['ERROR_QUEUE'] = multiprocessing.Queue()
        s.setschema(node['datasource']['cache']['name'])
        for collection in collections:
            if collection.lower() not in inschdesc: continue
            if collection.lower() not in schdesc:
                request = "select column_name, data_type from information_schema.columns where table_name = '" + collection.lower() + "' and table_schema = '" +  pnode['datasource']['cache']['name'] + "'"
                coldesc = ', '.join([row['column_name'] + ' ' + row['data_type'] for row in r.execute(request)])
                request = "create table " + collection.lower() + " ("  + coldesc + ") partition by list(kairos_nodeid)"
                r.execute(request)
            pname = collection + '_' + str(part)
            request = "create table " + pname.lower() + " partition of " + collection.lower() + " for values in ('" + str(part) + "')"
            r.execute(request)
            tabledesc[collection] = OrderedDict()
            x = r.execute("select column_name, data_type from information_schema.columns where table_name = '" + collection.lower() + "' and table_schema = '" +  node['datasource']['cache']['name'] + "'")
            for row in x.fetchall(): tabledesc[collection][row['column_name']] = row['data_type']
            queues[collection] = multiprocessing.Queue()

        def write_to_queue(collection):
            try:
                logging.info("Node: " + str(nid) + ", Type: " + ntype + ", building partition: " + str(part) + " for collection: '" + collection + "' ...")
                pnode = s.getnode(part)
                s.getcache(pnode)
                inschname = pnode['datasource']['cache']['name']
                lgby = [k for k in tabledesc[collection] if tabledesc[collection][k] == 'text']
                lavg = [k for k in tabledesc[collection] if tabledesc[collection][k] == 'real']
                lsum = [k for k in tabledesc[collection] if tabledesc[collection][k] in ['integer', 'bigint']]
                selector = ', '.join(tabledesc[collection].keys()) + ', ' + str(part) + ' as kairos_nodeid'
                where = " where meet(timestamp,'" + node['datasource']['aggregatortimefilter'] + "') or timestamp='00000000000000000'" if 'timestamp' in lgby else ' '
                subrequest = "select * from " + inschname + "." + collection.lower() + where
                request = "select "
                for x in lgby: request = request + function["name"] + '(timestamp) as timestamp, ' if x == "timestamp" else request + x + ', '
                for x in lavg: request += 'sum(coalesce(' + x + ', 0)) as ' + x + ', '
                for x in lsum: request += 'sum(' + x + ') as ' + x + ', '
                request = request[:-2] + ' from (' + subrequest + ') as foo group by '
                for x in lgby: request = request + function["name"] + '(timestamp), ' if x == 'timestamp' else request + x + ', '
                request = request[:-2]
                workrequest = 'select ' + function["name"] + '(timestamp) as timestamp, kairos_nodeid, count(*) num from (select distinct timestamp, kairos_nodeid from ' + inschname  + '.' + collection + where +') as foo group by ' + function["name"] + '(timestamp), kairos_nodeid'
                divisor = dict()
                context = Context(nodesdb=nodesdb)
                context.setschema(node['datasource']['cache']['name'])
                context.nrepo.execute(function["function"])
                context.nrepo.execute(meet["function"])
                if 'timestamp' in lgby:  
                    for x in context.nrepo.execute(workrequest).fetchall(): divisor[x['timestamp'] + x ['kairos_nodeid']] = x['num']
                if len(lgby) > 0:
                    for row in context.nrepo.execute(request).fetchall():
                        record = ''
                        if 'timestamp' in lgby:
                            for x in lavg: row[x] = row[x] * 1.0 / divisor[row['timestamp'] + row['kairos_nodeid']]
                        for k in tabledesc[collection].keys(): record += '\\N\t' if row[k] == None else str(row[k] if k != 'kairos_nodeid' else part).replace('\n','\\n').replace('\t','\\t').replace('\r', '').replace('\\', '\\\\') + '\t'
                        record = record[:-1] + '\n'
                        queues[collection].put(record)
                context.free()
            except: s.status.pusherrmessage(str(sys.exc_info()[1]))

        def read_from_queue(collection):
            context = Context(nodesdb=nodesdb)
            context.setschema(node['datasource']['cache']['name'])
            buffer = io.StringIO()
            bufferempty = True
            counter = 0
            partname = collection + '_' + str(part)
            try: limit = int(os.environ['BUFFER'])
            except: limit = 10000
            globalcounter = 0
            while True:
                try:
                    record = queues[collection].get()
                    if record == 'KAIROS_DONE': break
                    bufferempty = False
                    counter += 1
                    logging.debug('Buffer content at line: ' + str(counter) + ', record: ' + str(record))
                    buffer.write(record)
                    if counter == limit:
                        buffer.seek(0)
                        logging.info("Writing " + str(counter) + " records to partition: " + partname + "...")
                        context.nrepo.copy(buffer, partname, tuple(tabledesc[collection].keys()))
                        buffer = io.StringIO()
                        globalcounter += counter
                        counter = 0
                        bufferempty = True
                except:
                    s.status.pusherrmessage(str(sys.exc_info()[1]))
                    queues['ERROR_QUEUE'].put(collection)
                    buffer = io.StringIO()
                    counter = 0
                    bufferempty = True
            if not bufferempty:
                try:
                    buffer.seek(0)
                    logging.info("Writing " + str(counter) + " records to partition: " + partname + "...")
                    context.nrepo.copy(buffer, partname, tuple(tabledesc[collection].keys()))
                    globalcounter += counter
                except:
                    s.status.pusherrmessage(str(sys.exc_info()[1]))
                    queues['ERROR_QUEUE'].put(collection)
            logging.info("Partition: " + partname + ": " + str(globalcounter) + " records have been written! ")
            context.free()
        
        limit = multiprocessing.cpu_count()

        try:
            for collection in queues:
                if collection == 'ERROR_QUEUE': continue
                pr = Parallel(read_from_queue, workers = 1)
                pw = Parallel(write_to_queue, workers = 1)
                pr.push(collection)
                pw.push(collection)
                pw.join()
                queues[collection].put('KAIROS_DONE')
                pr.join()
                if not queues['ERROR_QUEUE'].empty():
                    s.status.pusherrmessage('At least one error found during collection cache building! See KAIROS.LOG for more information!')
                else:
                    if collection not in node['datasource']['cache']['collections']: node['datasource']['cache']['collections'][collection] = dict()
                    node['datasource']['cache']['collections'][collection][part] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    queues[collection].close()
                    queues[collection].join_thread()
            queues['ERROR_QUEUE'].close()
            queues['ERROR_QUEUE'].join_thread()
            logging.info("Node: " + str(nid) + ", Type: A, updating cache with collections info: '" + str(collections) + "' ...")
            s.setschema()
            r.execute("update caches set collections = '" + json.dumps(node['datasource']['cache']['collections']) + "' where id = " + str(nid))

        except: s.status.pusherrmessage(str(sys.exc_info()[1]))

    def createpartB(s, nid, part, collections):
        if collections == None: collections = s.createcollections
        if len(collections) == 0: return

        r = s.nrepo
        s.setschema()
        node = s.getnode(nid)
        s.getsource(node, getstream=True)
        queues = dict()
        writeheader = dict()
        readheader = dict()
        members = dict()
        queues['ERROR_QUEUE'] = multiprocessing.Queue()

        for collection in collections:
            queues[collection] = multiprocessing.Queue()
            writeheader[collection] = True
            readheader[collection] = True
            for member in node['datasource']['collections'][collection]['members']: members[member] = s.getanalyzer( node['datasource']['collections'][collection]['analyzer'])
        
        logging.info("Node: " + str(nid) + ", Type: B, building collections caches for collections: '" + str(collections) + "' ...")

        def write_to_queue(col, d, v, n):
            logging.debug('Writing to queue the following collection:' + col)
            if writeheader[col]:
                record = json.dumps(dict(header='KAIROS_START', desc=d)) 
                queues[col].put(record)
                writeheader[col] = False
            v = v if type(v) == type([]) else [v]
            for e in v:
                record = ''
                e['kairos_nodeid'] = nid
                for k in sorted(e.keys()): record += '\\N\t' if e[k] == '' else str(e[k]).replace('\n','\\n').replace('\t','\\t').replace('\r', '').replace('\\', '\\\\') + '\t'
                record = record[:-1] + '\n'
                queues[col].put(record)

        def read_from_queue(col):
            buffer = io.StringIO()
            bufferempty = True
            counter = 0
            limit = 10000
            globalcounter = 0
            context = Context(nodesdb=s.nodesdb)
            context.setschema(node['datasource']['cache']['name'])

            while True:
                try:
                    record = queues[col].get()
                    if record == 'KAIROS_DONE': break
                    with suppress(Exception): record = json.loads(record)
                    if type(record) == type(dict()) and 'header' in record and record['header'] == 'KAIROS_START':
                        if readheader[col]:
                            record['desc']['kairos_nodeid'] = 'text'
                            request = 'create table ' + col + '('
                            description= sorted(record['desc'].keys())
                            for k in description: request += k + ' ' + record['desc'][k] +  ', '
                            request = request[:-2] + ')'
                            context.nrepo.execute(request)
                            readheader[col] = False
                    else:
                        bufferempty = False
                        counter += 1
                        logging.debug('Buffer content at line: ' + str(counter) + ', record: ' + str(record))
                        buffer.write(record)
                        if counter == limit:
                            buffer.seek(0)
                            logging.info("Writing " + str(counter) + " records to collection: " + col + "...")
                            context.nrepo.copy(buffer, col, tuple(description))
                            buffer = io.StringIO()
                            globalcounter += counter
                            counter = 0
                            bufferempty = True
                except:
                    s.status.pusherrmessage(str(sys.exc_info()[1]))
                    queues['ERROR_QUEUE'].put(col)
                    buffer = io.StringIO()
                    counter = 0
                    bufferempty = True
            if not bufferempty:
                try:
                    buffer.seek(0)
                    logging.info("Writing " + str(counter) + " records to collection: " + col + "...")
                    context.nrepo.copy(buffer, col, tuple(description))
                    globalcounter += counter
                    logging.info("Collection: " + col + ": " + str(globalcounter) + " records have been written! ")
                except:
                    s.status.pusherrmessage(str(sys.exc_info()[1]))
                    queues['ERROR_QUEUE'].put(col)
            context.free()
                            
        thezip = zipfile.ZipFile(io.BytesIO(node['datasource']['stream']))
        logging.info('Analyzing archive attached to node ' + str(nid) + '...')
        listen = write_to_queue

        def do(member):
            if member in members:
                analyzer = Analyzer(members[member], set(collections), listen, nid)
                logging.info('Analyzing member: ' + member + '...')
                status = analyzer.analyze(thezip.read(member), member)
                if status.error: queues['ERROR_QUEUE'].put(member)
                return None

        limit = multiprocessing.cpu_count()

        try:
            pr = Parallel(read_from_queue, workers=len(collections))
            for collection in collections: pr.push(collection)
            pw = Parallel(do, workers = limit)
            for e in thezip.namelist(): pw.push(e)
            pw.join()
            thezip.close()
            for collection in collections: queues[collection].put('KAIROS_DONE')
            pr.join()
            if not queues['ERROR_QUEUE'].empty(): s.status.pusherrmessage('At least one error found during collection cache building! See KAIROS.LOG for more information!')
            else:
                for collection in collections:
                    if collection not in node['datasource']['cache']['collections']: node['datasource']['cache']['collections'][collection] = dict()
                    node['datasource']['cache']['collections'][collection][nid] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            for collection in collections: 
                queues[collection].close()
                queues[collection].join_thread()
            queues['ERROR_QUEUE'].close()
            queues['ERROR_QUEUE'].join_thread()
            logging.info("Node: " + str(nid) + ", Type: B, updating cache with collections info: '" + str(collections) + "' ...")
            s.setschema()
            r.execute("update caches set collections = '" + json.dumps(node['datasource']['cache']['collections']) + "' where id = " + str(nid))

        except: s.status.pusherrmessage(str(sys.exc_info()[1]))

    def createpartD(s, nid, part, collections):
        if collections == None: collections = s.createcollections
        r = s.nrepo
        node = s.getnode(nid)
        s.getcache(node)
        ntype = node['datasource']['type']
        s.setschema(node['datasource']['cache']['name'])
        for collection in collections:
            logging.info("Node: " + str(nid) + ", Type: " + ntype + ", building new collection cache: '" + collection + "' ...")
            r.execute("create table " + collection + " as select '" + str(nid) + "'::text as kairos_nodeid, * from foreign_" + collection)
            if collection not in node['datasource']['cache']['collections']: node['datasource']['cache']['collections'][collection] = dict()
            node['datasource']['cache']['collections'][collection][nid] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logging.info("Node: " + str(nid) + ", Type: D, updating cache with collections info: '" + str(collections) + "' ...")
        s.setschema()
        r.execute("update caches set collections = '" + json.dumps(node['datasource']['cache']['collections']) + "' where id = " + str(nid))

    def getchartcache(s, id, timeout):
        repository = s.nrepo

        class ChartCache:

            def __init__(s):
                s.timeout = timeout
                s.repository = repository
                s.cachename = 'cache_' + str(id)
                s.repository.setschema(s.cachename)
                x = s.repository.execute("select distinct table_name from information_schema.columns where table_schema='" + s.cachename + "'")
                if len([row['table_name'] for row in x.fetchall() if row['table_name'] == 'chartcache']) == 0:
                    s.repository.execute("create table chartcache(k text primary key, v text)")

            def get(s, key):
                s.repository.setschema(s.cachename)
                ckey = hashlib.md5(json.dumps(key).encode('utf-8')).hexdigest()
                x = s.repository.execute("select v from chartcache where k = '" + ckey + "'")
                lvalues = [row['v'] for row in x.fetchall()]
                if len(lvalues) == 0: return None
                jsonvalueout = lvalues[0]
                valueout = json.loads(jsonvalueout)
                now = int(datetime.now().strftime('%s'))
                timestamp = int(valueout['timestamp'])
                if now - timestamp > s.timeout: return None
                else: return valueout['value']

            def set(s, key, valuein):
                s.repository.setschema(s.cachename)
                ckey = hashlib.md5(json.dumps(key).encode('utf-8')).hexdigest()
                x = s.repository.execute("select v from chartcache where k = '" + ckey + "'")
                lvalues = [row['v'] for row in x.fetchall()]
                valueout = json.dumps(dict(timestamp=datetime.now().strftime('%s'), value=valuein))
                if len(lvalues) == 0:
                    s.repository.execute("insert into chartcache (k, v) values ('" + ckey + "', '" + valueout + "')")
                else:
                    s.repository.execute("update chartcache set v = '" + valueout + "' where k ='" + ckey + "'")
        
        return ChartCache()

    def runchart(s, id, chart, width, height, limit, colors, plotorientation, template):
        r = s.nrepo
        node = s.getnode(id)
        s.getcache(node)
        nodecache = node['datasource']['cache']
        if 'name' not in nodecache: s.createcache(id)
        s.getcache(node)
        timeout = 3600
        if node['datasource']['type'] == 'D': 
            liveobject = s.getliveobject(node['datasource']['liveobject'])
            try: timeout = liveobject['retention']
            except: timeout = 60
        chartcache = s.getchartcache(id, timeout)
        ckey = dict(chart=chart, limit=limit, colors=colors, plotorientation=plotorientation, template=template)
        jsonchart = chartcache.get(ckey)
        if jsonchart:
            chartobj = json.loads(jsonchart)
            fig = chartobj['figure']
            rows = chartobj['rows']
        else:
            s.setschema()
            template = s.gettemplate(template)
            colors = s.getcolors(colors)['colors']
            operations = s.schedulecacheoperations(id, 'chart', chart)
            if s.status.errors > 0: return
            s.executecacheoperations(operations)
            if s.status.errors > 0: return
            co=dict(rows=1, cols=1, isarray=False, shared_yaxes=False, shared_xaxes=False, layoutoptions=dict(), xaxis=dict(), yaxis=dict(), alreadyright=dict(), alreadyleft=dict(), traces=dict(), pies=dict())
            chart = s.getchart(chart)
            result = s.queryexecute(id, chart['reftime'], limit)
            if s.status.errors > 0: return
            reftimedf = gettimestampdf(result, co, plotorientation)
            co['shared_yaxes'] = True if plotorientation == 'horizontal' else False
            co['shared_xaxes'] = True if plotorientation == 'vertical' else False
            getnewaxis(co, reftimedf, template, axistype='x', index=0)
            if co['shared_yaxes']:
                i = 1
                for e in reftimedf[1:]: 
                    getnewaxis(co, reftimedf, template, axistype='x', index=i)
                    i += 1
                co['cols'] = i
            if co['shared_xaxes']: co['rows'] = len(reftimedf)
            fig = plotly.subplots.make_subplots(rows=co['rows'], cols=co['cols'], shared_yaxes=co['shared_yaxes'], shared_xaxes=co['shared_xaxes'], subplot_titles=tuple(getchartproducers(node)))
            for e in template['layout']: co['layoutoptions'][e] = template['layout'][e].copy() if type(template['layout'][e]) == type(dict()) else template['layout'][e]
            co['layoutoptions']['title']['text'] = chart['title']
            co['layoutoptions']['width'] = width
            co['numyaxis'] = 0
            events = dict()
            for y in chart['yaxis']:
                co['numyaxis'] += 1
                idxy = []
                if co['shared_yaxes']: 
                    idxy.append(getnewaxis(co, reftimedf, template, axistype='y', options=y, index=0))
                else:
                    for i in range(co['rows']): idxy.append(getnewaxis(co, reftimedf, template, axistype='y', options=y, index=i))
                for r in y['renderers']:
                    co['pielabels'] = dict()
                    co['pievalues'] = dict()
                    co['piecolors'] = dict()
                    for d in r['datasets']:
                        alreadyinlegend = dict()
                        result = s.queryexecute(id, d['query'], limit)
                        if s.status.errors > 0: return
                        datasetdf = gettimestampdf(result, co, plotorientation)
                        labeldf = [x.groupby('label')[['value']].sum() for x in datasetdf]
                        ascending = 0
                        i = 0
                        for e in labeldf:
                            if i not in co['pielabels']: co['pielabels'][i] = []
                            if i not in co['pievalues']: co['pievalues'][i] = []
                            if i not in co['piecolors']: co['piecolors'][i] = []
                            for label, row in e.sort_values(by=['value'], ascending=ascending).iterrows():
                                events[label] = dict(info=None, onclick=None)
                                if 'onclick' in d and d['onclick']: events[label]['onclick'] = d['onclick']
                                if 'info' in d and d['info']: events[label]['info'] = d['info']
                                if r['type'] == 'P':
                                    co['pielabels'][i].append(label)
                                    co['pievalues'][i].append(row['value'])
                                    co['piecolors'][i].append(getcolor(colors, label))
                                else:
                                    paddeddatasetdf = paddeddf(reftimedf[i], datasetdf[i][datasetdf[i]['label'] == label])
                                    settrace(co, r, dataframe=paddeddatasetdf, label=label, yaxisindex=idxy[i] if co['shared_xaxes'] else idxy[0], index=i, alreadyinlegend=alreadyinlegend, groupname=getcolor(colors, str(r)), plotorientation=plotorientation, colors=colors)
                            i += 1
                if r['type'] == 'P':
                    for i in co['pielabels']:
                        co['pies'][i]=dict(trace=plotly.graph_objs.Pie(labels=co['pielabels'][i], values=co['pievalues'][i], hoverinfo='label+percent', textinfo='none', marker=dict(colors=co['piecolors'][i], line=dict(color='#000000', width=2))), row=1, col=i)
            if len(co['pies']) > 0:
                fig['layout'].update(**co['layoutoptions'])
                fig = json.loads(json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder))
                for i in co['pies']:
                    fig['data'].append(json.loads(json.dumps(co['pies'][i]['trace'], cls=plotly.utils.PlotlyJSONEncoder)))
            else:
                for it in co['pies']: fig.append_trace(co['pies'][it]['trace'], co['pies'][it]['row'], co['pies'][it]['col'])
                for it in co['traces']: fig.append_trace(co['traces'][it]['trace'], co['traces'][it]['row'], co['traces'][it]['col'])
                for it in co['traces']: fig['data'][it].update(xaxis=co['xaxis'][co['traces'][it]['xaxis']]['smallname'], yaxis=co['yaxis'][co['traces'][it]['yaxis']]['smallname'])
                for iy in co['yaxis']: setattr(fig['layout'], co['yaxis'][iy]['name'], plotly.graph_objs.layout.YAxis())
                for ix in co['xaxis']: setattr(fig['layout'], co['xaxis'][ix]['name'], plotly.graph_objs.layout.XAxis())
                fig['layout'].update(**co['layoutoptions'])
                for iy in co['yaxis']: fig['layout'][co['yaxis'][iy]['name']].update(**co['yaxis'][iy]['options'])
                for ix in co['xaxis']: fig['layout'][co['xaxis'][ix]['name']].update(**co['xaxis'][ix]['options'])
            rows = co['rows']
            chartobj = dict(figure=fig, events=events, rows=rows)
            cvalue = json.dumps(chartobj, cls=plotly.utils.PlotlyJSONEncoder)
            if not s.nocache: chartcache.set(ckey, cvalue)
            chartobj = json.loads(cvalue)
            fig = chartobj['figure']
        fig['layout']['width'] = width
        if 'titlefont' not in fig['layout']: fig['layout']['titlefont'] = dict()
        fig['layout']['titlefont']['size'] = getfontsize(width, binf=1000, bsup=2000, vinf=12, vsup=18)
        if 'annotations' in fig['layout']:
            for a in fig['layout']['annotations']:
                a['font']['size'] = getfontsize(width, binf=1000, bsup=2000, vinf=10, vsup=14)
        if 'legend' not in fig['layout']: fig['layout']['legend'] = dict()
        if 'font' not in fig['layout']['legend']: fig['layout']['legend']['font'] = dict()
        fig['layout']['legend']['font']['size'] = getfontsize(width, binf=500, bsup=2000, vinf=8, vsup=12)
        fig['layout']['legend']['x'] = 1.02
        numleftyaxis = 0
        numrightyaxis = 0
        numxaxis = 0
        figtype = None
        fig['config'] = dict(showSendToCloud=True, editable=True, scrollZoom=True)
        for e in fig['data']:
            if e['type'] == 'pie': figtype = 'pie'
        for e in list(fig['layout']):
            if 'yaxis' in e:
                if 'side' not in fig['layout'][e]: del fig['layout'][e]
                else:
                    if fig['layout'][e]['side'] == 'left': numleftyaxis += 1
                    if fig['layout'][e]['side'] == 'right': numrightyaxis += 1
            if 'xaxis' in e: numxaxis += 1
        if figtype == 'pie':
            numleftyaxis = 0
            numrightyaxis = 0
            for e in list(fig['layout']):
                if 'xaxis' in e or 'yaxis' in e: del fig['layout'][e]
        for e in fig['layout']:
            if 'yaxis' in e or 'xaxis' in e:
                if 'titlefont' not in fig['layout'][e]: fig['layout'][e]['titlefont'] = dict()
                if 'tickfont' not in fig['layout'][e]: fig['layout'][e]['tickfont'] = dict()
                fig['layout'][e]['tickfont']['size'] = getfontsize(width, binf=500, bsup=2000, vinf=8, vsup=12)
                fig['layout'][e]['titlefont']['size'] = getfontsize(width, binf=500, bsup=2000, vinf=10, vsup=14)
            if 'yaxis' in e:
                fig['layout'][e]['position'] = getyposition(fig['layout'][e], width, numleftyaxis=numleftyaxis, rows=rows)
        for e in fig['layout']:
            if 'xaxis' in e:
                if 'xaxis' == e: index = 0
                else: index = int(e[-1]) - 1
                fig['layout'][e]['domain'] = getdomain(width, index=index, numleftyaxis=numleftyaxis, numrightyaxis=numrightyaxis, numxaxis=numxaxis, rows=rows)
        if figtype == 'pie':
            index = 0
            for e in fig['data']:
                if 'domain' not in e: e['domain'] = dict()
                e['domain']['x'] = getdomain(width, index=index, numleftyaxis=numleftyaxis, numrightyaxis=numrightyaxis, numxaxis=numxaxis, rows=rows)
                index += 1       
        if 'annotations' in fig['layout']:
                index = 0
                for a in list(fig['layout']['annotations']):
                    if plotorientation == 'horizontal': a['x'] = getaposition(width, index=index, numleftyaxis=numleftyaxis, numrightyaxis=numrightyaxis, numxaxis=numxaxis)
                    else: a['y'] = getaposition(width, index=index, numleftyaxis=numleftyaxis, numrightyaxis=numrightyaxis, numxaxis=numxaxis, rows=rows)
                    index += 1
        logging.debug('Generated figure: ' + json.dumps(chartobj))
        return chartobj