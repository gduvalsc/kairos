class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSNODPRGR$$1",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, prg_name label, executecount * 1.0 / ebscoeff() value from EBS12CM where node_name = '%(EBSNODPRGR)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)