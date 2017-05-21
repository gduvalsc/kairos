class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONMEMOV$$1",
            "collections": [
                "NMONMEM"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value value from NMONMEM where id in ('memtotal','swaptotal','memfree','Real free(MB)','Real total(MB)','Virtual free(MB)','Virtual total(MB)')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)