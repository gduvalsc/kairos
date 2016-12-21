class UserObject(dict):
    def __init__(s):
        if "BOUSRREQ" not in kairos: kairos['BOUSRREQ']=''
        object = {
            "type": "query",
            "id": "BOALLUSRREQ",
            "collection": "BO",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['bocoeff'],
            "request": "select timestamp, 'All requests' label, sum(executecount * 1.0) / bocoeff() value from BO where user_name = '" + kairos["BOUSRREQ"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
