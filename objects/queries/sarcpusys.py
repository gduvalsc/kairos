class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARCPUSYS",
            "collection": "SARU",
            "filterable": False,
            "request": "select timestamp, 'sys' label, avg(sys) value from SARU where cpuid = 'all' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
