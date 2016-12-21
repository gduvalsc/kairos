class UserObject(dict):
    def __init__(s):
        if "BOUSRREP" not in kairos: kairos['BOUSRREP']=''
        object = {
            "type": "query",
            "id": "BOALLUSRREPRT",
            "collection": "BO",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, 'Response time' label, sum(duration / 60.0) / count(*) value from BO where user_name = '" + kairos["BOUSRREP"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
