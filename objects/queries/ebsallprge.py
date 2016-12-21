class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSALLPRGE",
            "collection": "EBS12CM",
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'All programs with status E' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where status_code = 'E' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
