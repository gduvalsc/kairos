class UserObject(dict):
    def __init__(s):
        if 'DBORAHFMSAX0' not in kairos: kairos['DBORAHFMSAX0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHFMSAXCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct force_matching_signature label from ORAHQS where substr(force_matching_signature,1,2) = '" + kairos["DBORAHFMSAX0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
