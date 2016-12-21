class UserObject(dict):
    def __init__(s):
        if "EBSNODPRGW" not in kairos: kairos['EBSNODPRGW']=''
        object = {
            "type": "query",
            "id": "EBSTOPNODPRGW",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, prg_name label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and node_name = '" + kairos["EBSNODPRGW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
