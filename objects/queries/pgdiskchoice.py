class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDISKCHOICE",
            "collections": ["vpsutil_disk_io_counters"],
            "request": "select distinct disk  as label from vpsutil_disk_io_counters order by label"
        }
        super(UserObject, s).__init__(**object)