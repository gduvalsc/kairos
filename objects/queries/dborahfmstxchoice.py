class UserObject(dict):
    def __init__(s):
        if 'DBORAHFMSTX0' not in kairos: kairos['DBORAHFMSTX0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHFMSTXCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct force_matching_signature label from ORAHQS where substr(force_matching_signature,1,2) = '" + kairos["DBORAHFMSTX0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
