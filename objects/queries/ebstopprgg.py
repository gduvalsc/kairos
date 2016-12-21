class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSTOPPRGG",
            "collection": "EBS12CM",
            "filterable": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, prg_name label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where status_code = 'G' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
