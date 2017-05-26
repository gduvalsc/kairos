class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSPRGEXEW$$3",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Wait time' label, avg(value) value from (select timestamp, 'xxx' label, wait * 60.0 value from EBS12CM where prg_name = '%(EBSPRGEXEW)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)