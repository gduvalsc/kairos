class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "LIVEOBJECT_SAMPLE_ORACLE",
            "collection": "SESSION",
            "request": "select timestamp, sid, program from SESSION"
        }
        super(UserObject, s).__init__(**object)
