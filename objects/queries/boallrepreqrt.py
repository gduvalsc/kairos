class UserObject(dict):
    def __init__(s):
        if "BOREPREQ" not in kairos: kairos['BOREPREQ']=''
        object = {
            "type": "query",
            "id": "BOALLREPREQRT",
            "collection": "BO",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, 'Response time' label, sum(duration / 60.0) / count(*) value from BO where report = '" + kairos["BOREPREQ"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
