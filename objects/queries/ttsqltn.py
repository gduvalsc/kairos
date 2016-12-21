class UserObject(dict):
    def __init__(s):
        if "TTSQLT" not in kairos: kairos['TTSQLT']=''
        object = {
            "type": "query",
            "id": "TTSQLTN",
            "collection": "TTSQLHS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ttcoeff'],
            "request": "select timestamp, 'Number of executions / second' label, sum(executions / deltatime) value from TTSQLHS where hashid = '" + kairos["TTSQLT"] + "'  group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
