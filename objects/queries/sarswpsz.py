class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARSWPQSZ",
            "collection": "SARQ",
            "filterable": False,
            "request": "select timestamp, 'Swap queue' label, avg(swpqsz) value from SARQ group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
