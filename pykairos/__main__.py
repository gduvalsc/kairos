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
import argparse, pykairos, logging, os, multiprocessing, signal, subprocess, time
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
parser.add_argument('--version', action='version', version='KAIROS V3.2')
parser.add_argument('--launcher', action='store_true', dest='launcher', help='The launcher is requested to start')
parser.add_argument('--notifier', action='store_true', dest='notifier', help='A notifier is requested to start')
parser.add_argument('--bootstrap', action='store_true', dest='bootstrap', help='Bootstraping the system')
args = parser.parse_args()
logging.basicConfig(format='%(asctime)s %(process)5s %(levelname)8s %(message)s', level=logging.INFO, filename="/var/log/kairos/kairos.log")
if args.notifier:
    n = pykairos.KairosNotifier()
if args.launcher:
    logging.info('This system is configured with ' + str(multiprocessing.cpu_count()) + ' cpus.')
    import setproctitle
    setproctitle.setproctitle('KairosMain')
    logging.info('Process name: ' + setproctitle.getproctitle())
    logging.info('Process id: ' + str(os.getpid()))
    workers = multiprocessing.cpu_count() + 1
    workers = 1
    gunicorn = ['gunicorn']
    gunicorn.extend(['-b', '0.0.0.0:443'])
    gunicorn.extend(['-k', 'aiohttp.worker.GunicornWebWorker'])
    gunicorn.extend(['-t0'])
    gunicorn.extend(['-p', '/var/log/gunicorn.pid'])
    gunicorn.extend(['-w', str(workers)])
    gunicorn.extend(['--keyfile', '/kairos/kairos.key'])
    gunicorn.extend(['--certfile', '/kairos/kairos.crt'])
    gunicorn.extend(['--access-logfile', '/var/log/kairos/webserver.log'])
    gunicorn.extend(['--log-file', '/var/log/kairos/webserver.log'])
    gunicorn.extend(['--chdir', '/kairos'])
    gunicorn.extend(['worker'])
    notifier = ['python3']
    notifier.extend(['-m', 'pykairos', '--notifier'])
    os.system('rm -fr /var/log/gunicorn.pid')
    catchrun(gunicorn, notifier)
if args.bootstrap:
    print('O', end='', flush=True)
    odb = subprocess.run(['/etc/init.d/orientdb', 'start'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if  odb.returncode:
        logging.error("Error during startup of Orientdb!")
        exit(1)
    logging.info("Orientdb startup has been initiated!")
    print('K', end='', flush=True)
    kairos = subprocess.run(['daemonmgr', '--daemon', 'kairosd', '-start'])
    if  kairos.returncode:
        logging.error("Error during startup of Kairos")
        exit(1)
    logging.info("Kairos startup has been initiated!")
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
    obj = subprocess.run(['kairos', '-s', 'listobjects', '-a', 'kairos', '-p', 'root', '--nodesdb', 'kairos_system_system', '--systemdb', 'kairos_system_system'], stdout=subprocess.PIPE)
    lines = obj.stdout.decode().split('\n')
    if len(lines) - 1 == 0:
        logging.info("Loading system database...")
        objects = []
        objects.extend(glob('/tmp/objects/*/*.py'))
        objects.extend(glob('/tmp/objects/*/*.jpg'))
        for o in objects:
            print('l', end='', flush=True)
            logging.info('Loading ' + o + " ...")
            p = subprocess.run(['kairos', '-s', 'uploadobject', '-a', 'kairos', '-p', 'root', '--nodesdb', 'kairos_system_system', '--file', o])
            if p.returncode: logging.error('Error during loading of: ' + o)
        print('', flush=True)
        logging.info(str(len(objects)) + ' found objects in /tmp/objects!')
        obj = subprocess.run(['kairos', '-s', 'listobjects', '-a', 'kairos', '-p', 'root', '--nodesdb', 'kairos_system_system', '--systemdb', 'kairos_system_system'], stdout=subprocess.PIPE)
        lines = obj.stdout.decode().split('\n')
        logging.info("System database has " + str(int((len(lines) - 1) / 2)) + " objects.")
        try:
            assert len(objects) == int((len(lines) - 1) / 2)
        except:
             subprocess.run(['cat', '/var/log/kairos/kairos.log'])
             subprocess.run(['cat', '/var/log/kairos/webserver.log'])
             raise
        subprocess.run(['rm', '-fr', '/tmp/objects'])
        subprocess.run(['mkdir', '/orientdb/exports'])
        subprocess.run(['orientdb', "connect remote:localhost/kairos_system_system kairos root; export database /orientdb/exports/system"])
    catchrun(['bash'])
