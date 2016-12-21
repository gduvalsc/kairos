class UserObject(dict):
    def __init__(s):
        if "EBSQUENODR" not in kairos: kairos['EBSQUENODR']=''
        object = {
            "type": "query",
            "id": "EBSALLQUENODR",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Running nodes' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and queue_name = '" + kairos["EBSQUENODR"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
