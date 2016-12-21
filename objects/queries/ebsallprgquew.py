class UserObject(dict):
    def __init__(s):
        if "EBSPRGQUEW" not in kairos: kairos['EBSPRGQUEW']=''
        object = {
            "type": "query",
            "id": "EBSALLPRGQUEW",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Waiting queues' label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name = '" + kairos["EBSPRGQUEW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
