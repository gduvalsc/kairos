class UserObject(dict):
    def __init__(s):
        if "TTSQLT" not in kairos: kairos['TTSQLT']=''
        object = {
            "type": "query",
            "id": "TTSQLT",
            "collection": "TTSQLHS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ttcoeff'],
            "request": "select timestamp, 'Execution time' label, sum(totaltime / 1000.0 / deltatime) / ttcoeff() value from TTSQLHS where hashid = '" + kairos["TTSQLT"] + "'  group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
