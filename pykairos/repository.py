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
#
import logging, psycopg2, psycopg2.extensions, psycopg2.extras, os, json
from datetime import datetime

class Repository:

    def __init__(s, db=None):
        s.database = db
        postgresstr = "host='localhost' user='postgres' dbname='" + db + "'" if db != None else "host='localhost' user='postgres'"
        s.loglevel = logging.getLogger().getEffectiveLevel()
        s.tracefile = '/var/log/kairos/postgres_' + str(os.getpid()) + '.sql'
        s.trace('\n\n-- '+ str(datetime.now()))
        if db: s.trace('psql -d ' + db)
        else: s.trace('psql')
        s.trace('')
        s.postgres = psycopg2.connect(postgresstr)
        s.cursor =  s.postgres.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        s.setschema()
        s.postgres.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    
    def setschema(s, schema=None):
        s.schema = 'public' if schema == None else schema
        s.execute('set search_path=' + s.schema)

    def trace(s, stmt):
        if s.loglevel == logging.TRACE:
            ftrace = open(s.tracefile, 'a')
            print(stmt, file=ftrace)
            ftrace.close()  

    def execute(s,*req):
        logging.debug('Database: ' + str(s.database) + ', schema: ' + s.schema + ', request: ' + req[0])
        s.trace(req[0] + ';')
        s.cursor.execute(*req)
        return s.cursor

    def executep(s,req,prm):
        logging.debug('Database: ' + str(s.database) + ', schema: ' + s.schema + ', request: ' + req)
        c = s.postgres.cursor()
        c.execute(req, prm)
        return c

    def copy(s, buffer, table, description):
        logging.debug('Database: ' + str(s.database) + ', schema: ' + s.schema + ', copy into: ' + table + " using: " + str(description))
        s.trace('COPY ' + table + " " + json.dumps(description).replace('[','(').replace(']',')') + ' FROM stdin;')
        s.trace(buffer.getvalue()[:-1])
        s.trace('\\.')
        c = s.postgres.cursor()
        c.copy_from(buffer, table, columns=description)

    def exists(s, table):
        result = False
        x = s.execute("select 1 from information_schema.tables where table_schema = '" + s.schema + "' and table_name = '" + table + "'")
        for rx in x.fetchall(): result = True
        return result

    def disconnect(s):
        s.trace('\\q')
        s.cursor.close()
        s.postgres.close()
