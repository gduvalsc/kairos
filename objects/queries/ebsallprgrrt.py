class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSALLPRGRRT",
            "collection": "EBS12CM",
            "request": "select timestamp, 'Response time' label, sum(time * 60.0) / count(*) value from EBS12CM where prg_name not like 'FNDRS%' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
