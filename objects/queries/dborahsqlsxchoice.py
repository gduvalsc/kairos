class UserObject(dict):
    def __init__(s):
        if 'DBORAHSQLSX0' not in kairos: kairos['DBORAHSQLSX0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHSQLSXCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct sql_id label from ORAHQS where substr(sql_id,1,2) = '" + kairos["DBORAHSQLSX0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
