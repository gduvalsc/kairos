class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOALLREQ",
            "collection": "BO",
            "filterable": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, 'All requests' label, sum(executecount * 1.0) / bocoeff() value from BO group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
