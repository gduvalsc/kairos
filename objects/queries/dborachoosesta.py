class UserObject(dict):
    def __init__(s):
        if "DBORASTA" not in kairos: kairos['DBORASTA']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSESTA",
            "collection": "DBORASTA",
            "nocache": True,
            "request": "select timestamp, statistic label, sum(value) value from DBORASTA where statistic = '" + kairos["DBORASTA"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
