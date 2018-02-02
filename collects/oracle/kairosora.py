import json, argparse, zipfile, os, socket
from com.ziclix.python.sql import zxJDBC

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

PHST = Parameter('--host', 'host')
PPRT = Parameter('--port', 'port')
PSRV = Parameter('--service', 'service')
PUSR = Parameter('--user', 'user')
PPWD = Parameter('--password', 'password')
PLVL = Parameter('--level', 'level')
PAWR = Parameter('--awr', 'awr')
PFRM = Parameter('--from', 'from')
PTO = Parameter('--to', 'to')
PYES = Parameter('--yesterday', 'yesterday')

def get_parameters(parser, args):
    mandatory = [PHST, PPRT, PSRV, PAWR, PUSR, PPWD]
    if vars(args)[PAWR.target]: mandatory.extend([PLVL])
    vars(args)[PHST.target] = socket.gethostname() if vars(args)[PHST.target] == None else vars(args)[PHST.target]
    vars(args)[PSRV.target] = os.environ['ORACLE_SID'] if vars(args)[PSRV.target] == None and 'ORACLE_SID' in os.environ else vars(args)[PHST.target]
    
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
parser.add_argument(PLVL.name, action = 'store', dest=PLVL.target, default='1', help='Level 1: Extract AWR, level 2: Detailed info on requests, level 3: ASH')
parser.add_argument(PYES.name, action = 'store_true', dest=PYES.target, default=False, help='Extract data generated yesterday')
parser.add_argument(PFRM.name, action = 'store', dest=PFRM.target, help='Extract data generated from this date')
parser.add_argument(PTO.name, action = 'store', dest=PTO.target, help='Extract data generated until this date plus one day')
args = parser.parse_args()
parameters = get_parameters(parser, args)
oracle = Oracle("jdbc:oracle:thin:@" + parameters['host'] + ":" + parameters['port'] + ":" + parameters['service'], parameters['user'], parameters['password'], "oracle.jdbc.driver.OracleDriver")
pprint(oracle.execute("select object_name from user_objects"))
