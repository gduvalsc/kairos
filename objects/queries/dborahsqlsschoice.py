class UserObject(dict):
    def __init__(s):
        if 'DBORAHSQLSS0' not in kairos: kairos['DBORAHSQLSS0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHSQLSSCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct sql_id label from ORAHQS where substr(sql_id,1,2) = '" + kairos["DBORAHSQLSS0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
