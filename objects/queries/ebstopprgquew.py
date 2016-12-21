class UserObject(dict):
    def __init__(s):
        if "EBSPRGQUEW" not in kairos: kairos['EBSPRGQUEW']=''
        object = {
            "type": "query",
            "id": "EBSTOPPRGQUEW",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, queue_name label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name = '" + kairos["EBSPRGQUEW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
