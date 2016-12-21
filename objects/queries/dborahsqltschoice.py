class UserObject(dict):
    def __init__(s):
        if 'DBORAHSQLTS0' not in kairos: kairos['DBORAHSQLTS0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHSQLTSCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct sql_id label from ORAHQS where substr(sql_id,1,2) = '" + kairos["DBORAHSQLTS0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
