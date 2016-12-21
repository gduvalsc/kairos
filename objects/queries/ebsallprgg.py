class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSALLPRGG",
            "collection": "EBS12CM",
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'All programs with status G' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where status_code = 'G' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
