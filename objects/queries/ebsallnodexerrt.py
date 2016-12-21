class UserObject(dict):
    def __init__(s):
        if "EBSNODEXER" not in kairos: kairos['EBSNODEXER']=''
        object = {
            "type": "query",
            "id": "EBSALLNODEXERRT",
            "collection": "EBS12CM",
            "nocache": True,
            "request": "select timestamp, 'Response time' label, sum(time * 60.0) / count(*) value from EBS12CM where prg_name not like 'FNDRS%' and node_name = '" + kairos["EBSNODEXER"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
