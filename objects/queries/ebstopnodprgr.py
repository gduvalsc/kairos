class UserObject(dict):
    def __init__(s):
        if "EBSNODPRGR" not in kairos: kairos['EBSNODPRGR']=''
        object = {
            "type": "query",
            "id": "EBSTOPNODPRGR",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, prg_name label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and node_name = '" + kairos["EBSNODPRGR"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
