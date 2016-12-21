class UserObject(dict):
    def __init__(s):
        if "DBORARACFWES" not in kairos: kairos['DBORARACFWES']=''
        object = {
            "type": "query",
            "id": "DBORARACFWES",
            "collection": "DBORARACTTFE",
            "nocache": True,
            "request": "select timestamp, 'All instances' label, sum(timewaited) value from DBORARACTTFE where inum=0 and event = '" + kairos["DBORARACFWES"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
