class UserObject(dict):
    def __init__(s):
        if "BOREPREQ" not in kairos: kairos['BOREPREQ']=''
        object = {
            "type": "query",
            "id": "BOTOPREPREQ",
            "collection": "BO",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, report||' - '||event_id||' (duration: '||duration||')' label, sum(executecount * 1.0) / bocoeff() value from BO where report = '" + kairos["BOREPREQ"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
