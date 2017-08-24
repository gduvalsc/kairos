class UserObject(dict):
    CONNECTSTRING = "jdbc:postgresql://postgres/kairos?user=kairos"
    DEFS = {
        "defday": "defday as (select current_date minday, current_date + 1 maxday)",
        "pscpu": "pscpu as (select * from vpsutil_cpu_times)",
        "psvmem": "psvmem as (select * from vpsutil_virt_memory)",
        "pssmem": "pssmem as (select * from vpsutil_swap_memory)",
        "psio": "psio as (select * from vpsutil_disk_io_counters)",
        "psproc": "psproc as (select * from vpsutil_processes)",
        "statd": "statd as (select * from vkpg_stat_database)",
        "stata": "stata as (select * from vkpg_stat_activity)",
    }
    def __init__(s):
        object = {
            "type": "liveobject",
            "id": "POSTGRES_PY4JDBC_BRIDGE",
            "tables": {
                "vpsutil_cpu_times": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(defday)s, %(pscpu)s select timestamp, nbcpus, usr, sys, nice, idle, iowait, irq, softirq, steal, guest from pscpu, defday where snap >= minday and snap <= maxday" % UserObject.DEFS,
                            {"timestamp":"text", "nbcpus": "real", "usr": "real", "sys": "real", "nice": "real", "idle": "real", "iowait": "real", "irq": "real", "softirq": "real", "steal": "real", "guest": "real"}
                        ],
                    "method": UserObject.Bridge
                },
                "vpsutil_virt_memory": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(defday)s, %(psvmem)s select timestamp, total, available, percent, used, free, active, inactive, buffers, cached from psvmem, defday where snap >= minday and snap <= maxday" % UserObject.DEFS,
                            {"timestamp":"text", "total": "real", "available": "real", "percent": "real", "used": "real", "free": "real", "active": "real", "inactive": "real", "buffers": "real", "cached": "real"}
                        ],
                    "method": UserObject.Bridge
                },
                "vpsutil_swap_memory": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(defday)s, %(pssmem)s select timestamp, total, used, free, percent, sin, sout from pssmem, defday where snap >= minday and snap <= maxday" % UserObject.DEFS,
                            {"timestamp":"text", "total": "real", "used": "real", "free": "real", "percent": "real", "sin": "real", "sout": "real"}
                        ],
                    "method": UserObject.Bridge
                },
                "vpsutil_disk_io_counters": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(defday)s, %(psio)s select timestamp, disk, read_count, write_count, read_bytes, write_bytes, read_time, write_time from psio, defday where snap >= minday and snap <= maxday" % UserObject.DEFS,
                             {"timestamp":"text", "disk": "text", "read_count": "real", "write_count": "real", "read_bytes": "real", "write_bytes": "real", "read_time": "real", "write_time": "real"}
                        ],
                    "method": UserObject.Bridge
                },
                "vpsutil_processes": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(defday)s, %(psproc)s select timestamp, pid, create_time, pname, cmdline, usr, sys, status, num_threads, rss, vms, shared, texts, lib, datas, dirty from psproc, defday where snap >= minday and snap <= maxday" % UserObject.DEFS,
                            {"timestamp":"text", "pid":"text", "create_time":"text", "pname":"text", "cmdline":"text", "usr":"real", "sys":"real", "status": "text", "num_threads":"real", "rss":"real", "vms":"real", "shared":"real", "texts":"real", "lib":"real", "datas":"real", "dirty":"real"}
                        ],
                    "method": UserObject.Bridge
                },
                "vkpg_stat_database": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(defday)s, %(statd)s select timestamp, datname, datid, stats_reset, numbackends, blk_read_time, blk_write_time, blks_hit, blks_read, conflicts, deadlocks, temp_bytes, temp_files, tup_deleted, tup_fetched, tup_inserted, tup_returned, tup_updated, xact_commit, xact_rollback from statd, defday where snap >= minday and snap <= maxday" % UserObject.DEFS,
                            {"timestamp":"text", "snap":"text", "datid":"text", "datname":"text", "numbackends":"real", "xact_commit":"real", "xact_rollback":"real", "blks_read":"real", "blks_hit":"real", "tup_returned":"real", "tup_fetched":"real", "tup_inserted":"real", "tup_updated":"real", "tup_deleted":"real", "conflicts":"real", "temp_files":"real", "temp_bytes":"real", "deadlocks":"real", "blk_read_time":"real", "blk_write_time":"real", "stats_reset":"text"}
                        ],
                    "method": UserObject.Bridge
                },
                "vkpg_stat_activity": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(defday)s, %(stata)s select timestamp, snap_frequency, application_name, backend_start, backend_xid, backend_xmin, client_addr, client_hostname, client_port, datid, datname, pid, hash, query, query_start, state, state_change, usename, usesysid, wait_event, wait_event_type, xact_start from stata, defday where snap >= minday and snap <= maxday" % UserObject.DEFS,
                            {"timestamp":"text", "snap_frequency": "text", "application_name": "text", "backend_start": "text", "backend_xid": "text", "backend_xmin": "text", "client_addr": "text", "client_hostname": "text", "client_port": "text", "datid": "text", "datname": "text", "pid": "text", "hash": "text", "query": "text", "query_start": "text", "state": "text", "state_change": "text", "usename": "text", "usesysid": "text", "wait_event": "text", "wait_event_type": "text", "xact_start": "text"}
                        ],
                    "method": UserObject.Bridge
                },
            },
        } 

        super(UserObject, s).__init__(**object)

    class Bridge:
        def Connect(self, db, modulename, dbname, tablename, *args):
            import py4jdbc, base64, json, logging, sys
            from py4jdbc.java_sql_types import java_sql_types
            alphatype = lambda x: [y for y in java_sql_types if y[1] == x][0][0]
            [url, sql, jsontr, nodeid] = [base64.b64decode(p.encode()).decode() for p in args]
            typesredefined = json.loads(jsontr)
            self.nodeid = nodeid
            self.odbh = py4jdbc.connect(url)
            self.db = db
            self.tablename = tablename
            self.sql = sql
            realtable = tablename.lower().replace('virtual_','')
            self.realtable = realtable
            oc = self.odbh.cursor()
            request = "select * from (" + sql + ") as req limit 1"
            logging.debug(request)
            oc.execute(request)
            columns = []
            types = []
            desc = []
            for c in oc.description:
                columns.append(c[0].lower())
                ctype = 'text' if alphatype(c[1]) == 'VARCHAR' else None
                ctype = 'int' if alphatype(c[1]) == 'BIGINT' else ctype
                ctype = 'int' if alphatype(c[1]) == 'INTEGER' else ctype
                ctype = 'text' if alphatype(c[1]) == 'OTHER' else ctype
                ctype = 'text' if alphatype(c[1]) == 'TIMESTAMP' else ctype
                ctype = 'text' if alphatype(c[1]) == 'BIT' else ctype
                ctype = typesredefined[c[0].lower()] if c[0].lower() in typesredefined else ctype
                desc.append(c[0].lower() + " " + ctype)
                types.append(ctype)
            columns.append('kairos_nodeid');
            desc.append('kairos_nodeid text')
            types.append('text')
            columns.append('kairos_count');
            desc.append('kairos_count int')
            types.append('int')
            self.columns = columns
            self.types = types
            self.schema = "create table " + realtable + "(" + ','.join([str(x) for x in desc]) + ")"
            cursor = db.cursor()
            request = "create table if not exists " + realtable + "(" + ','.join([str(x) for x in desc]) + ")"
            logging.debug(request)
            cursor.execute(request)
            cursor.close()
            self.cursor = self.odbh.cursor()
            logging.debug(sql)
            self.cursor.execute(sql)
            self.logging = logging
            return self.schema, self.BridgeTable(self.columns, self)

        def Create(self, db, modulename, dbname, tablename, *args):
            if not hasattr(self, "schema"):
                x = self.Connect(db, modulename, dbname, tablename, *args)
                self.odbh.close()
                return x 
            else:
                return self.schema, self.BridgeTable(self.columns, self)
    
        class BridgeTable:
            def __init__(self, columns, data):
                self.bridge = data
            def BestIndex(self, *args):
                return None
            def Open(self):
                return self.BridgeCursor(self)
            def Destroy(self):
                request = "drop table " + self.bridge.realtable
                cursor = self.bridge.db.cursor()
                self.bridge.logging.debug(cursor)
                cursor.execute(request)
                cursor.close()
            
            class BridgeCursor:
                from datetime import datetime
                def __init__(self, table):
                    self.eof = False
                    self.currow = None
                    self.table = table
                def Filter(self, *args):
                    self.currow = self.table.bridge.cursor.fetchone()
                    self.rownum = 0
                    self.rowlen = len(self.currow)
                def Eof(self):
                    return self.eof
                def Column(self, col):
                    if col == self.rowlen: raw = str(self.table.bridge.nodeid)
                    elif col == self.rowlen+1: raw = 1
                    else: raw = self.currow[col]
                    value = str(raw) if self.table.bridge.types[col] == 'text' else raw
                    value = float(raw) if self.table.bridge.types[col] == 'real' else value
                    value = int(raw) if self.table.bridge.types[col] == 'int' else value
                    return value
                def Rowid(self):
                    return self.currow[0]
                def Next(self):
                    self.currow = self.table.bridge.cursor.fetchone()
                    self.eof = True if self.currow == None else False
                    self.rownum += 1
                def Close(self):
                    self.table.bridge.odbh.close()
