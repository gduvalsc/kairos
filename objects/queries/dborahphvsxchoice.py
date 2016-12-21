class UserObject(dict):
    def __init__(s):
        if 'DBORAHPHVSX0' not in kairos: kairos['DBORAHPHVSX0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHPHVSXCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct plan_hash_value label from ORAHQS where substr(plan_hash_value,1,2) = '" + kairos["DBORAHPHVSX0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
