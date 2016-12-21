class UserObject(dict):
    def __init__(s):
        if "EBSPRGQUEW" not in kairos: kairos['EBSPRGQUEW']=''
        object = {
            "type": "query",
            "id": "EBSALLPRGQUEWRT",
            "collection": "EBS12CM",
            "nocache": True,
            "request": "select timestamp, 'Waited time' label, sum(wait * 60.0) / count(*) value from EBS12CM where prg_name = '" + kairos["EBSPRGQUEW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
