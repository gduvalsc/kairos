class UserObject(dict):
    def __init__(s):
        if "EBSPRGEXER" not in kairos: kairos['EBSPRGEXER']=''
        object = {
            "type": "query",
            "id": "EBSTOPPRGEXER",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, request_id||' (duration: '||cast(time * 60.0 as text)||')' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name = '" + kairos["EBSPRGEXER"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
