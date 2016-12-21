class UserObject(dict):
    def __init__(s):
        if "EBSQUEEXEW" not in kairos: kairos['EBSQUEEXEW']=''
        object = {
            "type": "query",
            "id": "EBSTOPQUEEXEW",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, request_id||' (wait: '||cast(wait * 60.0 as text)||')' label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and queue_name = '" + kairos["EBSQUEEXEW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
