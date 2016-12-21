class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUMLIBR",
            "collection": "DBORALIB",
            "request": "select timestamp, 'Reloads' label, sum(reloads) value from DBORALIB group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
