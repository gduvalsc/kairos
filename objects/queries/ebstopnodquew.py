class UserObject(dict):
    def __init__(s):
        if "EBSNODQUEW" not in kairos: kairos['EBSNODQUEW']=''
        object = {
            "type": "query",
            "id": "EBSTOPNODQUEW",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, queue_name label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and node_name = '" + kairos["EBSNODQUEW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
