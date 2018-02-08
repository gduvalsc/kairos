import json, argparse, zipfile, os, socket
from com.ziclix.python.sql import zxJDBC
from datetime import datetime, timedelta

class Oracle:
    def __init__(s, jdbc_url, username, password, driver):
        s.connection = zxJDBC.connect(jdbc_url, username, password, driver)
    def execute(s, request):
        cursor = s.connection.cursor()
        cursor.execute(request)
        return cursor
    def callproc(s, proc, *parameters):
        request = "begin " + proc + "(" + ', '.join([json.dumps(e) for e in list(parameters)]) + "); end;"
        request = request.replace('"', "'")
        return s.execute(request)
    def callfunc(s, func, *parameters):
        request = "select " + func + "(" + ', '.join([json.dumps(e) for e in list(parameters)]) + ") from dual"
        request = request.replace('"', "'")
        return s.execute(request)

class Parameter:
    def __init__(s, n, t):
        s.name = n
        s.target = t

def parse(x):
  if x.upper() == 'YESTERDAY':
    yesterday = datetime.now() - timedelta(1)
    r = datetime(yesterday.year, yesterday.month, yesterday.day)
  elif x.upper() == 'TODAY':
    today = datetime.now()
    r = datetime(today.year, today.month, today.day)
  else:
    try: r=datetime.strptime(x, '%Y-%m-%d %H:%M')
    except:
      try: r=datetime.strptime(x, '%Y-%m-%d %H')
      except: r=datetime.strptime(x, '%Y-%m-%d')
  return r

def strs(x):
  return "" if x == None else x

PHST = Parameter('--host', 'host')
PPRT = Parameter('--port', 'port')
PSRV = Parameter('--service', 'service')
PUSR = Parameter('--user', 'user')
PPWD = Parameter('--password', 'password')
PINS = Parameter('--instance', 'instance')
PLVL = Parameter('--level', 'level')
PAWR = Parameter('--awr', 'awr')
PFRM = Parameter('--from', 'from')
PTO = Parameter('--to', 'to')
PDIR = Parameter('--directory', 'directory')
PBAS = Parameter('--bash', 'bash')

GET_STATSPACK_NUMBER = """
create or replace function get_statspack_number (bid in number, eid in number, dbid in number, inst_num in number, para in varchar2, statname in varchar2) return number is
  lhtr    number;
  bfwt   number;
  tran    number;
  chng   number;
  ucal    number;
  urol   number;
  rsiz    number;
  phyr    number;
  phyrd  number;
  phyrdl  number;
  phyrc  number;
  phyw    number;
  ucom   number;
  prse    number;
  hprse  number;
  recr    number;
  gets   number;
  slr     number;
  rlsr    number;
  rent   number;
  srtm    number;
  srtd   number;
  srtr    number;
  strn   number;
  lhr     number;
  bbc     varchar2(80);
  ebc    varchar2(80);
  bsp     varchar2(80);
  esp    varchar2(80);
  blb     varchar2(80);
  bs      varchar2(80);
  twt    number;
  logc    number;
  prscpu number;
  tcpu    number;
  exe    number;
  prsela  number;
  bspm    number;
  espm   number;
  bfrm    number;
  efrm   number;
  blog    number;
  elog   number;
  bocur   number;
  eocur  number;
  bpgaalloc number;
  epgaalloc number;
  bsgaalloc number;
  esgaalloc number;
  bnprocs number;
  enprocs number;
  timstat varchar2(80);
  statlvl varchar2(80);
  bncpu   number;
  encpu  number  ;
  bpmem   number;
  epmem  number;
  blod    number;
  elod   number;
  itic    number;
  btic   number;
  iotic   number;
  rwtic  number;
  utic    number;
  stic   number;
  vmib    number;
  vmob   number;
  oscpuw  number;
  dbtim   number;
  dbcpu  number ;
  bgela   number;
  bgcpu  number;
  prstela number;
  sqleela number;
  conmela number;
  dmsd    number;
  dmfc   number;
  dmsi    number;
  pmrv    number;
  pmpt   number;
  npmrv   number;
  npmpt  number;
  dbfr    number;
  dpms    number;
  dnpms  number;
  glsg    number;
  glag   number;
  glgt    number;
  gccrrv  number;
  gccrrt number;
  gccrfl number;
  gccurv  number;
  gccurt number;
  gccufl number;
  gccrsv  number;
  gccrbt  number;
  gccrft number;
  gccrst  number;
  gccusv number;
  gccupt  number;
  gccuft number;
  gccust  number;
  msgsq   number;
  msgsqt  number;
  msgsqk  number;
  msgsqtk number;
  msgrq   number;
  msgrqt  number; 
begin
   STATSPACK.STAT_CHANGES (bid, eid, dbid, inst_num, para , lhtr, bfwt, tran, chng, ucal, urol, rsiz, phyr, phyrd, phyrdl, phyrc, phyw, ucom, prse, hprse, recr, gets, slr, rlsr, rent, srtm, srtd, srtr, strn, lhr, bbc, ebc, bsp, esp, blb, bs, twt, logc, prscpu, tcpu, exe, prsela, bspm, espm, bfrm, efrm, blog, elog, bocur, eocur, bpgaalloc, epgaalloc, bsgaalloc, esgaalloc, bnprocs, enprocs, timstat, statlvl, bncpu, encpu , bpmem, epmem, blod, elod, itic, btic, iotic, rwtic, utic, stic, vmib, vmob, oscpuw, dbtim, dbcpu , bgela, bgcpu, prstela,sqleela, conmela, dmsd, dmfc , dmsi, pmrv, pmpt, npmrv, npmpt, dbfr, dpms, dnpms, glsg, glag, glgt, gccrrv, gccrrt, gccrfl, gccurv, gccurt, gccufl, gccrsv, gccrbt, gccrft, gccrst, gccusv, gccupt, gccuft, gccust, msgsq, msgsqt, msgsqk, msgsqtk, msgrq, msgrqt);
   if statname = 'elog' then
      return elog;
   end if;
   if statname = 'dbcpu' then
      return dbcpu;
   end if;
   if statname = 'dbtim' then
      return dbtim;
   end if;
   if statname = 'gets' then
      return gets;
   end if;
   if statname = 'phyr' then
      return phyr;
   end if;
   if statname = 'prse' then
      return prse;
   end if;
   if statname = 'espm' then
      return espm;
   end if;
end;
"""
GET_STATSPACK_VARCHAR = """
create or replace function get_statspack_varchar (bid in number, eid in number, dbid in number, inst_num in number, para in varchar2, statname in varchar2) return varchar2 is
  lhtr    number;
  bfwt   number;
  tran    number;
  chng   number;
  ucal    number;
  urol   number;
  rsiz    number;
  phyr    number;
  phyrd  number;
  phyrdl  number;
  phyrc  number;
  phyw    number;
  ucom   number;
  prse    number;
  hprse  number;
  recr    number;
  gets   number;
  slr     number;
  rlsr    number;
  rent   number;
  srtm    number;
  srtd   number;
  srtr    number;
  strn   number;
  lhr     number;
  bbc     varchar2(80);
  ebc    varchar2(80);
  bsp     varchar2(80);
  esp    varchar2(80);
  blb     varchar2(80);
  bs      varchar2(80);
  twt    number;
  logc    number;
  prscpu number;
  tcpu    number;
  exe    number;
  prsela  number;
  bspm    number;
  espm   number;
  bfrm    number;
  efrm   number;
  blog    number;
  elog   number;
  bocur   number;
  eocur  number;
  bpgaalloc number;
  epgaalloc number;
  bsgaalloc number;
  esgaalloc number;
  bnprocs number;
  enprocs number;
  timstat varchar2(80);
  statlvl varchar2(80);
  bncpu   number;
  encpu  number  ;
  bpmem   number;
  epmem  number;
  blod    number;
  elod   number;
  itic    number;
  btic   number;
  iotic   number;
  rwtic  number;
  utic    number;
  stic   number;
  vmib    number;
  vmob   number;
  oscpuw  number;
  dbtim   number;
  dbcpu  number ;
  bgela   number;
  bgcpu  number;
  prstela number;
  sqleela number;
  conmela number;
  dmsd    number;
  dmfc   number;
  dmsi    number;
  pmrv    number;
  pmpt   number;
  npmrv   number;
  npmpt  number;
  dbfr    number;
  dpms    number;
  dnpms  number;
  glsg    number;
  glag   number;
  glgt    number;
  gccrrv  number;
  gccrrt number;
  gccrfl number;
  gccurv  number;
  gccurt number;
  gccufl number;
  gccrsv  number;
  gccrbt  number;
  gccrft number;
  gccrst  number;
  gccusv number;
  gccupt  number;
  gccuft number;
  gccust  number;
  msgsq   number;
  msgsqt  number;
  msgsqk  number;
  msgsqtk number;
  msgrq   number;
  msgrqt  number; 
begin
   STATSPACK.STAT_CHANGES (bid, eid, dbid, inst_num, para , lhtr, bfwt, tran, chng, ucal, urol, rsiz, phyr, phyrd, phyrdl, phyrc, phyw, ucom, prse, hprse, recr, gets, slr, rlsr, rent, srtm, srtd, srtr, strn, lhr, bbc, ebc, bsp, esp, blb, bs, twt, logc, prscpu, tcpu, exe, prsela, bspm, espm, bfrm, efrm, blog, elog, bocur, eocur, bpgaalloc, epgaalloc, bsgaalloc, esgaalloc, bnprocs, enprocs, timstat, statlvl, bncpu, encpu , bpmem, epmem, blod, elod, itic, btic, iotic, rwtic, utic, stic, vmib, vmob, oscpuw, dbtim, dbcpu , bgela, bgcpu, prstela,sqleela, conmela, dmsd, dmfc , dmsi, pmrv, pmpt, npmrv, npmpt, dbfr, dpms, dnpms, glsg, glag, glgt, gccrrv, gccrrt, gccrfl, gccurv, gccurt, gccufl, gccrsv, gccrbt, gccrft, gccrst, gccusv, gccupt, gccuft, gccust, msgsq, msgsqt, msgsqk, msgsqtk, msgrq, msgrqt);
   if statname = 'bs' then
      return bs;
   end if;
end;
"""

CREATE_TMP_SQLSTATS = """
create table stats$tmp_sqlstats (
  SQL_ID VARCHAR2(31),
  TEXT_SUBSET                   VARCHAR2(31),
  MODULE                        VARCHAR2(64),
  DELTA_BUFFER_GETS             NUMBER,      
  DELTA_EXECUTIONS              NUMBER,       
  DELTA_CPU_TIME                NUMBER,       
  DELTA_ELAPSED_TIME            NUMBER,       
  AVG_ELAPSED_TIME              NUMBER,       
  AVG_HARD_PARSE_TIME           NUMBER,       
  DELTA_DISK_READS              NUMBER,       
  DELTA_PARSE_CALLS             NUMBER,       
  MAX_SHARABLE_MEM              NUMBER,       
  LAST_SHARABLE_MEM             NUMBER,       
  DELTA_VERSION_COUNT           NUMBER,       
  MAX_VERSION_COUNT             NUMBER,       
  LAST_VERSION_COUNT            NUMBER,       
  DELTA_CLUSTER_WAIT_TIME       NUMBER,       
  DELTA_ROWS_PROCESSED          NUMBER       
)
"""
POPULATE_TMP_SQLSTATS = """
insert into stats$tmp_sqlstats
  ( sql_id, text_subset, module
  , delta_buffer_gets, delta_executions, delta_cpu_time
  , delta_elapsed_time, avg_hard_parse_time, delta_disk_reads, delta_parse_calls
  , max_sharable_mem, last_sharable_mem
  , delta_version_count, max_version_count, last_version_count
  , delta_cluster_wait_time, delta_rows_processed
  )
 select sql_id, text_subset, module
      , delta_buffer_gets, delta_executions, delta_cpu_time
      , delta_elapsed_time, avg_hard_parse_time, delta_disk_reads, delta_parse_calls
      , max_sharable_mem, last_sharable_mem
      , delta_version_count, max_version_count, last_version_count
      , delta_cluster_wait_time, delta_rows_processed
  from ( select -- sum deltas
                sql_id
              , text_subset
              , module
              , sum(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else
                         case when (address != prev_address)
                                or (buffer_gets < prev_buffer_gets)
                              then buffer_gets
                              else buffer_gets - prev_buffer_gets
                         end
                   end)                    delta_buffer_gets
              , sum(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else
                         case when (address != prev_address)
                                or (executions < prev_executions)
                              then executions
                              else executions - prev_executions
                         end
                    end)                   delta_executions
              , sum(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else
                         case when (address != prev_address)
                                or (cpu_time < prev_cpu_time)
                              then cpu_time
                              else cpu_time - prev_cpu_time
                         end
                    end)                  delta_cpu_time
              , sum(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else
                         case when (address != prev_address)
                                or (elapsed_time < prev_elapsed_time)
                              then elapsed_time
                              else elapsed_time - prev_elapsed_time
                         end
                    end)                  delta_elapsed_time
              , avg(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else avg_hard_parse_time
                    end)                  avg_hard_parse_time
              , sum(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else
                         case when (address != prev_address)
                                or (disk_reads < prev_disk_reads)
                              then disk_reads
                              else disk_reads - prev_disk_reads
                         end
                    end)                   delta_disk_reads
              , sum(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else
                         case when (address != prev_address)
                                or (parse_calls < prev_parse_calls)
                              then parse_calls
                              else parse_calls - prev_parse_calls
                         end
                    end)                   delta_parse_calls
              , max(sharable_mem)          max_sharable_mem
              , sum(case when snap_id = %(eid)s
                         then last_sharable_mem
                         else 0
                    end)                   last_sharable_mem
              , sum(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else
                         case when (address != prev_address)
                                or (version_count < prev_version_count)
                              then version_count
                              else version_count - prev_version_count
                         end
                    end)                   delta_version_count
              , max(version_count)         max_version_count
              , sum(case when snap_id = %(eid)s
                         then last_version_count
                         else 0
                    end)                   last_version_count
              , sum(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else
                         case when (address != prev_address)
                                or (cluster_wait_time < prev_cluster_wait_time)
                              then cluster_wait_time
                              else cluster_wait_time - prev_cluster_wait_time
                         end
                    end)                   delta_cluster_wait_time
              , sum(case
                    when snap_id = %(bid)s and prev_snap_id = -1
                    then 0
                    else
                         case when (address != prev_address)
                                or (rows_processed < prev_rows_processed)
                              then rows_processed
                              else rows_processed - prev_rows_processed
                         end
                    end)                   delta_rows_processed
          from (select /*+ first_rows */
                       -- windowing function
                       snap_id
                     , sql_id
                     , text_subset
                     , module
                     , (lag(snap_id, 1, -1)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                            order by snap_id))    prev_snap_id
                     , (lead(snap_id, 1, -1)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                            order by snap_id))    next_snap_id
                     , address
                     ,(lag(address, 1, hextoraw(0))
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_address
                     , buffer_gets
                     ,(lag(buffer_gets, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_buffer_gets
                     , cpu_time
                     ,(lag(cpu_time, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_cpu_time
                     , executions
                     ,(lag(executions, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_executions
                     , elapsed_time
                     ,(lag(elapsed_time, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_elapsed_time
                     , avg_hard_parse_time
                     , disk_reads
                     ,(lag(disk_reads, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_disk_reads
                     , parse_calls
                     ,(lag(parse_calls, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_parse_calls
                     , sharable_mem
                     ,(last_value(sharable_mem)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   last_sharable_mem
                     ,(lag(sharable_mem, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_sharable_mem
                     , version_count
                     ,(lag(version_count, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_version_count
                     ,(last_value(version_count)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   last_version_count
                     , cluster_wait_time
                     ,(lag(cluster_wait_time, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_cluster_wait_time
                     , rows_processed
                     ,(lag(rows_processed, 1, 0)
                       over (partition by sql_id
                                        , dbid
                                        , instance_number
                             order by snap_id))   prev_rows_processed
                from stats$sql_summary s
               where s.snap_id between %(bid)s and %(eid)s
                 and s.dbid            = %(dbid)s
                 and s.instance_number = %(instance_number)s
               )
        group by sql_id
               , text_subset
               , module
       )
 where delta_buffer_gets       > 0
    or delta_executions        > 0
    or delta_cpu_time          > 0
    or delta_disk_reads        > 0
    or delta_parse_calls       > 0
    or max_sharable_mem        > 0
    or max_version_count       > 0
    or delta_cluster_wait_time > 0
"""

SPVALIDDELTAS = """
    select dbid, instance_number, to_char(startup_time, 'YYYYMMDDHH24MISS') startup_time, bid, eid, to_char(snap_time, 'YYYYMMDDHH24MISS')||'000' snap_time, round(((snap_time - prev_snap_time) * 1440 * 60), 0) elapsed from (
          select snap_time, 
                 first_value(snap_time) over (order by snap_time asc rows between 1 preceding and current row) prev_snap_time, 
                 first_value(snap_id) over (order by snap_time asc rows between 1 preceding and current row) bid, 
                 snap_id eid,
                 first_value(dbid) over (order by snap_time asc rows between 1 preceding and current row) prev_dbid,
                 dbid,
                 first_value(instance_number) over (order by snap_time asc rows between 1 preceding and current row) prev_instance_number,
                 instance_number,
                 first_value(startup_time) over (order by snap_time asc rows between 1 preceding and current row) prev_startup_time,
                 startup_time
          from stats$snapshot 
          where session_id=0
    )
    where dbid=prev_dbid and instance_number=prev_instance_number and startup_time=prev_startup_time and bid != eid
"""

def get_parameters(parser, args):
    mandatory = [PHST, PPRT, PSRV, PAWR, PUSR, PPWD, PINS]
    if vars(args)[PAWR.target]: mandatory.extend([PLVL])
    vars(args)[PHST.target] = socket.gethostname() if vars(args)[PHST.target] == None else vars(args)[PHST.target]
    vars(args)[PSRV.target] = os.environ['ORACLE_SID'] if vars(args)[PSRV.target] == None and 'ORACLE_SID' in os.environ else vars(args)[PHST.target]
    vars(args)[PINS.target] = os.environ['ORACLE_SID'] if vars(args)[PINS.target] == None and 'ORACLE_SID' in os.environ else vars(args)[PINS.target]
    vars(args)[PDIR.target] = '/tmp' if vars(args)[PDIR.target] == None else vars(args)[PDIR.target]
    vars(args)[PFRM.target] = '19000101000000000' if vars(args)[PFRM.target] == None else datetime.strftime(parse(vars(args)[PFRM.target]), '%Y%m%d%H%M%S') + '000' 
    vars(args)[PTO.target] = '20991231235959000' if vars(args)[PTO.target] == None else datetime.strftime(parse(vars(args)[PTO.target]), '%Y%m%d%H%M%S') + '000' 
    for m in mandatory:
        if m.target not in vars(args) or vars(args)[m.target] == None:
            message = '*** Parameter: ' + m.name + ' is mandatory!'
            parser.error(message)
            exit(1)
    parameters = vars(args)
    return parameters

def pprint(c):
    result = c.fetchall()
    print(c.description)
    print('*' * 80)
    for x in result: print(str(x))


parser = argparse.ArgumentParser()
parser.add_argument('--version', action = 'version', version='KAIROSORAXTRACT V0.1')
parser.add_argument(PAWR.name, action = 'store_true', dest=PAWR.target, default=False, help='True: AWR extract, False: STATSPACK extract')
parser.add_argument(PHST.name, action = 'store', dest=PHST.target, help='Host to connect to using SQL*Net. Default: current host name')
parser.add_argument(PPRT.name, action = 'store', dest=PPRT.target, default='1521', help='Port number. Default 1521')
parser.add_argument(PSRV.name, action = 'store', dest=PSRV.target, help='Service to connect to. Default: value of ORACLE_SID')
parser.add_argument(PUSR.name, action = 'store', dest=PUSR.target, default='PERFSTAT', help='Schema from which STATSPACK data is extracted. Deafult: PERFSTAT')
parser.add_argument(PPWD.name, action = 'store', dest=PPWD.target, help='PERFSTAT schema password in case of STATSPACK, SYS password in case of AWR')
parser.add_argument(PINS.name, action = 'store', dest=PINS.target, help='Instance from which to retrieve data. Default: value of ORACLE_SID')
parser.add_argument(PLVL.name, action = 'store', dest=PLVL.target, default='1', help='Level 1: Extract AWR, level 2: Detailed info on requests, level 3: ASH')
parser.add_argument(PFRM.name, action = 'store', dest=PFRM.target, help='Extract data generated from this date')
parser.add_argument(PTO.name, action = 'store', dest=PTO.target, help='Extract data generated until this date')
parser.add_argument(PDIR.name, action = 'store', dest=PDIR.target, help='Directory to store the result. Default: /tmp')
parser.add_argument(PBAS.name, action = 'store_true', dest=PBAS.target, default=False, help='True: B-ash extract')
args = parser.parse_args()
parameters = get_parameters(parser, args)
oracle = Oracle("jdbc:oracle:thin:@" + parameters[PHST.target] + ":" + parameters[PPRT.target] + ":" + parameters[PSRV.target], parameters[PUSR.target], parameters[PPWD.target], "oracle.jdbc.driver.OracleDriver")
oracle.execute("alter session set nls_date_format='YYYYMMDDHH24MISS'")
masterlist = [dict(dbid=str(r[0]), instance_number=str(int(r[1])), startup_time=str(r[2])) for r in oracle.execute("select dbid, instance_number, to_char(startup_time, 'YYYYMMDDHH24MISS') startup_time from stats$database_instance where instance_name = '" + parameters[PINS.target] + "'").fetchall()]
deltas = [dict(dbid=str(r[0]), instance_number=str(int(r[1])), startup_time=str(r[2]), bid=str(int(r[3])), eid=str(int(r[4])), snap_time=str(r[5]), elapsed=int(r[6])) for r in oracle.execute(SPVALIDDELTAS).fetchall()]
validdeltas = [d for d in deltas for e in masterlist if d['dbid']==e['dbid'] and d['instance_number'] == e['instance_number'] and d['startup_time'] == e['startup_time'] and d['snap_time'] >= parameters[PFRM.target] and d['snap_time'] < parameters[PTO.target]]
dmin=min([d['snap_time'] for d in validdeltas])
oracle.execute(GET_STATSPACK_NUMBER)
oracle.execute(GET_STATSPACK_VARCHAR)
try: oracle.execute("drop table stats$tmp_sqlstats")
except: pass
oracle.execute(CREATE_TMP_SQLSTATS)
zipname = parameters[PDIR.target] + '/kairos_' + parameters[PINS.target] + '_' + dmin[0:4] + '-' + dmin[4:6] + '-' + dmin[6:8] + '.zip'
zipf = zipfile.ZipFile(zipname, 'w', compression=zipfile.ZIP_DEFLATED)
captured = dict()
captured['DBORASTATSPACK'] = dict(collection='DBORASTATSPACK', desc= dict(type='text'), data=[])
captured['DBORAMISC'] = dict(collection='DBORAMISC', desc= dict(timestamp='text', avgelapsed='real', elapsed='integer', sessions='real', type='text'), data=[])
captured['DBORAINFO'] = dict(collection='DBORAINFO', desc= dict(timestamp='text', startup='text'), data=[])
captured['DBORATMS'] = dict(collection='DBORATMS', desc= dict(timestamp='text', statistic='text', time='real'), data=[])
captured['DBORAWEV'] = dict(collection='DBORAWEV', desc= dict(timestamp='text', event='text', count='real', time='real', timeouts='real'), data=[])
captured['DBORAWEB'] = dict(collection='DBORAWEB', desc= dict(timestamp='text', event='text', count='real', time='real', timeouts='real'), data=[])
captured['DBORAWEH'] = dict(collection='DBORAWEH', desc= dict(timestamp='text', event='text', bucket='text', count='real'), data=[])
captured['DBORASQC'] = dict(collection='DBORASQC', desc= dict(timestamp='text', sqlid='text', cpu='real', elapsed='real', gets='real', execs='real', percent='real'), data=[])
captured['DBORASQE'] = dict(collection='DBORASQE', desc= dict(timestamp='text', sqlid='text', cpu='real', elapsed='real', gets='real', execs='real', percent='real'), data=[])
captured['DBORASQG'] = dict(collection='DBORASQG', desc= dict(timestamp='text', sqlid='text', cpu='real', elapsed='real', gets='real', execs='real', percent='real'), data=[])
captured['DBORASQR'] = dict(collection='DBORASQR', desc= dict(timestamp='text', sqlid='text', cpu='real', elapsed='real', gets='real', execs='real', percent='real'), data=[])
captured['DBORASQX'] = dict(collection='DBORASQX', desc= dict(timestamp='text', sqlid='text', rows='real', execs='real', cpuperexec='real', elapsederexec='real'), data=[])
captured['DBORASQP'] = dict(collection='DBORASQP', desc= dict(timestamp='text', sqlid='text', parses='real', execs='real', percent='real'), data=[])
captured['DBORASQM'] = dict(collection='DBORASQM', desc= dict(timestamp='text', sqlid='text', sharedmem='real', execs='real', percent='real'), data=[])
captured['DBORASQV'] = dict(collection='DBORASQV', desc= dict(timestamp='text', sqlid='text', versioncount='real', execs='real'), data=[])
captured['DBORASQW'] = dict(collection='DBORASQW', desc= dict(timestamp='text', sqlid='text', cpu='real', elapsed='real', clusterwait='real', execs='real'), data=[])
captured['DBORAREQ'] = dict(collection='DBORAREQ', desc= dict(sqlid='text', module='text', request='text'), data=[])
captured['DBORASTA'] = dict(collection='DBORASTA', desc= dict(timestamp='text', statistic='text', value='real'), data=[])
captured['DBORADRV'] = dict(collection='DBORADRV', desc= dict(timestamp='text', statistic='text', value='real'), data=[])
captured['DBORAOSS'] = dict(collection='DBORAOSS', desc= dict(timestamp='text', statistic='text', value='real'), data=[])
captured['DBORATBS'] = dict(collection='DBORATBS', desc= dict(timestamp='text', tablespace='text', reads='real', writes='real', busy='real', blocksperread='real', readtime='real', busytime='real'), data=[])
captured['DBORAFIL'] = dict(collection='DBORAFIL', desc= dict(timestamp='text', tablespace='text', file='text', reads='real', writes='real', busy='real', blocksperread='real', readtime='real', busytime='real'), data=[])
captured['DBORAMDC'] = dict(collection='DBORAMDC', desc=dict(timestamp='text', component='text', operation='text', size='real', vmin='real', vmax='real', opcount='real'), data=[])
captured['DBORABUF'] = dict(collection='DBORABUF', desc=dict(timestamp='text', bufpool='text', gets='real', reads='real', writes='real', freewaits='real', writecompletewaits='real', busywaits='real'), data=[])
captured['DBORAENQ'] = dict(collection='DBORAENQ', desc=dict(timestamp='text', enqueue='text', requests='real', succgets='real', failedgets='real', waits='real', avgwaitpersec='real'), data=[])
captured['DBORALAW'] = dict(collection='DBORALAW', desc=dict(timestamp='text', latch='text', wait='real'), data=[])
captured['DBORALAT'] = dict(collection='DBORALAT', desc=dict(timestamp='text', latch='text', gets='real', misses='real', sleeps='real'), data=[])
captured['DBORALIB'] = dict(collection='DBORALIB', desc=dict(timestamp='text', item='text', gets='real', pins='real', reloads='real', invalidations='real'), data=[])
captured['DBORASGA'] = dict(collection='DBORASGA', desc=dict(timestamp='text', pool='text', name='text', size='real'), data=[])
captured['DBORAPRM'] = dict(collection='DBORAPRM', desc=dict(timestamp='text', parameter='text', value='text'), data=[])
captured['DBORASGLR'] = dict(collection='DBORASGLR', desc=dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', gets='real'), data=[])
captured['DBORASGPR'] = dict(collection='DBORASGPR', desc=dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', reads='real'), data=[])
captured['DBORASGRLW'] = dict(collection='DBORASGRLW', desc=dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', waits='real'), data=[])
captured['DBORASGIW'] = dict(collection='DBORASGIW', desc=dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', waits='real'), data=[])
captured['DBORASGBBW'] = dict(collection='DBORASGBBW', desc=dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', waits='real'), data=[])
captured['DBORASGGCBB'] = dict(collection='DBORASGGCBB', desc=dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', waits='real'), data=[])
captured['DBORASGCRBR'] = dict(collection='DBORASGCRBR', desc=dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', blocks='real'), data=[])
captured['DBORASGCBR'] = dict(collection='DBORASGCBR', desc=dict(timestamp='text', owner='text', tablespace='text', object='text', subobject='text', objtype='text', blocks='real'), data=[])
captured['DBORAPGA'] = dict(collection='DBORAPGA', desc=dict(timestamp='text', aggrtarget='real', autotarget='real', memalloc='real', memused='real'), data=[])
captured['DBORAPGC'] = dict(collection='DBORAPGC', desc=dict(timestamp='text', highoptimal='text', totexecs='real', execs0='real', execs1='real', execs2='real'), data=[])
captured['DBORABPA'] = dict(collection='DBORABPA', desc=dict(timestamp='text', bufpool='text', sizefactor='text', estphysreadsfactor='real'), data=[])
captured['DBORAPMA'] = dict(collection='DBORAPMA', desc=dict(timestamp='text', sizefactor='text', estextrabytesrw='real', estoveralloc='real'), data=[])
captured['DBORASPA'] = dict(collection='DBORASPA', desc=dict(timestamp='text', sizefactor='text', estloadtimefctr='real'), data=[])
captured['DBORASGAA'] = dict(collection='DBORASGAA', desc=dict(timestamp='text', sizefactor='text', estphysicalreads='real'), data=[])
captured['ORAHAS'] = dict(collection='ORAHAS', desc=dict(timestamp='text', kairos_count='int', sql_id='text', sample_id='text', session_id='text', session_serial='text', user_id='text', sql_child_number='text', sql_plan_hash_value='text', force_matching_signature='text', sql_opcode='text', service_hash='text', session_type='text', session_state='text', qc_session_id='text', qc_instance_id='text', blocking_session='text', blocking_session_status='text', blocking_session_serial='text', event='text', event_id='text', seq='text', p1='text', p1text='text', p2='text', p2text='text', p3='text', p3text='text', wait_class='text', wait_class_id='text', wait_time='real', time_waited='real', xid='text', current_obj='text', current_file='text', current_block='text', program='text', module='text', action='text', client_id='text', blocking_hangchain_info='text', blocking_inst_id='text', capture_overhead='text',consumer_group_id='text', current_row='text', delta_interconnect_io_bytes='real', delta_read_io_bytes='real', delta_read_io_requests='real', delta_time='real', delta_write_io_bytes='real', delta_write_io_requests='real', ecid='text', flags='text', in_bind='text', in_connection_mgmt='text', in_cursor_close='text', in_hard_parse='text', in_java_execution='text', in_parse='text', in_plsql_compilation='text', in_plsql_execution='text', in_plsql_rpc='text', in_sequence_load='text', in_sql_execution='text', is_captured='text', is_replayed='text', is_sqlid_current='text', machine='text', pga_allocated='real', plsql_entry_object_id='text', plsql_entry_subprogram_id='text', plsql_object_id='text', plsql_subprogram_id='text', port='text', qc_session_serial='text', remote_instance='text', replay_overhead='text', sql_exec_id='text', sql_exec_start='text', sql_opname='text', sql_plan_line_id='text', sql_plan_operation='text', sql_plan_options='text', temp_space_allocated='real', time_model='text', tm_delta_cpu_time='real', tm_delta_db_time='real', tm_delta_time='real', top_level_call='text', top_level_call_name='text', top_level_sql_id='text', top_level_sql_opcode='text', dbreplay_file_id='text', dbreplay_call_counter='text'), data=[])
for e in validdeltas:
    print('Extracting data from snapshot: ' + e['snap_time'] + '...')
    oracle.execute("truncate table stats$tmp_sqlstats")
    oracle.execute(POPULATE_TMP_SQLSTATS % dict(bid=e['bid'], eid=e['eid'], dbid=e['dbid'], instance_number=e['instance_number']))
    elog = oracle.execute("select get_statspack_number(" + e['bid'] + "," + e['eid'] + "," + e['dbid'] + "," + e['instance_number'] + ", 'NO', 'elog') from dual").fetchall()[0][0]
    dbcpu = oracle.execute("select get_statspack_number(" + e['bid'] + "," + e['eid'] + "," + e['dbid'] + "," + e['instance_number'] + ", 'NO', 'dbcpu') from dual").fetchall()[0][0]
    dbtim = oracle.execute("select get_statspack_number(" + e['bid'] + "," + e['eid'] + "," + e['dbid'] + "," + e['instance_number'] + ", 'NO', 'dbtim') from dual").fetchall()[0][0]
    gets = oracle.execute("select get_statspack_number(" + e['bid'] + "," + e['eid'] + "," + e['dbid'] + "," + e['instance_number'] + ", 'NO', 'gets') from dual").fetchall()[0][0]
    phyr = oracle.execute("select get_statspack_number(" + e['bid'] + "," + e['eid'] + "," + e['dbid'] + "," + e['instance_number'] + ", 'NO', 'phyr') from dual").fetchall()[0][0]
    prse = oracle.execute("select get_statspack_number(" + e['bid'] + "," + e['eid'] + "," + e['dbid'] + "," + e['instance_number'] + ", 'NO', 'prse') from dual").fetchall()[0][0]
    espm = oracle.execute("select get_statspack_number(" + e['bid'] + "," + e['eid'] + "," + e['dbid'] + "," + e['instance_number'] + ", 'NO', 'espm') from dual").fetchall()[0][0]
    bs = oracle.execute("select get_statspack_varchar(" + e['bid'] + "," + e['eid'] + "," + e['dbid'] + "," + e['instance_number'] + ", 'NO', 'bs') from dual").fetchall()[0][0]
    captured['DBORASTATSPACK']['data'].append(dict(type='STATSPACK'))
    captured['DBORAMISC']['data'].append(dict(timestamp=e['snap_time'], type='STATSPACK_12C', avgelapsed=float(e['elapsed']), elapsed=e['elapsed'],  sessions=float(elog)))
    captured['DBORAINFO']['data'].append(dict(timestamp=e['snap_time'], startup=e['startup_time']))
    captured['DBORATMS']['data'].extend([dict(timestamp=e['snap_time'], statistic=strs(r[0]),  time=float(r[1]) / e['elapsed'] / 1000000) for r in oracle.execute("select sn.stat_name statistic, (e.value - b.value) time from stats$sys_time_model e, stats$sys_time_model b, stats$time_model_statname sn where b.snap_id = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid = " + e['dbid'] + " and e.dbid  = " + e['dbid'] + " and b.instance_number = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.stat_id = e.stat_id and sn.stat_id = e.stat_id and e.value - b.value > 0").fetchall()])
    captured['DBORAWEV']['data'].extend([dict(timestamp=e['snap_time'], event=strs(r[0]),  count=float(r[1]) / e['elapsed'], time=float(r[3]) / e['elapsed'] / 1000000, timeouts=float(r[2]) / e['elapsed']) for r in oracle.execute("select e.event, e.total_waits_fg - nvl(b.total_waits_fg,0) count, e.total_timeouts_fg - nvl(b.total_timeouts_fg,0) timeouts, e.time_waited_micro_fg - nvl(b.time_waited_micro_fg,0) time from stats$system_event b, stats$system_event e, stats$idle_event i where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.event(+) = e.event and e.total_waits_fg > nvl(b.total_waits_fg,0) and i.event(+) = e.event").fetchall()])
    captured['DBORAWEB']['data'].extend([dict(timestamp=e['snap_time'], event=strs(r[0]),  count=float(r[1]) / e['elapsed'], time=float(r[3]) / e['elapsed'] / 1000000, timeouts=float(r[2]) / e['elapsed']) for r in oracle.execute("select e.event, e.total_waits - nvl(b.total_waits,0) count, e.total_timeouts - nvl(b.total_timeouts,0) timeouts, e.time_waited_micro - nvl(b.time_waited_micro,0) time from stats$bg_event_summary b, stats$bg_event_summary e, stats$idle_event i where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.event(+) = e.event and e.total_waits > nvl(b.total_waits,0) and i.event(+) = e.event").fetchall()])
    captured['DBORAWEH']['data'].extend([dict(timestamp=e['snap_time'], event=strs(r[0]), bucket=str(int(r[1])), count=float(r[2]) / e['elapsed']) for r in oracle.execute("select n.event event, e.wait_time_milli bucket, e.wait_count - nvl(b.wait_count, 0) count from stats$event_histogram b, stats$event_histogram e, (select distinct event, event_id from stats$system_event) n where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.event_id(+) = e.event_id and b.wait_time_milli(+) = e.wait_time_milli and e.event_id = n.event_id and e.wait_count - nvl(b.wait_count, 0) > 0").fetchall()])
    captured['DBORASQC']['data'].extend([dict(timestamp=e['snap_time'], sqlid=strs(r[0]),  cpu=float(r[1]) / e['elapsed'] / 1000000, elapsed=float(r[2]) / e['elapsed'] / 1000000, gets=float(r[3]) / e['elapsed'], execs=float(r[4]) / e['elapsed'], percent= 0.0 if dbcpu == 0.0 else 100 * float(r[1]) / dbcpu) for r in oracle.execute("select sql_id sqlid, delta_cpu_time cpu, delta_elapsed_time elapsed, delta_buffer_gets gets, delta_executions execs from perfstat.stats$tmp_sqlstats ").fetchall()])
    captured['DBORASQE']['data'].extend([dict(timestamp=e['snap_time'], sqlid=strs(r[0]),  cpu=float(r[1]) / e['elapsed'] / 1000000, elapsed=float(r[2]) / e['elapsed'] / 1000000, reads=float(r[3]) / e['elapsed'], execs=float(r[4]) / e['elapsed'], percent= 0.0 if dbtim == 0.0 else 100 * float(r[2]) / dbtim) for r in oracle.execute("select sql_id sqlid, delta_cpu_time cpu, delta_elapsed_time elapsed, delta_disk_reads reads, delta_executions execs from perfstat.stats$tmp_sqlstats ").fetchall()])
    captured['DBORASQG']['data'].extend([dict(timestamp=e['snap_time'], sqlid=strs(r[0]),  cpu=float(r[1]) / e['elapsed'] / 1000000, elapsed=float(r[2]) / e['elapsed'] / 1000000, gets=float(r[3]) / e['elapsed'], execs=float(r[4]) / e['elapsed'], percent= 0.0 if gets == 0.0 else 100 * float(r[3]) / gets) for r in oracle.execute("select sql_id sqlid, delta_cpu_time cpu, delta_elapsed_time elapsed, delta_buffer_gets gets, delta_executions execs from perfstat.stats$tmp_sqlstats ").fetchall()])
    captured['DBORASQR']['data'].extend([dict(timestamp=e['snap_time'], sqlid=strs(r[0]),  cpu=float(r[1]) / e['elapsed'] / 1000000, elapsed=float(r[2]) / e['elapsed'] / 1000000, reads=float(r[3]) / e['elapsed'], execs=float(r[4]) / e['elapsed'], percent= 0.0 if phyr == 0.0 else 100 * float(r[3]) / phyr) for r in oracle.execute("select sql_id sqlid, delta_cpu_time cpu, delta_elapsed_time elapsed, delta_disk_reads reads, delta_executions execs from perfstat.stats$tmp_sqlstats ").fetchall()])
    captured['DBORASQX']['data'].extend([dict(timestamp=e['snap_time'], sqlid=strs(r[0]),  rows=float(r[1]) / e['elapsed'], execs=float(r[2]) / e['elapsed'], cpuperexec=float(r[3]) / 1000000, elapsedperexec=float(r[4]) / 1000000) for r in oracle.execute("select sql_id sqlid, delta_rows_processed rowes, delta_executions execs, decode(delta_executions, 0, 0, delta_cpu_time / delta_executions) cpuperexec, decode(delta_executions, 0, 0, delta_elapsed_time / delta_executions) elapsedperexec from perfstat.stats$tmp_sqlstats ").fetchall()])
    captured['DBORASQP']['data'].extend([dict(timestamp=e['snap_time'], sqlid=strs(r[0]),  parses=float(r[1]) / e['elapsed'], execs=float(r[2]) / e['elapsed'], percent= 0.0 if prse == 0.0 else 100 * float(r[1]) / prse) for r in oracle.execute("select sql_id sqlid, delta_parse_calls parses, delta_executions execs from perfstat.stats$tmp_sqlstats ").fetchall()])
    captured['DBORASQM']['data'].extend([dict(timestamp=e['snap_time'], sqlid=strs(r[0]),  sharedmem=float(r[1]) / e['elapsed'], execs=float(r[2]) / e['elapsed'], percent= 0.0 if espm == 0.0 else 100 * float(r[1]) / espm) for r in oracle.execute("select sql_id sqlid, max_sharable_mem sharedmem, delta_executions execs from perfstat.stats$tmp_sqlstats ").fetchall()])
    captured['DBORASQV']['data'].extend([dict(timestamp=e['snap_time'], sqlid=strs(r[0]),  versioncount=float(r[1]) / e['elapsed'], execs=float(r[2]) / e['elapsed']) for r in oracle.execute("select sql_id sqlid, max_version_count versioncount, delta_executions execs from perfstat.stats$tmp_sqlstats ").fetchall()])
    captured['DBORASQW']['data'].extend([dict(timestamp=e['snap_time'], sqlid=strs(r[0]),  cpu=float(r[1]) / e['elapsed'] / 1000000, elapsed=float(r[2]) / e['elapsed'] / 1000000, clusterwait=float(r[3]) / e['elapsed'] / 1000000, execs=float(r[4]) / e['elapsed']) for r in oracle.execute("select sql_id sqlid, delta_cpu_time cpu, delta_elapsed_time elapsed, delta_cluster_wait_time clusterwait, delta_executions execs from perfstat.stats$tmp_sqlstats ").fetchall()])
    captured['DBORAREQ']['data'].extend([dict(sqlid=strs(r[0]),  module=strs(r[1]), request=strs(r[2])) for r in oracle.execute("SELECT distinct p.sql_id sqlid, p.module module, RTRIM(XMLAGG(XMLELEMENT(E,t.sql_text,'').EXTRACT('//text()') ORDER BY t.piece).GetClobVal(),',') as request from perfstat.stats$tmp_sqlstats p, stats$sqltext t where p.sql_id=t.sql_id group by p.sql_id, p.module").fetchall()])
    captured['DBORASTA']['data'].extend([dict(timestamp=e['snap_time'], statistic=strs(r[0]),  value=float(r[1]) / e['elapsed']) for r in oracle.execute("select b.name statistic, e.value - b.value value from stats$sysstat b, stats$sysstat e where b.snap_id = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.name = e.name and e.name not in ('logons current', 'opened cursors current', 'workarea memory allocated', 'session cursor cache count') and e.value >= b.value and e.value  >  0").fetchall()])
    captured['DBORADRV']['data'].extend([dict(timestamp=e['snap_time'], statistic=strs(r[0]),  value=float(r[1]) / e['elapsed']) for r in oracle.execute("select 'log switches (derived)' statistic, e.sequence# - b.sequence# value from stats$thread e, stats$thread b where b.snap_id = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.thread# = e.thread# and b.thread_instance_number = e.thread_instance_number and e.thread_instance_number = " + e['instance_number']).fetchall()])
    captured['DBORAOSS']['data'].extend([dict(timestamp=e['snap_time'], statistic=strs(r[0]),  value=float(r[1])) for r in oracle.execute("select osn.stat_name statistic, decode( osn.cumulative, 'NO', e.value, e.value - b.value)  dif, (  to_number(decode(sign(instrb(osn.stat_name, 'TIME')), 1, 1, 0)) + to_number(decode(sign(instrb(osn.stat_name, 'LOAD')), 1, 2, 0)) + to_number(decode(sign(instrb(osn.stat_name, 'CPU_WAIT')), 1, 3, 0)) + to_number(decode(sign(instrb(osn.stat_name, 'VM_')), 1, 4, 0)) + to_number(decode(sign(instrb(osn.stat_name, 'PHYSICAL_MEMORY')), 1, 5, 0)) + to_number(decode(sign(instrb(osn.stat_name, 'NUM_CPU')), 1, 6, 0)) + to_number(decode(sign(instrb(osn.stat_name, 'TCP')), 1, 7, 0)) + to_number(decode(sign(instrb(osn.stat_name, 'GLOBAL')), 1, 7, 0))) value from  stats$osstat b, stats$osstat e, stats$osstatname osn where b.snap_id = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.osstat_id = e.osstat_id and osn.osstat_id = e.osstat_id and (osn.stat_name not like 'AVG_%' and osn.stat_name not like '%LOAD%') and e.value >= b.value and e.value > 0").fetchall()])
    captured['DBORATBS']['data'].extend([dict(timestamp=e['snap_time'], tablespace=strs(r[0]),  reads=float(r[1]) / e['elapsed'], writes=float(r[2]) / e['elapsed'], busy=float(r[3]) / e['elapsed'], blocksperread=float(r[4]), readtime=float(r[5]) / e['elapsed'] / 1000000 , busytime=float(r[6]) / e['elapsed'] / 1000000) for r in oracle.execute("select e.tsname tablespace, sum (e.phyrds - nvl(b.phyrds,0)) reads, sum (e.phywrts - nvl(b.phywrts,0)) writes, sum (e.wait_count - nvl(b.wait_count,0)) busy, decode( sum(e.phyrds - nvl(b.phyrds,0)), 0, 0, sum(e.phyblkrd - nvl(b.phyblkrd,0)) / sum(e.phyrds - nvl(b.phyrds,0))) blocksperread, decode( sum(e.phyrds - nvl(b.phyrds,0)), 0, 0, (sum(e.readtim - nvl(b.readtim,0)) / sum(e.phyrds  - nvl(b.phyrds,0)))*10) readtime, decode (sum(e.wait_count - nvl(b.wait_count, 0)), 0, 0, (sum(e.time - nvl(b.time,0)) / sum(e.wait_count - nvl(b.wait_count,0)))*10) busytime from stats$filestatxs e, stats$filestatxs b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.dbid(+) = e.dbid and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.instance_number(+) = e.instance_number and b.tsname(+) = e.tsname and b.filename(+) = e.filename and ( (e.phyrds - nvl(b.phyrds,0)) + (e.phywrts - nvl(b.phywrts,0))) > 0 group by e.tsname union all select e.tsname tablespace, sum (e.phyrds - nvl(b.phyrds,0)) reads, sum (e.phywrts - nvl(b.phywrts,0)) writes, sum (e.wait_count - nvl(b.wait_count,0)) busy, decode( sum(e.phyrds - nvl(b.phyrds,0)), 0, 0, sum(e.phyblkrd - nvl(b.phyblkrd,0)) / sum(e.phyrds - nvl(b.phyrds,0))) blocksperread, decode( sum(e.phyrds - nvl(b.phyrds,0)), 0, 0, (sum(e.readtim - nvl(b.readtim,0)) / sum(e.phyrds  - nvl(b.phyrds,0)))*10) readtime, decode (sum(e.wait_count - nvl(b.wait_count, 0)), 0, 0, (sum(e.time - nvl(b.time,0)) / sum(e.wait_count - nvl(b.wait_count,0)))*10) busytime from stats$tempstatxs e, stats$tempstatxs b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.dbid(+) = e.dbid and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.instance_number(+) = e.instance_number and b.tsname(+) = e.tsname and b.filename(+) = e.filename and ((e.phyrds  - nvl(b.phyrds,0)) + (e.phywrts - nvl(b.phywrts,0))) > 0 group by e.tsname").fetchall()])
    captured['DBORAFIL']['data'].extend([dict(timestamp=e['snap_time'], tablespace=strs(r[0]),  file=strs(r[1]), reads=float(r[2]) / e['elapsed'], writes=float(r[3]) / e['elapsed'], busy=float(r[4]) / e['elapsed'], blocksperread=float(r[5]), readtime=float(r[6]) / e['elapsed'] / 1000000 , busytime=float(r[7]) / e['elapsed'] / 1000000) for r in oracle.execute("select e.tsname tablespace, e.filename filex, sum (e.phyrds - nvl(b.phyrds,0)) reads, sum (e.phywrts - nvl(b.phywrts,0)) writes, sum (e.wait_count - nvl(b.wait_count,0)) busy, decode( sum(e.phyrds - nvl(b.phyrds,0)), 0, 0, sum(e.phyblkrd - nvl(b.phyblkrd,0)) / sum(e.phyrds - nvl(b.phyrds,0))) blocksperread, decode( sum(e.phyrds - nvl(b.phyrds,0)), 0, 0, (sum(e.readtim - nvl(b.readtim,0)) / sum(e.phyrds  - nvl(b.phyrds,0)))*10) readtime, decode (sum(e.wait_count - nvl(b.wait_count, 0)), 0, 0, (sum(e.time - nvl(b.time,0)) / sum(e.wait_count - nvl(b.wait_count,0)))*10) busytime from stats$filestatxs e, stats$filestatxs b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.dbid(+) = e.dbid and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.instance_number(+) = e.instance_number and b.tsname(+) = e.tsname and b.filename(+) = e.filename and ( (e.phyrds - nvl(b.phyrds,0)) + (e.phywrts - nvl(b.phywrts,0))) > 0 group by e.tsname,e.filename union all select e.tsname tablespace, e.filename filex, sum (e.phyrds - nvl(b.phyrds,0)) reads, sum (e.phywrts - nvl(b.phywrts,0)) writes, sum (e.wait_count - nvl(b.wait_count,0)) busy, decode( sum(e.phyrds - nvl(b.phyrds,0)), 0, 0, sum(e.phyblkrd - nvl(b.phyblkrd,0)) / sum(e.phyrds - nvl(b.phyrds,0))) blocksperread, decode( sum(e.phyrds - nvl(b.phyrds,0)), 0, 0, (sum(e.readtim - nvl(b.readtim,0)) / sum(e.phyrds  - nvl(b.phyrds,0)))*10) readtime, decode (sum(e.wait_count - nvl(b.wait_count, 0)), 0, 0, (sum(e.time - nvl(b.time,0)) / sum(e.wait_count - nvl(b.wait_count,0)))*10) busytime from stats$tempstatxs e, stats$tempstatxs b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.dbid(+) = e.dbid and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.instance_number(+) = e.instance_number and b.tsname(+) = e.tsname and b.filename(+) = e.filename and ((e.phyrds  - nvl(b.phyrds,0)) + (e.phywrts - nvl(b.phywrts,0))) > 0 group by e.tsname, e.filename").fetchall()])
    captured['DBORAMDC']['data'].extend([dict(timestamp=e['snap_time'], component=strs(r[0]),  operation=strs(r[1]), size=float(r[2]) / 1048576, vmin=0.0, vmax=0.0, opcount=float(r[3]) / e['elapsed']) for r in oracle.execute("select replace(replace(replace(e.component, 'DEFAULT ', 'D:'), 'KEEP ', 'K:'), 'RECYCLE','R:') component, substr(e.last_oper_type,1,6) || decode(e.last_oper_type, 'STATIC', ' ', '/') || substr(e.last_oper_mode,1,3) operation, e.current_size sizex, e.oper_count - b.oper_count opcount from stats$memory_dynamic_comps b, stats$memory_dynamic_comps e where b.snap_id = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.dbid = e.dbid and b.instance_number = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.component = e.component and (e.current_size + b.current_size > 0 or e.oper_count - b.oper_count > 0)").fetchall()])
    captured['DBORABUF']['data'].extend([dict(timestamp=e['snap_time'], bufpool=strs(r[0]), gets=float(r[1]) / e['elapsed'], reads=float(r[2]) / e['elapsed'], writes=float(r[3]) / e['elapsed'], freewaits=float(r[4]) / e['elapsed'], writecompletewaits=float(r[5]) / e['elapsed'], busywaits=float(r[6]) / e['elapsed']) for r in oracle.execute("select replace(e.block_size/1024||'k', " + bs + "/1024||'k', substr(e.name,1,1)) name, e.db_block_gets - nvl(b.db_block_gets,0) + e.consistent_gets  - nvl(b.consistent_gets,0) gets, e.physical_reads - nvl(b.physical_reads,0) reads, e.physical_writes - nvl(b.physical_writes,0) writes, e.free_buffer_wait - nvl(b.free_buffer_wait,0) freewaits, e.write_complete_wait - nvl(b.write_complete_wait,0) writecompletewaits, e.buffer_busy_wait - nvl(b.buffer_busy_wait,0) busywaits from stats$buffer_pool_statistics b, stats$buffer_pool_statistics e where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.dbid(+) = e.dbid and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.instance_number(+) = e.instance_number and b.id(+) = e.id").fetchall()])
    captured['DBORAENQ']['data'].extend([dict(timestamp=e['snap_time'], enqueue=strs(r[0]), requests=float(r[1]) / e['elapsed'], succgets=float(r[2]) / e['elapsed'], failesgets=float(r[3]) / e['elapsed'], waits=float(r[4]) / e['elapsed'], avgwaitpersec=float(r[5]) * float(r[4]) / e['elapsed']) for r in oracle.execute("select e.eq_type || '-' || to_char(nvl(l.name,' ')) || decode( upper(e.req_reason), 'CONTENTION', null, '-',  null, ' ('||e.req_reason||')') enqueue, e.total_req# - nvl(b.total_req#,0) requests, e.succ_req# - nvl(b.succ_req#,0) succgets, e.failed_req# - nvl(b.failed_req#,0) failedgets, e.total_wait# - nvl(b.total_wait#,0) waits, decode(  (e.total_wait#   - nvl(b.total_wait#,0)), 0, to_number(0), ( (e.cum_wait_time - nvl(b.cum_wait_time,0)) / (e.total_wait#   - nvl(b.total_wait#,0)))) awttm from stats$enqueue_statistics e, stats$enqueue_statistics b, v$lock_type l where b.snap_id(+) = " + e['bid'] + " and e.snap_id  = " + e['eid'] + " and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.dbid(+) = e.dbid and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.instance_number(+) = e.instance_number and b.eq_type(+) = e.eq_type and b.req_reason(+) = e.req_reason and e.total_wait# - nvl(b.total_wait#,0) > 0 and l.type(+) = e.eq_type").fetchall()])
    captured['DBORALAW']['data'].extend([dict(timestamp=e['snap_time'], latch=strs(r[0]), wait=float(r[1]) / e['elapsed'] / 1000000) for r in oracle.execute("select b.name latch, (e.wait_time - b.wait_time) wait from  stats$latch b, stats$latch e where b.snap_id = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.dbid = e.dbid and b.instance_number = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.instance_number = e.instance_number and b.name = e.name and (e.gets - b.gets + e.immediate_gets - b.immediate_gets) > 0").fetchall()])
    captured['DBORALAT']['data'].extend([dict(timestamp=e['snap_time'], latch=strs(r[0]), gets=float(r[1]) / e['elapsed'], misses=float(r[2]) / e['elapsed'], sleeps=float(r[3]) / e['elapsed']) for r in oracle.execute("select b.name latch , e.gets - b.gets gets, e.misses - b.misses misses, e.sleeps - b.sleeps sleeps from stats$latch b, stats$latch e where b.snap_id = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and b.dbid = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.dbid = e.dbid and b.instance_number = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.instance_number = e.instance_number and b.name = e.name and e.sleeps - b.sleeps > 0").fetchall()])
    captured['DBORALIB']['data'].extend([dict(timestamp=e['snap_time'], item=strs(r[0]), gets=float(r[1]) / e['elapsed'], pins=float(r[2]) / e['elapsed'], reloads=float(r[3]) / e['elapsed'], invalidations=float(r[4]) / e['elapsed']) for r in oracle.execute("select e.namespace item, e.gets - b.gets gets, e.pins - b.pins pins, e.reloads - b.reloads reloads, e.invalidations - b.invalidations invalidations from stats$librarycache b, stats$librarycache e where b.snap_id = " + e['bid'] + " and e.snap_id = " + e['eid'] + " and e.dbid = " + e['dbid'] + " and b.dbid = e.dbid and e.instance_number = " + e['instance_number'] + " and b.instance_number = e.instance_number and b.namespace = e.namespace and e.gets - b.gets > 0").fetchall()])
    captured['DBORASGA']['data'].extend([dict(timestamp=e['snap_time'], pool=strs(r[0]), name=strs(r[1]), size=float(r[2])) for r in oracle.execute("select * from (select nvl(e.pool, b.pool) pool, nvl(e.name, b.name) name, e.bytes/1024/1024 sizex from (select * from stats$sgastat where snap_id = " + e['bid'] + " and dbid = " + e['dbid'] + " and instance_number = " + e['instance_number'] + ") b full outer join (select * from stats$sgastat where snap_id = " + e['eid'] + " and dbid = " + e['dbid'] + " and instance_number = " + e['instance_number'] + ") e on b.name = e.name and nvl(b.pool, 'a')  = nvl(e.pool, 'a')) where pool is null or name = 'free memory'").fetchall()])
    captured['DBORAPRM']['data'].extend([dict(timestamp=e['snap_time'], parameter=strs(r[0]), value=strs(r[1])) for r in oracle.execute("select e.name parameter, e.value value from stats$parameter e where e.snap_id(+) = " + e['eid'] + " and e.dbid(+) = " + e['dbid'] + " and e.instance_number(+) = " + e['instance_number'] + " and translate(e.name, '_', '#') not like '##%' and (nvl(e.isdefault, 'X') = 'FALSE' or nvl(e.ismodified,'X')  != 'FALSE')").fetchall()])
    captured['DBORASGLR']['data'].extend([dict(timestamp=e['snap_time'], owner=strs(r[0]), tablespace=strs(r[1]), object=strs(r[2]), subobject=strs(r[3]), objtype=strs(r[4]), gets=float(r[5]) / e['elapsed']) for r in oracle.execute("select n.owner owner, n.tablespace_name tablespace, n.object_name object, n.subobject_name subobject, n.object_type objtype, r.logical_reads gets from stats$seg_stat_obj n, (select * from (select e.dataobj#, e.obj#, e.ts#, e.dbid, e.logical_reads - nvl(b.logical_reads, 0) logical_reads from stats$seg_stat e, stats$seg_stat b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + "and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.ts#(+) = e.ts# and b.obj#(+) = e.obj# and b.dataobj#(+) = e.dataobj# and e.logical_reads - nvl(b.logical_reads, 0) > 0) d) r where n.dataobj# = r.dataobj# and n.obj# = r.obj# and n.ts# = r.ts# and n.dbid = r.dbid").fetchall()])
    captured['DBORASGPR']['data'].extend([dict(timestamp=e['snap_time'], owner=strs(r[0]), tablespace=strs(r[1]), object=strs(r[2]), subobject=strs(r[3]), objtype=strs(r[4]), reads=float(r[5]) / e['elapsed']) for r in oracle.execute("select n.owner owner, n.tablespace_name tablespace, n.object_name object, n.subobject_name subobject, n.object_type objtype, r.physical_reads reads from stats$seg_stat_obj n, (select * from (select e.dataobj#, e.obj#, e.ts#, e.dbid, e.physical_reads - nvl(b.physical_reads, 0) physical_reads from stats$seg_stat e, stats$seg_stat b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + "and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.ts#(+) = e.ts# and b.obj#(+) = e.obj# and b.dataobj#(+) = e.dataobj# and e.physical_reads - nvl(b.physical_reads, 0) > 0) d) r where n.dataobj# = r.dataobj# and n.obj# = r.obj# and n.ts# = r.ts# and n.dbid = r.dbid").fetchall()])
    captured['DBORASGRLW']['data'].extend([dict(timestamp=e['snap_time'], owner=strs(r[0]), tablespace=strs(r[1]), object=strs(r[2]), subobject=strs(r[3]), objtype=strs(r[4]), waits=float(r[5]) / e['elapsed']) for r in oracle.execute("select n.owner owner, n.tablespace_name tablespace, n.object_name object, n.subobject_name subobject, n.object_type objtype, r.row_lock_waits waits from stats$seg_stat_obj n, (select * from (select e.dataobj#, e.obj#, e.ts#, e.dbid, e.row_lock_waits - nvl(b.row_lock_waits, 0) row_lock_waits from stats$seg_stat e, stats$seg_stat b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + "and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.ts#(+) = e.ts# and b.obj#(+) = e.obj# and b.dataobj#(+) = e.dataobj# and e.row_lock_waits - nvl(b.row_lock_waits, 0) > 0) d) r where n.dataobj# = r.dataobj# and n.obj# = r.obj# and n.ts# = r.ts# and n.dbid = r.dbid").fetchall()])
    captured['DBORASGIW']['data'].extend([dict(timestamp=e['snap_time'], owner=strs(r[0]), tablespace=strs(r[1]), object=strs(r[2]), subobject=strs(r[3]), objtype=strs(r[4]), waits=float(r[5]) / e['elapsed']) for r in oracle.execute("select n.owner owner, n.tablespace_name tablespace, n.object_name object, n.subobject_name subobject, n.object_type objtype, r.itl_waits waits from stats$seg_stat_obj n, (select * from (select e.dataobj#, e.obj#, e.ts#, e.dbid, e.itl_waits - nvl(b.itl_waits, 0) itl_waits from stats$seg_stat e, stats$seg_stat b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + "and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.ts#(+) = e.ts# and b.obj#(+) = e.obj# and b.dataobj#(+) = e.dataobj# and e.itl_waits - nvl(b.itl_waits, 0) > 0) d) r where n.dataobj# = r.dataobj# and n.obj# = r.obj# and n.ts# = r.ts# and n.dbid = r.dbid").fetchall()])
    captured['DBORASGBBW']['data'].extend([dict(timestamp=e['snap_time'], owner=strs(r[0]), tablespace=strs(r[1]), object=strs(r[2]), subobject=strs(r[3]), objtype=strs(r[4]), waits=float(r[5]) / e['elapsed']) for r in oracle.execute("select n.owner owner, n.tablespace_name tablespace, n.object_name object, n.subobject_name subobject, n.object_type objtype, r.buffer_busy_waits waits from stats$seg_stat_obj n, (select * from (select e.dataobj#, e.obj#, e.ts#, e.dbid, e.buffer_busy_waits - nvl(b.buffer_busy_waits, 0) buffer_busy_waits from stats$seg_stat e, stats$seg_stat b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + "and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.ts#(+) = e.ts# and b.obj#(+) = e.obj# and b.dataobj#(+) = e.dataobj# and e.buffer_busy_waits - nvl(b.buffer_busy_waits, 0) > 0) d) r where n.dataobj# = r.dataobj# and n.obj# = r.obj# and n.ts# = r.ts# and n.dbid = r.dbid").fetchall()])
    captured['DBORASGGCBB']['data'].extend([dict(timestamp=e['snap_time'], owner=strs(r[0]), tablespace=strs(r[1]), object=strs(r[2]), subobject=strs(r[3]), objtype=strs(r[4]), waits=float(r[5]) / e['elapsed']) for r in oracle.execute("select n.owner owner, n.tablespace_name tablespace, n.object_name object, n.subobject_name subobject, n.object_type objtype, r.gc_buffer_busy waits from stats$seg_stat_obj n, (select * from (select e.dataobj#, e.obj#, e.ts#, e.dbid, e.gc_buffer_busy - nvl(b.gc_buffer_busy, 0) gc_buffer_busy from stats$seg_stat e, stats$seg_stat b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + "and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.ts#(+) = e.ts# and b.obj#(+) = e.obj# and b.dataobj#(+) = e.dataobj# and e.gc_buffer_busy - nvl(b.gc_buffer_busy, 0) > 0) d) r where n.dataobj# = r.dataobj# and n.obj# = r.obj# and n.ts# = r.ts# and n.dbid = r.dbid").fetchall()])
    captured['DBORASGCRBR']['data'].extend([dict(timestamp=e['snap_time'], owner=strs(r[0]), tablespace=strs(r[1]), object=strs(r[2]), subobject=strs(r[3]), objtype=strs(r[4]), blocks=float(r[5]) / e['elapsed']) for r in oracle.execute("select n.owner owner, n.tablespace_name tablespace, n.object_name object, n.subobject_name subobject, n.object_type objtype, r.gc_cr_blocks_received blocks from stats$seg_stat_obj n, (select * from (select e.dataobj#, e.obj#, e.ts#, e.dbid, e.gc_cr_blocks_received - nvl(b.gc_cr_blocks_received, 0) gc_cr_blocks_received from stats$seg_stat e, stats$seg_stat b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + "and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.ts#(+) = e.ts# and b.obj#(+) = e.obj# and b.dataobj#(+) = e.dataobj# and e.gc_cr_blocks_received - nvl(b.gc_cr_blocks_received, 0) > 0) d) r where n.dataobj# = r.dataobj# and n.obj# = r.obj# and n.ts# = r.ts# and n.dbid = r.dbid").fetchall()])
    captured['DBORASGCBR']['data'].extend([dict(timestamp=e['snap_time'], owner=strs(r[0]), tablespace=strs(r[1]), object=strs(r[2]), subobject=strs(r[3]), objtype=strs(r[4]), blocks=float(r[5]) / e['elapsed']) for r in oracle.execute("select n.owner owner, n.tablespace_name tablespace, n.object_name object, n.subobject_name subobject, n.object_type objtype, r.gc_current_blocks_received blocks from stats$seg_stat_obj n, (select * from (select e.dataobj#, e.obj#, e.ts#, e.dbid, e.gc_current_blocks_received - nvl(b.gc_current_blocks_received, 0) gc_current_blocks_received from stats$seg_stat e, stats$seg_stat b where b.snap_id(+) = " + e['bid'] + " and e.snap_id = " + e['eid'] + "and b.dbid(+) = " + e['dbid'] + " and e.dbid = " + e['dbid'] + " and b.instance_number(+) = " + e['instance_number'] + " and e.instance_number = " + e['instance_number'] + " and b.ts#(+) = e.ts# and b.obj#(+) = e.obj# and b.dataobj#(+) = e.dataobj# and e.gc_current_blocks_received - nvl(b.gc_current_blocks_received, 0) > 0) d) r where n.dataobj# = r.dataobj# and n.obj# = r.obj# and n.ts# = r.ts# and n.dbid = r.dbid").fetchall()])
    captured['DBORAPGA']['data'].extend([dict(timestamp=e['snap_time'], aggrtarget=float(r[0]), autotarget=float(r[1]), memalloc=float(r[2]), memused=float(r[3])) for r in oracle.execute("select to_number(p.value)/1024/1024 aggrtarget, mu.pat/1024/1024 autotarget, mu.PGA_alloc/1024/1024 memalloc, (mu.PGA_used_auto + mu.PGA_used_man)/1024/1024 memused from (select sum(case when name = 'total PGA allocated' then value else 0 end) PGA_alloc, sum(case when name = 'total PGA used for auto workareas' then value else 0 end) PGA_used_auto, sum(case when name = 'total PGA used for manual workareas' then value else 0 end) PGA_used_man, sum(case when name = 'global memory bound' then value else 0 end) glob_mem_bnd, sum(case when name = 'aggregate PGA auto target' then value else 0 end) pat from stats$pgastat pga where pga.snap_id = " + e['eid'] + " and pga.dbid = " + e['dbid'] + " and pga.instance_number = " + e['instance_number'] + ") mu, stats$parameter p where p.snap_id = " + e['eid'] + " and p.dbid = " + e['dbid'] + " and p.instance_number = " + e['instance_number'] + " and p.name = 'pga_aggregate_target' and p.value  != '0'").fetchall()])
    captured['DBORAPGC']['data'].extend([dict(timestamp=e['snap_time'], highoptimal=strs(r[0]), totexecs=float(r[1]) / e['elapsed'], execs0=float(r[2]) / e['elapsed'], execs1=float(r[3]) / e['elapsed'], execs2=float(r[4]) / e['elapsed']) for r in oracle.execute("select case when e.high_optimal_size >= 1024*1024*1024*1024 then lpad(round(e.high_optimal_size/1024/1024/1024/1024) || 'T',7) when e.high_optimal_size >= 1024*1024*1024 then lpad(round(e.high_optimal_size/1024/1024/1024) || 'G',7) when e.high_optimal_size >= 1024*1024 then lpad(round(e.high_optimal_size/1024/1024) || 'M',7) when e.high_optimal_size >= 1024 then lpad(round(e.high_optimal_size/1024) || 'K',7) else e.high_optimal_size || 'B' end highoptimal, e.total_executions - nvl(b.total_executions,0) totexecs, e.optimal_executions - nvl(b.optimal_executions,0) execs0, e.onepass_executions - nvl(b.onepass_executions,0) execs1, e.multipasses_executions - nvl(b.multipasses_executions,0) execs2 from stats$sql_workarea_histogram e, stats$sql_workarea_histogram b where e.snap_id = " + e['eid'] + " and e.dbid = " + e['dbid'] + " and e.instance_number = " + e['instance_number'] + " and b.snap_id(+) = " + e['bid'] + " and b.dbid(+) = e.dbid and b.instance_number(+) = e.instance_number and b.low_optimal_size(+) = e.low_optimal_size and b.high_optimal_size(+) = e.high_optimal_size and e.total_executions  - nvl(b.total_executions,0) > 0").fetchall()])
    captured['DBORABPA']['data'].extend([dict(timestamp=e['snap_time'], bufpool=strs(r[0]), sizefactor=strs(r[1]), estphysreadsfactor=float(r[2])) for r in oracle.execute("select name bufpool, size_factor sizefactor, estd_physical_read_factor estphysreadsfactor from stats$db_cache_advice where snap_id = " + e['eid'] + " and dbid = " + e['dbid'] + " and instance_number = " + e['instance_number'] + " and estd_physical_reads > 0").fetchall()])
    captured['DBORAPMA']['data'].extend([dict(timestamp=e['snap_time'], sizefactor=strs(r[0]), estextrabytesrw=float(r[1]), estoveralloc=float(r[2])) for r in oracle.execute("select pga_target_factor sizefactor, estd_extra_bytes_rw  byt_rw, estd_overalloc_count eoc from stats$pga_target_advice e where snap_id = " + e['eid'] + " and dbid = " + e['dbid'] + " and instance_number = " + e['instance_number']).fetchall()])
    captured['DBORASPA']['data'].extend([dict(timestamp=e['snap_time'], sizefactor=strs(r[0]), estloadtimefctr=float(r[1])) for r in oracle.execute("select shared_pool_size_factor sizefactor, estd_lc_load_time_factor elcltf from stats$shared_pool_advice where snap_id = " + e['eid'] + " and dbid = " + e['dbid'] + " and instance_number = " + e['instance_number']).fetchall()])
    captured['DBORASGAA']['data'].extend([dict(timestamp=e['snap_time'], sizefactor=strs(r[0]), estphysicalreads=float(r[1])) for r in oracle.execute("select sga_size_factor sizefactor, estd_physical_reads epr from stats$sga_target_advice where snap_id = " + e['eid'] + " and dbid = " + e['dbid'] + " and instance_number = " + e['instance_number']).fetchall()])
if parameters[PBAS.target]: 
  captured['ORAHAS']['data'].extend([dict(timestamp=strs(r[0]), kairos_count=1, sql_id=strs(r[1]), sample_id=strs(r[2]), session_id=strs(r[3]), session_serial=strs(r[4]), user_id=strs(r[5]), sql_child_number=strs(r[6]), sql_plan_hash_value=strs(r[7]), force_matching_signature=strs(r[8]), sql_opcode=strs(r[9]), service_hash=strs(r[10]), session_type=strs(r[11]), session_state=strs(r[12]), qc_session_id=strs(r[13]), qc_instance_id=strs(r[14]), blocking_session=strs(r[15]), blocking_session_status=strs(r[16]), blocking_session_serial=strs(r[17]), event=strs(r[18]), event_id=strs(r[19]), seq=strs(r[20]), p1=strs(r[21]), p1text=strs(r[22]), p2=strs(r[23]), p2text=strs(r[24]), p3=strs(r[25]), p3text=strs(r[26]), wait_class=strs(r[27]), wait_class_id=strs(r[28]), wait_time=float(r[29]), time_waited=float(r[30]), xid=strs(r[31]), current_obj=strs(r[32]), current_file=strs(r[33]), current_block=strs(r[34]), program=strs(r[35]), module=strs(r[36]), action=strs(r[37]), client_id=strs(r[38]), blocking_hangchain_info=strs(r[39]), blocking_inst_id=strs(r[40]), capture_overhead=strs(r[41]), consumer_group_id=strs(r[42]), current_row=strs(r[43]), delta_interconnect_io_bytes=float(r[44]), delta_read_io_bytes=float(r[45]), delta_read_io_requests=float(r[46]), delta_time=float(r[47]), delta_write_io_bytes=float(r[48]), delta_write_io_requests=float(r[49]), ecid=strs(r[50]), flags=strs(r[51]), in_bind=strs(r[52]), in_connection_mgmt=strs(r[53]), in_cursor_close=strs(r[54]), in_hard_parse=strs(r[55]), in_java_execution=strs(r[56]), in_parse=strs(r[57]), in_plsql_compilation=strs(r[58]), in_plsql_execution=strs(r[59]), in_plsql_rpc=strs(r[60]), in_sequence_load=strs(r[61]), in_sql_execution=strs(r[62]), is_captured=strs(r[63]), is_replayed=strs(r[64]), is_sqlid_current=strs(r[65]), machine=strs(r[66]), pga_allocated=float(r[67]), plsql_entry_object_id=strs(r[68]), plsql_entry_subprogram_id=strs(r[69]), plsql_object_id=strs(r[70]), plsql_subprogram_id=strs(r[71]), port=strs(r[72]), qc_session_serial=strs(r[73]), remote_instance=strs(r[74]), replay_overhead=strs(r[75]), sql_exec_id=strs(r[76]), sql_exec_start=strs(r[77]), sql_opname=strs(r[78]), sql_plan_line_id=strs(r[79]), sql_plan_operation=strs(r[80]), sql_plan_options=strs(r[81]), temp_space_allocated=float(r[82]), time_model=strs(r[83]), tm_delta_cpu_time=float(r[84]), tm_delta_db_time=float(r[85]), tm_delta_time=float(r[86]), top_level_call=strs(r[87]), top_level_call_name=strs(r[88]), top_level_sql_id=strs(r[89]), top_level_sql_opcode=strs(r[90]), dbreplay_file_id=strs(r[91]), dbreplay_call_counter=strs(r[92])) for r in oracle.execute("select to_char(sample_time, 'YYYYMMDDHH24MISS')||'000' timepstamp, sql_id, sample_id, session_id, session_serial#, user_id, sql_child_number, sql_plan_hash_value, force_matching_signature, sql_opcode, service_hash, decode(session_type, 'USER', 'FOREGROUND', session_type), session_state, qc_session_id, qc_instance_id, blocking_session, blocking_session_status, blocking_session_serial#, event, event_id, seq#, p1, p1text, p2, p2text, p3, p3text, wait_class, wait_class_id, nvl(wait_time,0), nvl(time_waited,0), rawtohex(xid), current_obj#, current_file#, current_block#, program, module, action, client_id, blocking_hangchain_info, blocking_inst_id, capture_overhead, consumer_group_id, current_row#, nvl(delta_interconnect_io_bytes,0), nvl(delta_read_io_bytes,0), nvl(delta_read_io_requests,0), nvl(delta_time,0), nvl(delta_write_io_bytes,0), nvl(delta_write_io_requests,0), ecid, flags, in_bind, in_connection_mgmt, in_cursor_close, in_hard_parse, in_java_execution, in_parse, in_plsql_compilation, in_plsql_execution, in_plsql_rpc, in_sequence_load, in_sql_execution, is_captured, is_replayed, is_sqlid_current, machine, nvl(pga_allocated,0), plsql_entry_object_id, plsql_entry_subprogram_id, plsql_object_id, plsql_subprogram_id, port, qc_session_serial#, remote_instance#, replay_overhead, sql_exec_id, to_char(sql_exec_start, 'YYYYMMDDHH24MISS'), sql_opname, sql_plan_line_id, sql_plan_operation, sql_plan_options, nvl(temp_space_allocated,0), time_model, nvl(tm_delta_cpu_time,0), nvl(tm_delta_db_time,0), nvl(tm_delta_time,0), top_level_call#, top_level_call_name, top_level_sql_id, top_level_sql_opcode, dbreplay_file_id, dbreplay_call_counter from bash$hist_active_sess_history sq where sq.instance_number=" + e['instance_number'] + " and to_char(sq.sample_time, 'YYYYMMDDHH24MISS') between '" + parameters[PFRM.target] + "' and '" + parameters[PTO.target] + "'").fetchall()])
for e in captured:
  print('Writing: ' + e + '...')
  zipf.writestr(e, json.dumps(captured[e], indent=4, sort_keys=True))
oracle.execute("drop function get_statspack_number")
oracle.execute("drop function get_statspack_varchar")
oracle.execute("drop table stats$tmp_sqlstats")
zipf.close()
print('File ' + zipname + ' has been written!')