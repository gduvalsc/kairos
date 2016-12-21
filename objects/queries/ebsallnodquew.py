class UserObject(dict):
    def __init__(s):
        if "EBSNODQUEW" not in kairos: kairos['EBSNODQUEW']=''
        object = {
            "type": "query",
            "id": "EBSALLNODQUEW",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Waiting queues' label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'NDRS%' and node_name = '" + kairos["EBSNODQUEW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
