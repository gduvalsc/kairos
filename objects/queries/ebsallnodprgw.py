class UserObject(dict):
    def __init__(s):
        if "EBSNODPRGW" not in kairos: kairos['EBSNODPRGW']=''
        object = {
            "type": "query",
            "id": "EBSALLNODPRGW",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Waiting programs' label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'NDRS%' and node_name = '" + kairos["EBSNODPRGW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
