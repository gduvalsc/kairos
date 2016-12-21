class UserObject(dict):
    def __init__(s):
        if 'DBORAHSQLTX0' not in kairos: kairos['DBORAHSQLTX0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHSQLTXCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct sql_id label from ORAHQS where substr(sql_id,1,2) = '" + kairos["DBORAHSQLTX0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
