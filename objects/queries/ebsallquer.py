class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSALLQUER",
            "collection": "EBS12CM",
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Running queues' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
