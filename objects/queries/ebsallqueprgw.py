class UserObject(dict):
    def __init__(s):
        if "EBSQUEPRGW" not in kairos: kairos['EBSQUEPRGW']=''
        object = {
            "type": "query",
            "id": "EBSALLQUEPRGW",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Waiting programs' label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'NDRS%' and queue_name = '" + kairos["EBSQUEPRGW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
