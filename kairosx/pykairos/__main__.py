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
import argparse, pykairos, logging, os, multiprocessing, signal, subprocess, time, json
from pykairos.kairosnotifier import KairosNotifier
from glob import glob

def catchrun(*c):
    import signal, time, subprocess, os
    v = dict(stop = False, processes=[])
    def handler(signum, stack):
        v['stop'] = True
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)
    for x in c: v['processes'].append(subprocess.Popen(x))
    while True:
        for p in v['processes']:
            if p.poll() != None: v['stop'] = True
        if v['stop']: break
        time.sleep(1)
    for p in v['processes']:
        if p.poll() == None: p.send_signal(signal.SIGTERM)
        p.wait()

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='KAIROS V8.1')
parser.add_argument('--launcher', action='store_true', dest='launcher', help='The launcher is requested to start')
parser.add_argument('--monoprocess', action='store_true', dest='monoprocess', help='Only one subprocess required')
parser.add_argument('--notifier', action='store_true', dest='notifier', help='A notifier is requested to start')
parser.add_argument('--bootstrap', action='store_true', dest='bootstrap', help='Bootstraping the system')
parser.add_argument('--makeboot', action='store_true', dest='makeboot', help='Create boostrap data')
args = parser.parse_args()
logging.basicConfig(format='%(asctime)s %(process)5s %(levelname)8s %(message)s', level=logging.TRACE, filename="/var/log/kairos/kairos.log")
if args.notifier:
    n = KairosNotifier()
if args.launcher:
    logging.info(f'This system is configured with {multiprocessing.cpu_count()} cpus.')
    import setproctitle
    setproctitle.setproctitle('KairosMain')
    logging.info(f'Process name: {setproctitle.getproctitle()}')
    logging.info(f'Process id: {os.getpid()}')
    workers = 1 if args.monoprocess else multiprocessing.cpu_count() + 1
    gunicorn = ['gunicorn']
    gunicorn.extend(['-b', '0.0.0.0:443'])
    gunicorn.extend(['-k', 'aiohttp.worker.GunicornWebWorker'])
    gunicorn.extend(['-t0'])
    gunicorn.extend(['-p', '/var/log/gunicorn.pid'])
    gunicorn.extend(['-w', str(workers)])
    gunicorn.extend(['--keyfile', '/kairosx/kairos.key'])
    gunicorn.extend(['--certfile', '/kairosx/kairos.crt'])
    gunicorn.extend(['--access-logfile', '/var/log/kairos/webserver.log'])
    gunicorn.extend(['--log-file', '/var/log/kairos/webserver.log'])
    gunicorn.extend(['--chdir', '/kairosx'])
    gunicorn.extend(['worker'])
    notifier = ['python3']
    notifier.extend(['-m', 'pykairos', '--notifier'])
    os.system('rm -fr /var/log/gunicorn.pid')
    catchrun(gunicorn, notifier)

if args.bootstrap:
    os.system('/usr/sbin/crond')
    if len(os.listdir('/postgres/data')) == 0: os.system('cd /postgres; tar xvf /postgres/backups/pgboot.tar; chmod 700 /postgres/data')
    os.system('su - postgres -c "pg_ctl -D /postgres/data start"')
    os.system("python3 -m pykairos --launcher")
    
if args.makeboot:
    command = 'su - postgres -c "pg_ctl stop"'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    command = 'rm -fr  /postgres/boot; mkdir /postgres/boot; mkdir /postgres/boot/data; chown -R postgres:postgres /postgres/boot'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    command = 'su - postgres -c "initdb -D /postgres/boot/data -E UTF8 --no-locale"'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    command = 'su - postgres -c "pg_ctl -D /postgres/boot/data start"'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    command = 'su - postgres -c "echo ''local all postgres trust'' > /postgres/boot/data/pg_hba.conf"'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    command = 'su - postgres -c "echo ''host all postgres all trust'' >> /postgres/boot/data/pg_hba.conf"'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    command = 'su - postgres -c "echo ''host all all all md5'' >> /postgres/boot/data/pg_hba.conf"'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    command = 'su - postgres -c "echo ''log_min_duration_statement = -1'' >> /postgres/boot/data/postgresql.conf"'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    print('S', end='', flush=True)
    logging.info("Creating system database...")
    while True:
        print('s', end='', flush=True)
        logging.info("Trying to create system database...")
        time.sleep(1)
        crs = subprocess.run(['kairos', '-s', 'createsystem'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if not crs.returncode: break
    logging.info("System database created!")
    print('L', end='', flush=True)
    logging.info("Loading system database...")
    objects = []
    objects.extend(glob('/tmp/objects/*/*.py'))
    objects.extend(glob('/tmp/objects/*/*.jpg'))
    for o in objects:
       print('l', end='', flush=True)
       logging.info('Loading ' + o + " ...")
       try: 
           result = json.loads(subprocess.getoutput(f"kairos -s uploadobject --nodesdb kairos_system_system --file '{o}'"))
           success = result['success']
           if not success: logging.error(f'Error during loading of: {o}')
           else: logging.info(json.dumps(result))
       except:
           logging.error(f'Error during loading of: {o}')
           subprocess.run(['cat', '/var/log/kairos/kairos.log'])
           raise
    print('', flush=True)
    logging.info(f'{len(objects)} found objects in /tmp/objects!')
    data = json.loads(subprocess.getoutput('kairos -s listobjects --nodesdb kairos_system_system --systemdb kairos_system_system'))['data']
    logging.info(f"System database has {int((len(data)) / 2)} objects.")
    try:
        assert len(objects) == int(len(data) / 2)
    except:
        subprocess.run(['cat', '/var/log/kairos/kairos.log'])
        subprocess.run(['cat', '/var/log/kairos/webserver.log'])
        raise
    subprocess.run(['rm', '-fr', '/tmp/objects'])
    command = 'su - postgres -c "pg_ctl -D /postgres/boot/data stop"'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    command = 'cd /postgres/boot; rm -fr /postgres/backups/*; tar cvf /postgres/backups/pgboot.tar data'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
    command = 'rm -fr /postgres/boot'
    os.system('echo ' + "===============================================")
    os.system('echo ' + command)
    os.system(command)
