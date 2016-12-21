class UserObject(dict):
    def __init__(s):
        if "BOREPREQ" not in kairos: kairos['BOREPREQ']=''
        object = {
            "type": "query",
            "id": "BOALLREPREQ",
            "collection": "BO",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, 'All requests' label, sum(executecount * 1.0) / bocoeff() value from BO where report = '" + kairos["BOREPREQ"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
