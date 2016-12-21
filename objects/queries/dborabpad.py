class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORABPAD",
            "collection": "DBORABPA",
            "filterable": False,
            "request": "select timestamp, sizefactor label, avg(estphysreadsfactor) value from DBORABPA where bufpool = 'D' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
