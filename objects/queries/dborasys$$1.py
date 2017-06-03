class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASYS$$1",
            "collections": [
                "DBORAOSS",
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, statistic label, value*1.0/100/avgelapsed value from (select t.timestamp, statistic, value, avgelapsed from (select *, 'abcdef' kairosnode from DBORAOSS) t, (select *, 'abcdef' kairosnode from DBORAMISC) m where t.timestamp=m.timestamp and t.kairosnode=m.kairosnode) where statistic in ('USER_TIME','SYS_TIME')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)