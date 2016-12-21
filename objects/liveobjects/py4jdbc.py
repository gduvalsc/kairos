class UserObject(dict):
    def __init__(s):
        object = {
            "type": "liveobject",
            "id": "PY4JDBC",
            "tables": {
                "SESSION": {
                    "parameters": [
                            "jdbc:oracle:thin:system/manager@oracle12c:1521/orcl",
                            "select substr(to_char(cast(sysdate as timestamp),'YYYYMMDDHH24MISSFF'),1,17) timestamp, saddr, sid, serial# as serial, audsid, paddr, username, command, taddr, lockwait, status, server, schemaname, osuser, process, machine, port, terminal, program, type, sql_address, sql_hash_value, sql_id, sql_child_number, sql_exec_start, sql_exec_id, module, action, client_info, fixed_table_sequence, row_wait_obj# as  row_wait_obj, row_wait_file# as row_wait_file, row_wait_block# as row_wait_block, row_wait_row# as row_wait_row, logon_time, last_call_et, resource_consumer_group, client_identifier, blocking_session_status, blocking_instance, blocking_session, seq# as seq, event, p1text, p1, p1raw, p2text, p2, p2raw, p3text, p3, p3raw, wait_class, wait_time, seconds_in_wait, state, wait_time_micro, service_name, external_name from v$session",
                            {"sid": "text", "serial": "text", "audsid": "text", "osuser": "text", "process": "text", "command": "text", "sql_hash_value": "text", "port": "text", "sql_child_number": "text", "sql_exec_id": "text", "row_wait_obj": "text", "row_wait_file": "text", "row_wait_block": "text", "row_wait_row": "text", "fixed_table_sequence": "text", "client_identifier": "text", "blocking_instance": "text", "blocking_session": "text", "p1": "text", "p2": "text", "p3": "text", "seq": "text"}
                        ],
                    "method": UserObject.Bridge
                }
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
            request = "select * from (" + sql + ") where rownum < 1"
            logging.debug(request)
            oc.execute(request)
            columns = []
            types = []
            desc = []
            for c in oc.description:
                columns.append(c[0].lower())
                ctype = 'text' if alphatype(c[1]) == 'VARCHAR' else None
                ctype = 'real' if alphatype(c[1]) == 'NUMERIC' else ctype
                ctype = 'text' if alphatype(c[1]) == 'TIMESTAMP' else ctype
                ctype = 'text' if alphatype(c[1]) == 'VARBINARY' else ctype
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
            if not hasattr(self, "schema"): return self.Connect(db, modulename, dbname, tablename, *args) 
            else: return self.schema, self.BridgeTable(self.columns, self)
    
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
                    pass