class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONTOPCPU$$1",
            "collections": [
                "NMONTOP"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, label label, value value from (select t.timestamp timestamp, t.process||'-'||command label, value from (select timestamp, process, (value+0)/100.0 value from NMONTOP where id='%CPU') t, (select timestamp, process, value command from NMONTOP where id='Command') s where t.timestamp=s.timestamp and t.process=s.process)) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)