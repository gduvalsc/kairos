class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOTOPUSR",
            "collection": "BO",
            "filterable": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, user_name label, sum(executecount * 1.0) / bocoeff() value from BO group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
