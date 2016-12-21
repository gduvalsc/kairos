class UserObject(dict):
    def __init__(s):
        object = {
            "type": "liveobject",
            "id": "JAYDEBEAPI",
            "tables": {
                "ORAHAS": {
                    "parameters": [
                            "oracle.jdbc.driver.OracleDriver",
                            "jdbc:oracle:thin:system/manager@oracle12c:1521/orcl",
                            "select sample_id, to_char(sample_time,'yyyymmddhh24missff') timestamp, is_awr_sample, session_id, session_serial# session_serial, session_type, flags, user_id, sql_id, is_sqlid_current, sql_child_number, sql_opcode, sql_opname, force_matching_signature, top_level_sql_id, top_level_sql_opcode, sql_adaptive_plan_resolved, sql_full_plan_hash_value, sql_plan_hash_value, sql_plan_line_id, sql_plan_operation, sql_plan_options, sql_exec_id, sql_exec_start, plsql_entry_object_id, plsql_entry_subprogram_id, plsql_object_id, plsql_subprogram_id, qc_instance_id, qc_session_id, qc_session_serial# qc_session_serial, px_flags, event, event_id, event# eventnum, seq# seq, p1text, p1, p2text, p2, p3text, p3, wait_class, wait_class_id, wait_time, session_state, time_waited, blocking_session_status, blocking_session, blocking_session_serial# blocking_session_serial, blocking_inst_id, blocking_hangchain_info, current_obj# current_obj, current_file# current_file, current_block# current_block, current_row# current_row, top_level_call# top_level_call, top_level_call_name, consumer_group_id, xid,  remote_instance# remote_instance, time_model, in_connection_mgmt, in_parse, in_hard_parse, in_sql_execution, in_plsql_execution, in_plsql_rpc, in_plsql_compilation, in_java_execution, in_bind, in_cursor_close, in_sequence_load, in_inmemory_query, in_inmemory_populate, in_inmemory_prepopulate, in_inmemory_repopulate, in_inmemory_trepopulate, capture_overhead, replay_overhead, is_captured, is_replayed, service_hash, program, module, action, client_id, machine, port, ecid, dbreplay_file_id, dbreplay_call_counter, tm_delta_time, tm_delta_cpu_time, tm_delta_db_time, delta_time, delta_read_io_requests, delta_write_io_requests, delta_read_io_bytes, delta_write_io_bytes, delta_interconnect_io_bytes, delta_read_mem_bytes, pga_allocated, temp_space_allocated, con_dbid, con_id, dbop_name, dbop_exec_id from v$active_session_history",
                            {"sample_id": "text", "session_id": "text", "session_serial": "text", "flags": "text", "user_id": "text", "sql_child_number": "text", "sql_opcode": "text", "force_matching_signature": "text", "top_level_sql_opcode": "text", "sql_adaptive_plan_resolved": "text", "sql_full_plan_hash_value": "text", "sql_plan_hash_value": "text", "sql_plan_line_id": "text", "sql_exec_id": "text", "plsql_entry_object_id": "text", "plsql_entry_subprogram_id": "text", "plsql_object_id": "text", "plsql_subprogram_id": "text", "qc_instance_id": "text", "qc_session_id": "text", "qc_session_serial": "text", "px_flags": "text", "event_id": "text", "eventnum": "text", "seq": "text", "p1": "text", "p2": "text", "p3": "text", "wait_class_id": "text", "blocking_session": "text", "blocking_session_serial": "text", "blocking_inst_id": "text", "current_obj": "text", "current_file": "text", "current_block": "text", "current_row": "text", "top_level_call": "text", "consumer_group_id": "text", "remote_instance": "text", "time_model": "text", "service_hash": "text", "port": "text", "dbreplay_file_id": "text", "con_dbid": "text", "con_id": "text", "dbop_exec_id": "text"}
                        ],
                    "method": UserObject.OracleBridge
                }
            },
        } 

        super(UserObject, s).__init__(**object)

    class OracleBridge:
        def Connect(self, db, modulename, dbname, tablename, *args):
            import jaydebeapi, base64, json, logging, sys
            [driver, url, sql, jsontr, nodeid] = [base64.b64decode(p.encode()).decode() for p in args]
            typesredefined = json.loads(jsontr)
            self.nodeid = nodeid
            self.odbh = jaydebeapi.connect(driver, url)
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
                ctype = 'text' if c[1] == jaydebeapi.STRING else None
                ctype = 'real' if c[1] == jaydebeapi.DECIMAL else ctype
                ctype = 'real' if c[1] == jaydebeapi.NUMBER else ctype
                ctype = 'text' if c[1] == jaydebeapi.DATETIME else ctype
                ctype = 'text' if c[1] == jaydebeapi.BINARY else ctype
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
            return self.schema, self.OracleBridgeTable(self.columns, self)

        def Create(self, db, modulename, dbname, tablename, *args):
            if not hasattr(self, "schema"): return self.Connect(db, modulename, dbname, tablename, *args) 
            else: return self.schema, self.OracleBridgeTable(self.columns, self)
    
        class OracleBridgeTable:
            def __init__(self, columns, data):
                self.bridge = data
            def BestIndex(self, *args):
                return None
            def Open(self):
                return self.OracleBridgeCursor(self)
            def Destroy(self):
                request = "drop table " + self.bridge.realtable
                cursor = self.bridge.db.cursor()
                self.bridge.logging.debug(cursor)
                cursor.execute(request)
                cursor.close()
            
            class OracleBridgeCursor:
                from datetime import datetime
                def __init__(self, table):
                    self.printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
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
                    #value = list(filter(lambda x: x in self.printable, str(raw))) if self.table.bridge.types[col] == 'text' else raw
                    value = str(raw) if self.table.bridge.types[col] == 'text' else raw
                    return value
                def Rowid(self):
                    return self.currow[0]
                def Next(self):
                    self.currow = self.table.bridge.cursor.fetchone()
                    self.eof = True if self.currow == None else False
                    self.rownum += 1
                def Close(self):
                    pass
