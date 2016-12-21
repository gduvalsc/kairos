class UserObject(dict):
    def __init__(s):
        if "EBSPRGEXEW" not in kairos: kairos['EBSPRGEXEW']=''
        object = {
            "type": "query",
            "id": "EBSALLPRGEXEWRT",
            "collection": "EBS12CM",
            "nocache": True,
            "request": "select timestamp, 'Waited time' label, sum(wait * 60.0) / count(*) value from EBS12CM where prg_name = '" + kairos["EBSPRGEXEW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
