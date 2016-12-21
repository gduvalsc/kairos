class UserObject(dict):
    def __init__(s):
        if "EBSQUEEXER" not in kairos: kairos['EBSQUEEXER']=''
        object = {
            "type": "query",
            "id": "EBSALLQUEEXERRT",
            "collection": "EBS12CM",
            "nocache": True,
            "request": "select timestamp, 'Response time' label, sum(time * 60.0) / count(*) value from EBS12CM where prg_name not like 'FNDRS%' and queue_name = '" + kairos["EBSQUEEXER"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
