class UserObject(dict):
    def __init__(s):
        if "EBSQUEPRGW" not in kairos: kairos['EBSQUEPRGW']=''
        object = {
            "type": "query",
            "id": "EBSTOPQUEPRGW",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, prg_name label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and queue_name = '" + kairos["EBSQUEPRGW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
