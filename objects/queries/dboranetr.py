class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORANETR",
            "collection": "DBORASTA",
            "userfunctions": ['match'],
            "request": "select timestamp, statistic label, sum(value) value from DBORASTA where match(statistic, '(SQL.*Net roundtrips)') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
