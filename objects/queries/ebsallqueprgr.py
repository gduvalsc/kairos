class UserObject(dict):
    def __init__(s):
        if "EBSQUEPRGR" not in kairos: kairos['EBSQUEPRGR']=''
        object = {
            "type": "query",
            "id": "EBSALLQUEPRGR",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Running programs' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and queue_name = '" + kairos["EBSQUEPRGR"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
