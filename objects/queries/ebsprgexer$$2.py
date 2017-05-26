class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSPRGEXER$$2",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [
                "ebscoeff"
            ],
            "request": "select timestamp, 'Running executions' label, sum(value) value from (select timestamp, 'xxx' label, executecount * 1.0 / ebscoeff() value from EBS12CM where prg_name = '%(EBSPRGEXER)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)