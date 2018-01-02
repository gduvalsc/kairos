class UserObject(dict):
    
# Oracle foreign data wrapper

# create extension oracle_fdw;
# CREATE SERVER orcl FOREIGN DATA WRAPPER oracle_fdw  OPTIONS (dbserver '//orcl/orcl');
# GRANT USAGE ON FOREIGN SERVER orcl TO agensgraph;
# CREATE USER MAPPING FOR agensgraph SERVER orcl OPTIONS (user 'system', password 'manager');
# CREATE FOREIGN TABLE sysdate (sysdate timestamp) SERVER orcl OPTIONS (table '(select sysdate from dual)');

    CONNECTSTRING = "system/manager@oracle12c/orcl"
    DEFS = {
        "iname": "iname as (select 'orcl' name from dual)",
        "defday": "defday as (select null minday, null maxday from dual)",
        "interval": "interval as (select to_char(nvl(to_date(minday,'YYYY-MM-DD'),sysdate),'YYYY-MM-DD') minday, to_char(nvl(to_date(maxday,'YYYY-MM-DD'),sysdate+1),'YYYY-MM-DD') maxday from defday)",
        "dbid": "dbid as (select * from (select dbid from dba_hist_database_instance, iname where instance_name = iname.name order by startup_time desc) where rownum = 1)",
        "dbname": "dbname as (select * from (select db_name name from dba_hist_database_instance x, iname, dbid where x.instance_name = iname.name and x.dbid=dbid.dbid order by startup_time desc) where rownum=1)",
        "dbname": "dbname as (select * from (select db_name name from dba_hist_database_instance x, iname, dbid where x.instance_name = iname.name and x.dbid=dbid.dbid order by startup_time desc) where rownum=1)",
        "inum": "inum as (select * from (select to_char(instance_number) id from dba_hist_database_instance x, iname, dbid where x.instance_name = iname.name and x.dbid=dbid.dbid order by startup_time desc) where rownum=1)",
        "alldeltas": "alldeltas as (select startup_time, begin_interval_time, end_interval_time, first_value(snap_id) over (order by END_INTERVAL_TIME asc rows between 1 preceding and current row) prev_snap_id, snap_id from dba_hist_snapshot x, dbid, inum where x.dbid=dbid.dbid and x.instance_number = inum.id)",
        "snapshots": "snapshots as (select to_char(end_interval_time, 'YYYYMMDDHH24MISSFF') timestamp, startup_time, begin_interval_time, end_interval_time, cast(86400 * (cast(end_interval_time as date) - cast(begin_interval_time as date)) as integer) duration, prev_snap_id, snap_id, dbid.dbid dbid, dbname.name dbname, inum.id inum from alldeltas, dbid, inum, dbname, interval where end_interval_time >= to_date(interval.minday, 'YYYY-MM-DD') and end_interval_time <= to_date(interval.maxday, 'YYYY-MM-DD') and prev_snap_id != snap_id)",
        "segname": "segname as (select x.dbid, ts# ts, obj# obj, dataobj# dataobj, owner, object_name oname, subobject_name sname, object_type otype, tablespace_name tablespace, partition_type ptype from dbid, dba_hist_seg_stat_obj x where dbid.dbid = x.dbid)",
        "svstats": "svstats as (select timestamp, x2.service_name service, x2.stat_name stat, (x2.value - x1.value) / duration value from snapshots s, dba_hist_service_stat x1, dba_hist_service_stat x2 where s.prev_snap_id = x1.snap_id and s.snap_id = x2.snap_id and s.dbid = x1.dbid and s.dbid = x2.dbid and s.inum = x1.instance_number and s.inum = x2.instance_number and x1.stat_id = x2.stat_id and x1.service_name_hash = x2.service_name_hash and x1.value != x2.value and x2.stat_name in ('physical reads', 'session logical reads', 'DB time', 'DB CPU'))",
        "swstats": "swstats as (select timestamp, x2.service_name service, x2.wait_class wclass, (x2.time_waited - x1.time_waited) / 100 / duration time, (x2.total_waits - x1.total_waits) / duration count from snapshots s, dba_hist_service_wait_class x1, dba_hist_service_wait_class x2 where s.prev_snap_id = x1.snap_id and s.snap_id = x2.snap_id and s.dbid = x1.dbid and s.dbid = x2.dbid and s.inum = x1.instance_number and s.inum = x2.instance_number and x1.wait_class_id = x2.wait_class_id and x1.service_name_hash = x2.service_name_hash and x1.total_waits != x2.total_waits)",
        "dboraawr": "dboraawr as (select timestamp from snapshots)",
        "dborafil": "dborafil as (select timestamp, (x2.phyrds - x1.phyrds) / duration reads, (x2.phyblkrd - x1.phyblkrd) / (x2.phyrds - x1.phyrds) blocksperread, (x2.readtim - x1.readtim) / 100 / duration readtime, (x2.phywrts - x1.phywrts) / duration writes, (x2.wait_count - x1.wait_count) / duration busy, (x2.time - x1.time) / duration busytime, x2.tsname tablespace, x2.filename " + '"file"' + " from snapshots s, dba_hist_filestatxs x1, dba_hist_filestatxs x2 where s.prev_snap_id = x1.snap_id and s.snap_id = x2.snap_id and s.dbid = x1.dbid and s.dbid = x2.dbid and s.inum = x1.instance_number and s.inum = x2.instance_number and x1.file# = x2.file# and x1.ts# = x2.ts# and x1.phyrds != x2.phyrds)",
        "dborainfo": "dborainfo as (select timestamp, startup_time startup from snapshots)",
        "dboramisc": "dboramisc as (select timestamp, duration elapsed, duration avgelapsed, 'AWR_11G' type, value sessions from snapshots s, dba_hist_sysstat x where x.stat_name = 'logons current' and x.snap_id = s.snap_id and s.inum = x.instance_number and s.dbid = x.dbid)",
        "dboraoss": "dboraoss as (select timestamp, stat_name statistic, value from snapshots s, dba_hist_osstat x where s.snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborareq": "dborareq as (select sql_id sqlid, sql_text request, '' module from dbid, dba_hist_sqltext x where dbid.dbid = x.dbid)",
        "dborasga": "dborasga as (select timestamp, pool, name, x.bytes / 1048576 " + '"size"' + " from snapshots s, dba_hist_sgastat x where s.snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborasgbbw": "dborasgbbw as (select timestamp, x.buffer_busy_waits_delta / duration waits, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgcbr": "dborasgcbr as (select timestamp, x.gc_cu_blocks_received_delta / duration blocks, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgcrbr": "dborasgcrbr as (select timestamp, x.gc_cr_blocks_received_delta / duration blocks, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgdbc": "dborasgdbc as (select timestamp, x.db_block_changes_delta / duration changes, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgdpr": "dborasgdpr as (select timestamp, x.physical_reads_direct_delta / duration reads, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgdpw": "dborasgdpw as (select timestamp, x.physical_writes_direct_delta / duration writes, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasggcbb": "dborasggcbb as (select timestamp, x.gc_buffer_busy_delta / duration waits, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgiw": "dborasgiw as (select timestamp, x.itl_waits_delta / duration waits, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasglr": "dborasglr as (select timestamp, x.logical_reads_delta / duration gets, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgor": "dborasgor as (select timestamp, x.optimized_physical_reads_delta / duration reads, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgpr": "dborasgpr as (select timestamp, x.physical_reads_delta / duration reads, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgprr": "dborasgprr as (select timestamp, x.physical_read_requests_delta / duration reads, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgpw": "dborasgpw as (select timestamp, x.physical_writes_delta / duration writes, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgpwr": "dborasgpwr as (select timestamp, x.physical_write_requests_delta / duration writes, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgrlw": "dborasgrlw as (select timestamp, x.row_lock_waits_delta / duration waits, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgts": "dborasgts as (select timestamp, x.table_scans_delta / duration scans, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasgur": "dborasgur as (select timestamp, (x.physical_reads_delta - x.optimized_physical_reads_delta) / duration reads, y.owner owner, y.oname object, y.otype objtype, y.tablespace tablespace, y.sname subobject from snapshots s, segname y, dba_hist_seg_stat x where s.snap_id = x.snap_id and s.dbid = x.dbid and x.dbid = y.dbid and s.inum = x.instance_number and x.ts# = y.ts and x.obj# = y.obj and x.dataobj# = y.dataobj)",
        "dborasqc": "dborasqc as (select timestamp, x.buffer_gets_delta / duration gets, x.cpu_time_delta / 1000000 / duration cpu, x.executions_delta / duration execs, 0 percent, x.elapsed_time_delta / duration elapsed, x.sql_id sqlid from snapshots s, dba_hist_sqlstat x where s.prev_snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborasqe": "dborasqe as (select timestamp, x.disk_reads_delta / duration reads, x.cpu_time_delta / 1000000 / duration cpu, x.executions_delta / duration execs, 0 percent, x.elapsed_time_delta / duration elapsed, x.sql_id sqlid from snapshots s, dba_hist_sqlstat x where s.prev_snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborasqg": "dborasqg as (select timestamp, x.buffer_gets_delta / duration gets, x.cpu_time_delta / 1000000 / duration cpu, x.executions_delta / duration execs, 0 percent, x.elapsed_time_delta / duration elapsed, x.sql_id sqlid from snapshots s, dba_hist_sqlstat x where s.prev_snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborasqm": "dborasqm as (select timestamp, x.sharable_mem sharedmem, x.executions_delta / duration execs, 0 percent, x.sql_id sqlid from snapshots s, dba_hist_sqlstat x where s.prev_snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborasqp": "dborasqp as (select timestamp, x.parse_calls_delta / duration parses, x.executions_delta / duration execs, 0 percent, x.sql_id sqlid from snapshots s, dba_hist_sqlstat x where s.prev_snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborasqr": "dborasqr as (select timestamp, x.disk_reads_delta / duration reads, x.cpu_time_delta / 1000000 / duration cpu, x.executions_delta / duration execs, 0 percent, x.elapsed_time_delta / duration elapsed, x.sql_id sqlid from snapshots s, dba_hist_sqlstat x where s.prev_snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborasqv": "dborasqv as (select timestamp, x.version_count versioncount, x.executions_delta / duration execs, 0 percent, x.sql_id sqlid from snapshots s, dba_hist_sqlstat x where s.prev_snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborasqw": "dborasqw as (select timestamp, x.clwait_delta / 1000000 / duration clusterwait, x.cpu_time_delta / 1000000 / duration cpu, x.executions_delta / duration execs, x.elapsed_time_delta / duration elapsed, x.sql_id sqlid from snapshots s, dba_hist_sqlstat x where s.prev_snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number)",
        "dborasqx": "dborasqx as (select timestamp, x.cpu_time_delta / x.executions_delta / 1000000 cpuperexec, x.elapsed_time_delta / x.executions_delta / 1000000 elapsedperexec, x.executions_delta / duration execs, x.rows_processed_delta / duration " + '"rows"' + ", x.sql_id sqlid from snapshots s, dba_hist_sqlstat x where s.prev_snap_id = x.snap_id and s.dbid = x.dbid and s.inum = x.instance_number and x.executions_delta != 0)",
        "dborasrv": "dborasrv as (select timestamp, service, decode(stat, 'physical reads',  value, 0) reads, decode(stat, 'session logical reads',  value, 0) gets, decode(stat, 'DB time',  value / 1000000, 0) dbtime, decode(stat, 'DB CPU',  value / 1000000 , 0) cpu from svstats)",
        "dborasta": "dborasta as (select timestamp, (x2.value - x1.value) / duration value, x2.stat_name statistic from snapshots s, dba_hist_sysstat x1, dba_hist_sysstat x2 where s.prev_snap_id = x1.snap_id and s.snap_id = x2.snap_id and s.dbid = x1.dbid and s.dbid = x2.dbid and s.inum = x1.instance_number and s.inum = x2.instance_number and x1.stat_id = x2.stat_id and x1.value != x2.value)",
        "dborasvw": "dborasvw as (select timestamp, service, decode(wclass, 'Network',  count, 0) netwaits, decode(wclass, 'Network',  time, 0) netwaitt, decode(wclass, 'User I/O',  count, 0) uiowaits, decode(wclass, 'User I/O',  time, 0) uiowaitt, decode(wclass, 'Concurrency',  count, 0) conwaits, decode(wclass, 'Concurrency',  time, 0) conwaitt, decode(wclass, 'Administrative',  count, 0) admwaits, decode(wclass, 'Administrative',  time, 0) admwaitt from swstats where wclass in ('Network', 'User I/O', 'Administrative', 'Concurrency'))",
        "dboratbs": "dboratbs as (select timestamp, (x2.phyrds - x1.phyrds) / duration reads, (x2.phyblkrd - x1.phyblkrd) / (x2.phyrds - x1.phyrds) blocksperread, (x2.readtim - x1.readtim) / 100 / duration readtime, (x2.phywrts - x1.phywrts) / duration writes, (x2.wait_count - x1.wait_count) / duration busy, (x2.time - x1.time) / duration busytime, x2.tsname tablespace from snapshots s, dba_hist_filestatxs x1, dba_hist_filestatxs x2 where s.prev_snap_id = x1.snap_id and s.snap_id = x2.snap_id and s.dbid = x1.dbid and s.dbid = x2.dbid and s.inum = x1.instance_number and s.inum = x2.instance_number and x1.file# = x2.file# and x1.ts# = x2.ts# and x1.phyrds != x2.phyrds)",
        "dboratms": "dboratms as (select timestamp, (x2.value - x1.value) / 1000000 / duration time, x2.stat_name statistic from snapshots s, dba_hist_sys_time_model x1, dba_hist_sys_time_model x2 where s.prev_snap_id = x1.snap_id and s.snap_id = x2.snap_id and s.dbid = x1.dbid and s.dbid = x2.dbid and s.inum = x1.instance_number and s.inum = x2.instance_number and x1.stat_id = x2.stat_id and x1.value != x2.value)",
        "dboraweb": "dboraweb as (select timestamp, (x2.time_waited_micro - x2.time_waited_micro_fg - x1.time_waited_micro + x1.time_waited_micro_fg) / 1000000 / duration time, (x2.total_waits - x2.total_waits_fg - x1.total_waits + x1.total_waits_fg) / duration count, (x2.total_timeouts - x2.total_timeouts_fg - x1.total_timeouts + x1.total_timeouts_fg) / duration timeouts, x2.event_name event from snapshots s, dba_hist_system_event x1, dba_hist_system_event x2 where s.prev_snap_id = x1.snap_id and s.snap_id = x2.snap_id and s.dbid = x1.dbid and s.dbid = x2.dbid and s.inum = x1.instance_number and s.inum = x2.instance_number and x1.event_id = x2.event_id and x1.total_waits - x1.total_waits_fg != x2.total_waits - x2.total_waits_fg)",
        "dborawec": "dborawec as (select timestamp, (x2.time_waited_micro_fg - x1.time_waited_micro_fg) / 1000000 / duration time, (x2.total_waits_fg - x1.total_waits_fg) / duration count, (x2.total_timeouts_fg - x1.total_timeouts_fg) / duration timeouts, x2.wait_class eclass from snapshots s, dba_hist_system_event x1, dba_hist_system_event x2 where s.prev_snap_id = x1.snap_id and s.snap_id = x2.snap_id and s.dbid = x1.dbid and s.dbid = x2.dbid and s.inum = x1.instance_number and s.inum = x2.instance_number and x1.event_id = x2.event_id and x1.total_waits_fg != x2.total_waits_fg)",
        "dborawev": "dborawev as (select timestamp, (x2.time_waited_micro_fg - x1.time_waited_micro_fg) / 1000000 / duration time, (x2.total_waits_fg - x1.total_waits_fg) / duration count, (x2.total_timeouts_fg - x1.total_timeouts_fg) / duration timeouts, x2.event_name event from snapshots s, dba_hist_system_event x1, dba_hist_system_event x2 where s.prev_snap_id = x1.snap_id and s.snap_id = x2.snap_id and s.dbid = x1.dbid and s.dbid = x2.dbid and s.inum = x1.instance_number and s.inum = x2.instance_number and x1.event_id = x2.event_id and x1.total_waits_fg != x2.total_waits_fg)",
    }
    def __init__(s):
        object = {
            "type": "liveobject",
            "id": "ORACLE_AWR_BRIDGE",
            "tables": {
                "DBORAAWR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dboraawr)s select * from dboraawr" % UserObject.DEFS,
                            {"timestamp": "text", "elapsed": "int", "avgelapsed": "real", "type": "text", "sessions": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORAFIL": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborafil)s select * from dborafil" % UserObject.DEFS,
                            {"timestamp": "text", "reads": "real", "blocksperread": "real", "tablespace": "text", "file": "text", "readtime": "real", "writes": "real", "busy": "real", "busytime": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORAINFO": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborainfo)s select * from dborainfo" % UserObject.DEFS,
                            {"timestamp": "text", "startup": "text"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORAMISC": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dboramisc)s select * from dboramisc" % UserObject.DEFS,
                            {"timestamp": "text", "elapsed": "int", "avgelapsed": "real", "type": "text", "sessions": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORAOSS": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dboraoss)s select * from dboraoss" % UserObject.DEFS,
                            {"timestamp": "text", "value": "real", "statistic": "text"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORAREQ": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(dbid)s, %(dborareq)s select * from dborareq" % UserObject.DEFS,
                            {"sqlid": "text", "request": "text", "module": "text"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGA": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasga)s select * from dborasga" % UserObject.DEFS,
                            {"timestamp": "text", "pool": "text", "name": "text", "size": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGBBW": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgbbw)s select * from dborasgbbw" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "waits": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGCBR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgcbr)s select * from dborasgcbr" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "blocks": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGCRBR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgcrbr)s select * from dborasgcrbr" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "blocks": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGDBC": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgdbc)s select * from dborasgdbc" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "changes": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGDPR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgdpr)s select * from dborasgdpr" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "reads": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGDPW": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgdpw)s select * from dborasgdpw" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "writes": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGGCBB": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasggcbb)s select * from dborasggcbb" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "waits": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGIW": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgiw)s select * from dborasgiw" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "waits": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGLR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasglr)s select * from dborasglr" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "gets": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGOR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgor)s select * from dborasgor" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "reads": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGPR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgpr)s select * from dborasgpr" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "reads": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGPRR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgprr)s select * from dborasgprr" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "reads": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGPW": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgpw)s select * from dborasgpw" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "writes": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGPWR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgpwr)s select * from dborasgpwr" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "writes": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGRLW": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgrlw)s select * from dborasgrlw" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "waits": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGTS": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgts)s select * from dborasgts" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "scans": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASGUR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(segname)s, %(dborasgur)s select * from dborasgur" % UserObject.DEFS,
                            {"timestamp": "text", "tablespace": "text", "object": "text", "owner": "text","objtype": "text", "subobject": "text", "reads": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASQC": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasqc)s select * from dborasqc" % UserObject.DEFS,
                            {"timestamp": "text", "gets": "real", "cpu": "real", "percent": "real", "elapsed": "real", "sqlid": "text", "execs": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASQE": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasqe)s select * from dborasqe" % UserObject.DEFS,
                            {"timestamp": "text", "reads": "real", "cpu": "real", "percent": "real", "elapsed": "real", "sqlid": "text", "execs": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASQG": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasqg)s select * from dborasqg" % UserObject.DEFS,
                            {"timestamp": "text", "gets": "real", "cpu": "real", "percent": "real", "elapsed": "real", "sqlid": "text", "execs": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASQM": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasqm)s select * from dborasqm" % UserObject.DEFS,
                            {"timestamp": "text", "sharedmem": "real", "percent": "real", "sqlid": "text", "execs": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASQP": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasqp)s select * from dborasqp" % UserObject.DEFS,
                            {"timestamp": "text", "parses": "real", "percent": "real", "sqlid": "text", "execs": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASQR": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasqr)s select * from dborasqr" % UserObject.DEFS,
                            {"timestamp": "text", "reads": "real", "cpu": "real", "percent": "real", "elapsed": "real", "sqlid": "text", "execs": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASQV": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasqv)s select * from dborasqv" % UserObject.DEFS,
                            {"timestamp": "text", "versioncount": "real", "percent": "real", "sqlid": "text", "execs": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASQW": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasqw)s select * from dborasqw" % UserObject.DEFS,
                            {"timestamp": "text", "clusterwait": "real", "cpu": "real", "elapsed": "real", "sqlid": "text", "execs": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASQX": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasqx)s select * from dborasqx" % UserObject.DEFS,
                            {"timestamp": "text", "cpuperexec": "real", "rows": "real", "elapsedperexec": "real", "sqlid": "text", "execs": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASRV": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(svstats)s, %(dborasrv)s select * from dborasrv" % UserObject.DEFS,
                            {"timestamp": "text", "reads": "real", "gets": "real", "dbtime": "real", "service": "text", "cpu": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASTA": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborasta)s select * from dborasta" % UserObject.DEFS,
                            {"timestamp": "text", "statistic": "text", "value": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORASVW": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(swstats)s, %(dborasvw)s select * from dborasvw" % UserObject.DEFS,
                            {"timestamp": "text", "netwaits": "real", "netwaitt": "real", "uiowaits": "real", "service": "text", "uiowaitt": "real", "admwaits": "real", "admwaitt": "real", "conwaits": "real", "conwaitt": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORATBS": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dboratbs)s select * from dboratbs" % UserObject.DEFS,
                            {"timestamp": "text", "reads": "real", "blocksperread": "real", "tablespace": "text", "readtime": "real", "writes": "real", "busy": "real", "busytime": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORATMS": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dboratms)s select * from dboratms" % UserObject.DEFS,
                            {"timestamp": "text", "statistic": "text", "time": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORAWEB": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dboraweb)s select * from dboraweb" % UserObject.DEFS,
                            {"timestamp": "text", "event": "text", "time": "real", "timeouts": "real", "count": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORAWEC": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborawec)s select * from dborawec" % UserObject.DEFS,
                            {"timestamp": "text", "eclass": "text", "time": "real", "timeouts": "real", "count": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "DBORAWEV": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "with %(iname)s, %(defday)s, %(interval)s, %(dbid)s, %(inum)s, %(dbname)s, %(alldeltas)s, %(snapshots)s, %(dborawev)s select * from dborawev" % UserObject.DEFS,
                            {"timestamp": "text", "event": "text", "time": "real", "timeouts": "real", "count": "real"}
                        ],
                    "method": UserObject.OracleBridge
                },
                "ORAHAS": {
                    "parameters": [
                            UserObject.CONNECTSTRING,
                            "select sample_id, to_char(sample_time,'yyyymmddhh24missff') timestamp, is_awr_sample, session_id, session_serial# session_serial, session_type, flags, user_id, sql_id, is_sqlid_current, sql_child_number, sql_opcode, sql_opname, force_matching_signature, top_level_sql_id, top_level_sql_opcode, sql_adaptive_plan_resolved, sql_full_plan_hash_value, sql_plan_hash_value, sql_plan_line_id, sql_plan_operation, sql_plan_options, sql_exec_id, sql_exec_start, plsql_entry_object_id, plsql_entry_subprogram_id, plsql_object_id, plsql_subprogram_id, qc_instance_id, qc_session_id, qc_session_serial# qc_session_serial, px_flags, event, event_id, event# eventnum, seq# seq, p1text, p1, p2text, p2, p3text, p3, wait_class, wait_class_id, wait_time, session_state, time_waited, blocking_session_status, blocking_session, blocking_session_serial# blocking_session_serial, blocking_inst_id, blocking_hangchain_info, current_obj# current_obj, current_file# current_file, current_block# current_block, current_row# current_row, top_level_call# top_level_call, top_level_call_name, consumer_group_id, xid,  remote_instance# remote_instance, time_model, in_connection_mgmt, in_parse, in_hard_parse, in_sql_execution, in_plsql_execution, in_plsql_rpc, in_plsql_compilation, in_java_execution, in_bind, in_cursor_close, in_sequence_load, in_inmemory_query, in_inmemory_populate, in_inmemory_prepopulate, in_inmemory_repopulate, in_inmemory_trepopulate, capture_overhead, replay_overhead, is_captured, is_replayed, service_hash, program, module, action, client_id, machine, port, ecid, dbreplay_file_id, dbreplay_call_counter, tm_delta_time, tm_delta_cpu_time, tm_delta_db_time, delta_time, delta_read_io_requests, delta_write_io_requests, delta_read_io_bytes, delta_write_io_bytes, delta_interconnect_io_bytes, delta_read_mem_bytes, pga_allocated, temp_space_allocated, con_dbid, con_id, dbop_name, dbop_exec_id from v$active_session_history",
                            {"sample_id": "text", "session_id": "text", "session_serial": "text", "flags": "text", "user_id": "text", "sql_child_number": "text", "sql_opcode": "text", "force_matching_signature": "text", "top_level_sql_opcode": "text", "sql_adaptive_plan_resolved": "text", "sql_full_plan_hash_value": "text", "sql_plan_hash_value": "text", "sql_plan_line_id": "text", "sql_exec_id": "text", "plsql_entry_object_id": "text", "plsql_entry_subprogram_id": "text", "plsql_object_id": "text", "plsql_subprogram_id": "text", "qc_instance_id": "text", "qc_session_id": "text", "qc_session_serial": "text", "px_flags": "text", "event_id": "text", "eventnum": "text", "seq": "text", "p1": "text", "p2": "text", "p3": "text", "wait_class_id": "text", "blocking_session": "text", "blocking_session_serial": "text", "blocking_inst_id": "text", "current_obj": "text", "current_file": "text", "current_block": "text", "current_row": "text", "top_level_call": "text", "consumer_group_id": "text", "remote_instance": "text", "time_model": "text", "service_hash": "text", "port": "text", "dbreplay_file_id": "text", "con_dbid": "text", "con_id": "text", "dbop_exec_id": "text"}
                        ],
                    "method": UserObject.OracleBridge
                },
            },
        } 

        super(UserObject, s).__init__(**object)

    class OracleBridge:
        def Connect(self, db, modulename, dbname, tablename, *args):
            import cx_Oracle, base64, json, logging, sys
            [url, sql, jsontr, nodeid] = [base64.b64decode(p.encode()).decode() for p in args]
            typesredefined = json.loads(jsontr)
            self.nodeid = nodeid
            self.odbh = cx_Oracle.connect(url)
            self.db = db
            self.tablename = tablename
            realtable = tablename.lower().replace('virtual_','')
            self.realtable = realtable
            oc = cx_Oracle.Cursor(self.odbh)
            request = "select * from (" + sql + ") where rownum < 1"
            oc.execute(request)
            columns = []
            types = []
            desc = []
            for c in oc.description:
                columns.append(c[0].lower())
                ctype = 'text' if c[1] == cx_Oracle.STRING else None
                ctype = 'real' if c[1] == cx_Oracle.NUMBER else ctype
                ctype = 'text' if c[1] == cx_Oracle.DATETIME else ctype
                ctype = 'text' if c[1] == cx_Oracle.BINARY else ctype
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
            cursor.execute(request)
            cursor.close()
            self.cursor = oc.execute(sql)
            self.logging = logging
            return self.schema, self.OracleBridgeTable(self.columns, self)

        def Create(self, db, modulename, dbname, tablename, *args):
            if not hasattr(self, "schema"):
                x = self.Connect(db, modulename, dbname, tablename, *args)
                self.odbh.close()
                return x 
            else:
                return self.schema, self.BridgeTable(self.columns, self)

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
                    self.table.bridge.odbh.close()