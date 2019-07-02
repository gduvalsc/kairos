class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONTOPMEM$$1",
            "collections": [
                "NMONTOP"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, label as label, value as value from (select t.timestamp as timestamp, t.process||'-'||command as label, value from (select timestamp, process, cast(value as real)+0.0 as value from NMONTOP where id='ResData') t, (select timestamp, process, value command from NMONTOP where id='Command') s where t.timestamp=s.timestamp and t.process=s.process) as foo) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)