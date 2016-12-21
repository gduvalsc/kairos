class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLV",
            "collection": "ORAHQS",
            "filterable": True,
            "request": "select timestamp, sql_id label, sum(version_count) value from ORAHQS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
