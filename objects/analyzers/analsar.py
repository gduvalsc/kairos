class UserObject(dict):
    def __init__(s):
        object = {
            "type": "analyzer",
            "id": "ANALSAR",
            "begin": s.begin,
            "end": s.end,
            "rules": [
                {"action": s.asarx, "regexp": '([0-9]+)\/([0-9]+)\/([0-9]+).*$'},
                {"action": s.genstate(''), "regexp": '^Average.*$'},
            ],
            "contextrules": [
                {"action": s.asarb0x, "regexp": '^(..):(..):(..) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?)[ \t]+(.+?)[ \t]+(.+?)$', "context": "sarb0", "scope": "SARB"},
                {"action": s.asarb1x, "regexp": '^(..):(..):(..) (  |PM|AM) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "sarb1", "scope": "SARB"},
                {"action": s.asard0x, "regexp": '^$|^(..):(..):(..) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?)$|^ +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "sard0", "scope": "SARD"},
                {"action": s.asard1x, "regexp": '^(..):(..):(..) +(.+?) +([0-9]+.*?) +([0-9]+.*)$', "context": "sard1", "scope": "SARD"},
                {"action": s.asard2x, "regexp": '(..):(..):(..) (  |PM|AM) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "sard2", "scope": "SARD"},
                {"action": s.asarn0x, "regexp": '(..):(..):(..) (  |PM|AM) +(.+?) +(\d+\.\d+) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "sarn0", "scope": "SARN"},
                {"action": s.asarp0x, "regexp": '^(..):(..):(..) (  |PM|AM) +(.+?) +(.+?)', "context": "sarp0", "scope": "SARP"},
                {"action": s.asarq0x, "regexp": '^(..):(..):(..) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "sarq0", "scope": "SARQ"},
                {"action": s.asarq1x, "regexp": '^(..):(..):(..) (  |PM|AM) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "sarq1", "scope": "SARQ"},
                {"action": s.asarm0x, "regexp": '(..):(..):(..) +(.+?) +(.+?)$', "context": "sarm0", "scope": "SARQ"},
                {"action": s.asarm1x, "regexp": '(..):(..):(..) (  |AM|PM) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "sarm1", "scope": "SARQ"},
                {"action": s.asaru0x, "regexp": '(..):(..):(..) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "saru0", "scope": "SARU"},
                {"action": s.asaru1x, "regexp": '(..):(..):(..) (  |PM|AM) +(all|[0-9]+) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "saru1", "scope": "SARU"},
                {"action": s.asaru2x, "regexp": '(..):(..):(..) (  |PM|AM) +(all|[0-9]+) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?)$', "context": "saru2", "scope": "SARU"},
                {"action": s.asaru3x, "regexp": '(..):(..):(..) +(.+?) +(.+?) +(.+?) +(.+?) +([0-9]+\.[0-9][0-9])', "context": "saru3", "scope": "SARU"},
                {"action": s.asarv0x, "regexp": '^(..):(..):(..).*? +([0-9]+)\/.*$', "context": "sarv0", "scope": "SARV"},
                {"action": s.asarw0x, "regexp": '^(..):(..):(..) +(.+?) +(.+?)$', "context": "sarw0", "scope": "SARW"},
            ],
            "outcontextrules": [
                {"action": s.genstate("sarb0"), "regexp": '^.*bread.*lread.*bwrit.*lwrit.*pread.*pwrit', "scope": "SARB"},
                {"action": s.genstate("sarb1"), "regexp": '^.*tps.*rtps.*wtps.*bread.*bwrtn', "scope": "SARB"},
                {"action": s.genstate("sard0"), "regexp": '^.*device.*busy.*avque.*avwait.*avserv', "scope": "SARD"},
                {"action": s.genstate("sard1"), "regexp": 'DEV.*tps.*blks/s', "scope": "SARD"},
                {"action": s.genstate("sard2"), "regexp": 'DEV.*tps.*rd_sec/s.*wr_sec/s', "scope": "SARD"},
                {"action": s.genstate("sarn0"), "regexp": 'IFACE.*rxpck/s.*txpck/s.*rxbyt/s.*txbyt/s.*rxcmp/s.*txcmp/s.*rxmcst/s', "scope": "SARN"},
                {"action": s.genstate("sarp0"), "regexp": 'pgpgin/s.*pgpgout/s', "scope": "SARP"},
                {"action": s.genstate("sarq0"), "regexp": '^.*runq-sz.*swpq-sz', "scope": "SARQ"},
                {"action": s.genstate("sarq1"), "regexp": 'runq-sz.*plist-sz.*ldavg-1.*ldavg-5', "scope": "SARQ"},
                {"action": s.genstate("sarm0"), "regexp": '^.*freemem freesw[a]*p', "scope": "SARR"},
                {"action": s.genstate("sarm1"), "regexp": 'kbmemfree.*kbmemused.*%memused.*kbbuffers.*kbcached.*kbswpfree.*kbswpused.*%swpused', "scope": "SARR"},
                {"action": s.genstate("saru0"), "regexp": '^.*usr.*sys.*wio.*idle', "scope": "SARU"},
                {"action": s.genstate("saru1"), "regexp": 'CPU.*%user.*%nice.*%system.*%idle', "scope": "SARU"},
                {"action": s.genstate("saru2"), "regexp": 'CPU.*%user.*%nice.*%sys.*%iowait.*%idle', "scope": "SARU"},
                {"action": s.genstate("saru2"), "regexp": 'CPU.*%usr.*%nice.*%sys.*%iowait.*%steal', "scope": "SARU"},
                {"action": s.genstate("saru3"), "regexp": '^.*usr.*sys.*wio.*idle.*physc', "scope": "SARU"},
                {"action": s.genstate("sarv0"), "regexp": '^.*proc-sz..*inod-sz.*file-sz', "scope": "SARV"},
                {"action": s.genstate("sarw0"), "regexp": 'pswpin/s.*pswpout/s', "scope": "SARW"},
                {"action": s.asarlcpu, "regexp": 'System configuration: lcpu=([0-9]+)'},
                {"action": s.asarent, "regexp": 'System configuration: lcpu=[0-9]+ ent=([0-9]+\.[0-9][0-9])'},
            ]
        }
        super(UserObject, s).__init__(**object)

    def begin(s, a):
        def tof(x):
            try: r = float(x)
            except: r = float(0)
            if str(r) == 'inf': r = 0.0
            if str(r) == 'nan': r = 0.0
            return r
        a.tof = tof
        a.tohour = lambda x,y: '00' if y=='AM'and int(x)>11 else str(int(x)+12) if y=='PM'and int(x)<12 else x

    def end(s, a):
        pass

    def genstate(s, c):
        def f(a, l ,g, m):
            a.setContext(c)
        return f

    def asarx(s, a, l, g, m):
        if len(g(3)) == 2:
            a.date = '20'+g(3)+g(1)+g(2)
        elif len(g(3)) == 4:
            a.date = g(3)+g(1)+g(2)

    def asarb0x(s, a, l, g, m):
        desc = dict(timestamp='text',bread='real',lread='real',bwrite='real',lwrite='real',pread='real',pwrite='real')
        a.emit('SARB', desc, dict(timestamp=a.date+g(1)+g(2)+g(3)+'000',bread=a.tof(g(4)),lread=a.tof(g(5)),bwrite=a.tof(g(7)),lwrite=a.tof(g(8)),pread=a.tof(g(10)),pwrite=a.tof(g(11))))

    def asarb1x(s, a, l, g, m):
        desc = dict(timestamp='text',bread='real',lread='real',bwrite='real',lwrite='real',pread='real',pwrite='real')
        a.emit('SARB', desc, dict(timestamp=a.date+a.tohour(g(1),g(4))+g(2)+g(3)+'000',bread=a.tof(g(8)),lread=0.0,bwrite=a.tof(g(9)),lwrite=0.0,pread=a.tof(g(6)),pwrite=a.tof(g(7))))

    def asard0x(s, a, l, g, m):
        desc = dict(timestamp='text',device='text',busy='real',avque='real',rws='real',kbs='real',avwait='real',avserv='real')
        if g(1):
            a.time=g(1)+g(2)+g(3)
            a.emit('SARD', desc, dict(timestamp=a.date+a.time+'000',device=g(4),busy=a.tof(g(5)),avque=a.tof(g(6)),rws=a.tof(g(7)),kbs=a.tof(g(8)),avwait=a.tof(g(9)),avserv=a.tof(g(10))))
        if g(11):
            a.emit('SARD', desc, dict(timestamp=a.date+a.time+'000',device=g(11),busy=a.tof(g(12)),avque=a.tof(g(13)),rws=a.tof(g(14)),kbs=a.tof(g(15)),avwait=a.tof(g(16)),avserv=a.tof(g(17))))

    def asard1x(s, a, l, g, m):
        desc = dict(timestamp='text',device='text',busy='real',avque='real',rws='real',kbs='real',avwait='real',avserv='real')
        a.emit('SARD', desc, dict(timestamp=a.date+g(1)+g(2)+g(3)+'000',device=g(4),busy=0.0,avque=0.0,rws=a.tof(g(5)),kbs=0.0,avwait=0.0,avserv=0.0))

    def asard2x(s, a, l, g, m):
        desc = dict(timestamp='text',device='text',busy='real',avque='real',rws='real',kbs='real',avwait='real',avserv='real')
        a.emit('SARD', desc, dict(timestamp=a.date+a.tohour(g(1),g(4))+g(2)+g(3)+'000',device=g(5),busy=0.0,avque=0.0,rws=a.tof(g(6))+a.tof(g(7)),kbs=0.0,avwait=0.0,avserv=0.0))

    def asarn0x(s, a, l, g, m):
        desc = dict(timestamp='text',iface='text',rxbyt='real',txbyt='real')
        a.emit('SARN', desc, dict(timestamp=a.date+a.tohour(g(1),g(4))+g(2)+g(3)+'000',iface=g(5),rxbyt=a.tof(g(8)),txbyt=a.tof(g(9))))

    def asarp0x(s, a, l, g, m):
        desc = dict(timestamp='text',pgpgin='real',pgpgout='real')
        a.emit('SARP', desc, dict(timestamp=a.date+a.tohour(g(1),g(4))+g(2)+g(3)+'000',pgpgin=a.tof(g(5)),pgpgout=a.tof(g(6))))

    def asarq0x(s, a, l, g, m):
        desc = dict(timestamp='text',runqsz='real',swpqsz='real')
        a.emit('SARQ', desc, dict(timestamp=a.date+g(1)+g(2)+g(3)+'000',runqsz=a.tof(g(4)),swpqsz=a.tof(g(6))))

    def asarq1x(s, a, l, g, m):
        desc = dict(timestamp='text',runqsz='real',swpqsz='real')
        a.emit('SARQ', desc, dict(timestamp=a.date+a.tohour(g(1),g(4))+g(2)+g(3)+'000',runqsz=a.tof(g(5)),swpqsz=0.0))

    def asarm0x(s, a, l, g, m):
        desc = dict(timestamp='text',kbmemfree='real',kbmemused='real',kbmemshrd='real',kbbuffers='real',kbcached='real',kbswpfree='real',kbswpused='real')
        a.emit('SARM', desc, dict(timestamp=a.date+g(1)+g(2)+g(3)+'000',kbmemfree=a.tof(g(4)),kbmemused=0.0,kbmemshrd=0.0,kbbuffers=0.0,kbcached=0.0,kbswpfree=a.tof(g(5)),kbswpused=0.0))

    def asarm1x(s, a, l, g, m):
        desc = dict(timestamp='text',kbmemfree='real',kbmemused='real',kbmemshrd='real',kbbuffers='real',kbcached='real',kbswpfree='real',kbswpused='real')
        a.emit('SARM', desc, dict(timestamp=a.date+a.tohour(g(1),g(4))+g(2)+g(3)+'000',kbmemfree=a.tof(g(5)),kbmemused=a.tof(g(6)),kbmemshrd=0.0,kbbuffers=a.tof(g(8)),kbcached=a.tof(g(9)),kbswpfree=a.tof(g(10)),kbswpused=a.tof(g(11))))

    def asaru0x(s, a, l, g, m):
        desc = dict(timestamp='text',cpuid='text',usr='real',sys='real',wio='real')
        a.emit('SARU', desc, dict(timestamp=a.date+g(1)+g(2)+g(3)+'000',cpuid='all',usr=a.tof(g(4)),sys=a.tof(g(5)),wio=a.tof(g(6))))

    def asaru1x(s, a, l, g, m):
        desc = dict(timestamp='text',cpuid='text',usr='real',sys='real',wio='real')
        a.emit('SARU', desc, dict(timestamp=a.date+a.tohour(g(1),g(4))+g(2)+g(3)+'000',cpuid=g(5),usr=a.tof(g(6)),sys=a.tof(g(8)),wio=0.0))

    def asaru2x(s, a, l, g, m):
        desc = dict(timestamp='text',cpuid='text',usr='real',sys='real',wio='real')
        a.emit('SARU', desc, dict(timestamp=a.date+a.tohour(g(1),g(4))+g(2)+g(3)+'000',cpuid=g(5),usr=a.tof(g(6)),sys=a.tof(g(8)),wio=a.tof(g(9))))

    def asaru3x(s, a, l, g, m):
        desc = dict(timestamp='text',cpuid='text',usr='real',sys='real',wio='real')
        corr=a.tof(g(8))/a.ent
        usr=a.tof(g(4))*corr
        sys=a.tof(g(5))*corr
        wio=a.tof(g(6))*corr
        a.emit('SARU', desc, dict(timestamp=a.date+g(1)+g(2)+g(3)+'000',cpuid='all',usr=usr,sys=sys,wio=wio))

    def asarv0x(s, a, l, g, m):
        desc = dict(timestamp='text',procsz='real')
        a.emit('SARV', desc, dict(timestamp=a.date+g(1)+g(2)+g(3)+'000',procsz=a.tof(g(4))))

    def asarw0x(s, a, l, g, m):
        desc = dict(timestamp='text',pswpin='real',pswpout='real')
        a.emit('SARW', desc, dict(timestamp=a.date+g(1)+g(2)+g(3)+'000',pswpin=a.tof(g(4)),pswpout=a.tof(g(5))))

    def asarlcpu(s, a, l, g, m):
        a.ent = a.tof(g(1)) / 2

    def asarent(s, a, l, g, m):
        a.ent = a.tof(g(1))
