class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPRS",
            "collection": "DBORASTA",
            "userfunctions": ['match'],
            "request": "select timestamp, statistic label, sum(value) value from DBORASTA where match(statistic, '(execute|parse count|session cursor)') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
