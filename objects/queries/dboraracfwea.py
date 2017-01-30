class UserObject(dict):
    def __init__(s):
        if "DBORARACFWEA" not in kairos: kairos['DBORARACFWEA']=''
        object = {
            "type": "query",
            "id": "DBORARACFWEA",
            "collection": "DBORARACTTFE",
            "nocache": True,
            "request": "select timestamp, 'All instances' label, sum(timewaited) value from DBORARACTTFE where inum=0 and event = '" + kairos["DBORARACFWEA"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
