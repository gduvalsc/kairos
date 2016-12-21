class UserObject(dict):
    def __init__(s):
        if "EBSPRGNODR" not in kairos: kairos['EBSPRGNODR']=''
        object = {
            "type": "query",
            "id": "EBSALLPRGNODR",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Running nodes' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name = '" + kairos["EBSPRGNODR"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
