class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARRUNQSZ",
            "collection": "SARQ",
            "filterable": False,
            "request": "select timestamp, 'Run queue' label, avg(runqsz) value from SARQ group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
