class UserObject(dict):
    def __init__(s):
        if "BOUSRREQ" not in kairos: kairos['BOUSRREQ']=''
        object = {
            "type": "query",
            "id": "BOALLUSRREQRT",
            "collection": "BO",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, 'Response time' label, sum(duration / 60.0) / count(*) value from BO where user_name = '" + kairos["BOUSRREQ"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
