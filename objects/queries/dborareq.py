class UserObject(dict):
    def __init__(s):
        if 'DBORAREQ' not in kairos: kairos['DBORAREQ'] = ''
        object = {
            "type": "query",
            "id": "DBORAREQ",
            "collection": "DBORAREQ",
            "nocache": True,
            "request": "select distinct sqlid key, request value from DBORAREQ where sqlid = '" + kairos["DBORAREQ"] + "'"
        }
        super(UserObject, s).__init__(**object)
