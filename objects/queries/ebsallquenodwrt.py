class UserObject(dict):
    def __init__(s):
        if "EBSQUENODW" not in kairos: kairos['EBSQUENODW']=''
        object = {
            "type": "query",
            "id": "EBSALLQUENODWRT",
            "collection": "EBS12CM",
            "nocache": True,
            "request": "select timestamp, 'Waited time' label, sum(wait * 60.0) / count(*) value from EBS12CM where prg_name not like 'FNDRS%' and node_name = '" + kairos["EBSQUENODW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
