class UserObject(dict):
    def __init__(s):
        if 'DBORAHSQLAS0' not in kairos: kairos['DBORAHSQLAS0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHSQLASCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct sql_id label from ORAHQS where substr(sql_id,1,2) = '" + kairos["DBORAHSQLAS0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
