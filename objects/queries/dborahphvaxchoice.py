class UserObject(dict):
    def __init__(s):
        if 'DBORAHPHVAX0' not in kairos: kairos['DBORAHPHVAX0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHPHVAXCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct plan_hash_value label from ORAHQS where substr(plan_hash_value,1,2) = '" + kairos["DBORAHPHVAX0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
