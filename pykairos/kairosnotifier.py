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

import multiprocessing, logging, os, pyinotify

class KairosNotifier:
    def __init__(s):
        logging.info('Init notification process...')
        s.wm = pyinotify.WatchManager()
        s.wm.add_watch('/autoupload', pyinotify.ALL_EVENTS)
        logging.info('Watching directory: /autoupload ...')
        for d in os.listdir('/autoupload'):
            wdir = '/autoupload/' + d
            if 'kairos_' in d and os.path.isdir(wdir):
                logging.info('Watching directory: ' + wdir + ' ...')
                s.wm.add_watch(wdir, pyinotify.ALL_EVENTS)
                for f in os.listdir(wdir): os.system('touch ' + wdir + '/' +f)
        s.eh = NotifyEventHandler()
        s.eh.wm = s.wm
        s.notifier = pyinotify.Notifier(s.wm, s.eh)
        import setproctitle
        multiprocessing.current_process().name = 'NotifyProcess'
        logging.info('Starting notification process...')
        setproctitle.setproctitle('KairosNotifier')
        logging.info('Process name: ' + setproctitle.getproctitle())
        logging.info('Process id: ' + str(os.getpid()))
        s.notifier.loop()


class NotifyEventHandler(pyinotify.ProcessEvent):
    def process_default(s, event):
        logging.debug('from process_default: ' + str(event))
    def process_IN_CREATE(s, event):
        if event.path == '/autoupload' and event.maskname == 'IN_CREATE|IN_ISDIR' and event.dir:
            logging.info('Watching a new directory: ' + event.pathname + ' ...')
            s.wm.add_watch(event.pathname, pyinotify.ALL_EVENTS)
    def process_IN_MODIFY(s, event):
        if 'kairos_' in event.path and not event.dir and os.path.isfile(event.pathname):
            if os.path.basename(event.pathname)[0] != '.':
                logging.info("Uploading file '" + event.pathname + "' into database " + os.path.basename(event.path) + " ...")
                status = os.system('kairos -s uploadnode --systemdb kairos_system_system --nodesdb ' + os.path.basename(event.path) + ' --id 1 --file ' + event.pathname)
                if status == 0: os.remove(event.pathname)
                logging.info("File '" + event.pathname + "' has been uploaded to " + os.path.basename(event.path) + "!")
    def process_IN_ATTRIB(s, event):
        s.process_IN_MODIFY(event)

