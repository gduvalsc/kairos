class UserObject(dict):
    def __init__(s):
        if 'DBORAHPHVTS0' not in kairos: kairos['DBORAHPHVTS0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHPHVTSCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct plan_hash_value label from ORAHQS where substr(plan_hash_value,1,2) = '" + kairos["DBORAHPHVTS0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
