class UserObject(dict):
    def __init__(s):
        if "EBSNODPRGR" not in kairos: kairos['EBSNODPRGR']=''
        object = {
            "type": "query",
            "id": "EBSALLNODPRGRRT",
            "collection": "EBS12CM",
            "nocache": True,
            "request": "select timestamp, 'Response time' label, sum(time * 60.0) / count(*) value from EBS12CM where prg_name not like 'FNDRS%' and node_name = '" + kairos["EBSNODPRGR"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
