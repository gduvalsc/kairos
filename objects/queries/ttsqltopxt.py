class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTSQLTOPXT",
            "collection": "TTSQLHS",
            "filterable": True,
            "userfunctions": ['ttcoeff'],
            "request": "select timestamp, hashid label, sum(totaltime / 1000.0 / deltatime ) / ttcoeff() value from TTSQLHS group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
