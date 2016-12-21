class UserObject(dict):
    def __init__(s):
        if "EBSQUEEXEW" not in kairos: kairos['EBSQUEEXEW']=''
        object = {
            "type": "query",
            "id": "EBSALLQUEEXEWRT",
            "collection": "EBS12CM",
            "nocache": True,
            "request": "select timestamp, 'Waited time' label, sum(wait * 60.0) / count(*) value from EBS12CM where prg_name not like 'FNDRS%' and queue_name = '" + kairos["EBSQUEEXEW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
