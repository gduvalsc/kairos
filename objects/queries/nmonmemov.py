class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONMEMOV",
            "collection": "NMONMEM",
            "request": "select timestamp, id label, sum(value) value from NMONMEM where id in ('memtotal','swaptotal','memfree','Real free(MB)','Real total(MB)','Virtual free(MB)','Virtual total(MB)') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
