class UserObject(dict):
    def __init__(s):
        if 'DBORAHPHVTX0' not in kairos: kairos['DBORAHPHVTX0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHPHVTXCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct plan_hash_value label from ORAHQS where substr(plan_hash_value,1,2) = '" + kairos["DBORAHPHVTX0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
