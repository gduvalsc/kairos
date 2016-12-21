class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALIBI",
            "collection": "DBORALIB",
            "filterable": True,
            "request": "select timestamp, item label, sum(invalidations) value from DBORALIB group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
