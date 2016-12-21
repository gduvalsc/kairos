class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARCPUUSR",
            "collection": "SARU",
            "filterable": False,
            "request": "select timestamp, 'usr' label, avg(usr) value from SARU where cpuid = 'all' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
