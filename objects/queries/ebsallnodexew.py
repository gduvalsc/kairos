class UserObject(dict):
    def __init__(s):
        if "EBSNODEXEW" not in kairos: kairos['EBSNODEXEW']=''
        object = {
            "type": "query",
            "id": "EBSALLNODEXEW",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Waiting executions' label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'NDRS%' and node_name = '" + kairos["EBSNODEXEW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
