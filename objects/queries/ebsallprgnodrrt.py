class UserObject(dict):
    def __init__(s):
        if "EBSPRGNODR" not in kairos: kairos['EBSPRGNODR']=''
        object = {
            "type": "query",
            "id": "EBSALLPRGNODRRT",
            "collection": "EBS12CM",
            "nocache": True,
            "request": "select timestamp, 'Response time' label, sum(time * 60.0) / count(*) value from EBS12CM where prg_name = '" + kairos["EBSPRGNODR"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
