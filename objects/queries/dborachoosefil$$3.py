class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSEFIL$$3",
            "collections": [
                "DBORAFIL"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'database blocks per read' label, sum(value) value from (select timestamp, 'xxx' label, blocksperread value from DBORAFIL where file='%(DBORAFIL)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)