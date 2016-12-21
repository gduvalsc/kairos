class UserObject(dict):
    def __init__(s):
        if "EBSQUENODW" not in kairos: kairos['EBSQUENODW']=''
        object = {
            "type": "query",
            "id": "EBSTOPQUENODW",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, node_name label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and queue_name = '" + kairos["EBSQUENODW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
