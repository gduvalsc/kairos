class UserObject(dict):
    def __init__(s):
        if 'DBORAHPHVSS0' not in kairos: kairos['DBORAHPHVSS0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHPHVSSCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct plan_hash_value label from ORAHQS where substr(plan_hash_value,1,2) = '" + kairos["DBORAHPHVSS0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
