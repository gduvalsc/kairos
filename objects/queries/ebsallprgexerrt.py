class UserObject(dict):
    def __init__(s):
        if "EBSPRGEXER" not in kairos: kairos['EBSPRGEXER']=''
        object = {
            "type": "query",
            "id": "EBSALLPRGEXERRT",
            "collection": "EBS12CM",
            "nocache": True,
            "request": "select timestamp, 'Response time' label, sum(time * 60.0) / count(*) value from EBS12CM where prg_name = '" + kairos["EBSPRGEXER"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
