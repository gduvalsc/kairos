class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSALLPRGW",
            "collection": "EBS12CM",
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Waiting programs' label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
