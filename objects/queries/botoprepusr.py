class UserObject(dict):
    def __init__(s):
        if "BOREPUSR" not in kairos: kairos['BOREPUSR']=''
        object = {
            "type": "query",
            "id": "BOTOPREPUSR",
            "collection": "BO",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, user_name label, sum(executecount * 1.0) / bocoeff() value from BO where report = '" + kairos["BOREPUSR"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
