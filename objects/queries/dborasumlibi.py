class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUMLIBI",
            "collection": "DBORALIB",
            "request": "select timestamp, 'Invalidations' label, sum(invalidations) value from DBORALIB group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
