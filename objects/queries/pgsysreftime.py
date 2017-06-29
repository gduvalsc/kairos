class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSREFTIME",
            "collections": ["vpsutil_cpu_times"],
            "request": "select distinct timestamp from vpsutil_cpu_times"
        }
        super(UserObject, s).__init__(**object)
