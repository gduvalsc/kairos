class UserObject(dict):
    def __init__(s):
        if "BOUSRREP" not in kairos: kairos['BOUSRREP']=''
        object = {
            "type": "query",
            "id": "BOTOPUSRREP",
            "collection": "BO",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, report label, sum(executecount * 1.0) / bocoeff() value from BO where user_name = '" + kairos["BOUSRREP"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
