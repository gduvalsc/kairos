class UserObject(dict):
    def __init__(s):
        if "TTSQLE" not in kairos: kairos['TTSQLE']=''
        object = {
            "type": "query",
            "id": "TTSQLE",
            "collection": "TTSQLHS",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ttcoeff'],
            "request": "select timestamp, 'Execution time per exec' label, sum(totaltime / 1.0 / deltatime / executions) / ttcoeff() value from TTSQLHS where hashid = '" + kairos["TTSQLE"] + "'  group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
