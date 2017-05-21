class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHITK$$3",
            "collections": [
                "DBORABUF"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'hit ratio' label, sum(value) value from (select timestamp, 'xxx' label, 100.0 * (1 - (reads / gets)) value from DBORABUF where bufpool='K') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)