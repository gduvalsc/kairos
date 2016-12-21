class UserObject(dict):
    def __init__(s):
        if 'DBORAHQT' not in kairos: kairos['DBORAHQT'] = ''
        object = {
            "type": "query",
            "id": "DBORAHQT",
            "collection": "ORAHQT",
            "nocache": True,
            "request": "select distinct sql_id key, sql_text value from ORAHQT where sql_id = '" + kairos["DBORAHQT"] + "'"
        }
        super(UserObject, s).__init__(**object)
