class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOALLREPRT",
            "collection": "BO",
            "filterable": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, 'Response time' label, sum(duration / 60.0) / count(*) value from BO group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
