class UserObject(dict):
    def __init__(s):
        if 'DBORAHSQLAX0' not in kairos: kairos['DBORAHSQLAX0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHSQLAXCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct sql_id label from ORAHQS where substr(sql_id,1,2) = '" + kairos["DBORAHSQLAX0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
