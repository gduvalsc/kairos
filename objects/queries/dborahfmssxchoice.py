class UserObject(dict):
    def __init__(s):
        if 'DBORAHFMSSX0' not in kairos: kairos['DBORAHFMSSX0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHFMSSXCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct force_matching_signature label from ORAHQS where substr(force_matching_signature,1,2) = '" + kairos["DBORAHFMSSX0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
