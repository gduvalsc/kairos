class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONTOPCPU",
            "collection": "NMONTOP",
            "filterable": True,
            "request": "select t.timestamp timestamp, t.process||'-'||command label, sum(value) value from (select timestamp, process, (value+0)/100.0 value from NMONTOP where id='%CPU') t, (select timestamp, process, value command from NMONTOP where id='Command') s where t.timestamp=s.timestamp and t.process=s.process group by t.timestamp, label order by t.timestamp"
        }
        super(UserObject, s).__init__(**object)
