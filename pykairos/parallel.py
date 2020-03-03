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

import multiprocessing

class Parallel:
    def __init__(s, action, workers=multiprocessing.cpu_count()):
        s.limit = int(workers)
        s.workers = dict()
        s.action = action
    def push(s, arg):
        if len(s.workers.keys()) < s.limit:
            p = multiprocessing.Process(target=s.action, args=(arg,))
            p.start()
            s.workers[p.sentinel] = p
        else:
            if len(s.workers.keys()) == s.limit:
                x = multiprocessing.connection.wait(s.workers.keys())
                for e in x:
                    s.workers[e].join()
                    del s.workers[e]
                p = multiprocessing.Process(target=s.action, args=(arg,))
                p.start()
                s.workers[p.sentinel] = p
    def join(s):
        while len(s.workers):
            x = multiprocessing.connection.wait(s.workers.keys())
            for e in x:
                s.workers[e].join()
                del s.workers[e]
