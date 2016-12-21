class UserObject(dict):
    def __init__(s):
        if "EBSNODQUER" not in kairos: kairos['EBSNODQUER']=''
        object = {
            "type": "query",
            "id": "EBSTOPNODQUER",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, queue_name label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and node_name = '" + kairos["EBSNODQUER"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
