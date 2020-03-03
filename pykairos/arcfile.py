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

import multiprocessing, zipfile, tarfile

class Arcfile:
    def __init__(s,file,mode='r'):
        s.lock = multiprocessing.Lock()
        opmode=mode.split(':')
        s.type='unknown'
        if opmode[0] in ['r','a']:
            if zipfile.is_zipfile(file):
                s.archive=zipfile.ZipFile(file,mode)
                s.type='zipfile'
            else:
                file.seek(0)
                try:
                    s.archive=tarfile.open(fileobj=file)
                    s.type='tarfile'
                except:
                    logging.error('Unknown file type')
        else:
            if len(opmode)>1 and opmode[1] in ['zip']:
                s.type='zipfile'
                s.archive=zipfile.ZipFile(file,opmode[0],zipfile.ZIP_DEFLATED)
            else: s.archive=tarfile.open(name='stream', mode='w+b', fileobj=file)
    def close(s):
        return s.archive.close()
    def list(s):
        if s.type=='tarfile': return s.archive.getnames()
        else: return s.archive.namelist()
    def read(s,member):
        s.lock.acquire()
        if s.type=='tarfile':
            try: 
                r = bz2.decompress(s.archive.extractfile(s.archive.getmember(member).name).read())
            except: 
                r = s.archive.extractfile(s.archive.getmember(member).name).read()
        else:
            try: 
                r = bz2.decompress(s.archive.read(member))
            except: 
                r = s.archive.read(member)
        s.lock.release()
        return r
    def write(s,member,stream):
        if s.type=='tarfile':
            inf=tarfile.TarInfo()
            inf.name=member
            inf.size=len(stream)
            inf.mtime = time.time()
            return s.archive.addfile(inf,StringIO.StringIO(stream))
        else: return s.archive.writestr(member,stream)