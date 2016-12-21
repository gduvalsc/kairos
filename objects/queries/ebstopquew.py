class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSTOPQUEW",
            "collection": "EBS12CM",
            "filterable": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, queue_name label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
