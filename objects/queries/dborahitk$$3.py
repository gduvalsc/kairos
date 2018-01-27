class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITK$$3",
            "collections": [
                "DBORABUF"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'hit ratio' as label, 100.0 * (1 - (reads / gets)) as value from DBORABUF where bufpool='K') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)