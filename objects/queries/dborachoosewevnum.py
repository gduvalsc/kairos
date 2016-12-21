class UserObject(dict):
    def __init__(s):
        if "DBORAWEV" not in kairos: kairos['DBORAWEV']=''
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEVNUM",
            "collection": "DBORAWEV",
            "nocache": True,
            "request": "select timestamp, 'number of operations/sec' label, sum(count) value from DBORAWEV where event = '" + kairos["DBORAWEV"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
