class UserObject(dict):
    def __init__(s):
        if "BOREPUSR" not in kairos: kairos['BOREPUSR']=''
        object = {
            "type": "query",
            "id": "BOALLREPUSRRT",
            "collection": "BO",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, 'Response time' label, sum(duration / 60.0) / count(*) value from BO where report = '" + kairos["BOREPUSR"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
