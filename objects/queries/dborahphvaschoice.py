class UserObject(dict):
    def __init__(s):
        if 'DBORAHPHVAS0' not in kairos: kairos['DBORAHPHVAS0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHPHVASCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct plan_hash_value label from ORAHQS where substr(plan_hash_value,1,2) = '" + kairos["DBORAHPHVAS0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
