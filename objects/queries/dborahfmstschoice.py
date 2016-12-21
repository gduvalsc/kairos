class UserObject(dict):
    def __init__(s):
        if 'DBORAHFMSTS0' not in kairos: kairos['DBORAHFMSTS0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHFMSTSCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct force_matching_signature label from ORAHQS where substr(force_matching_signature,1,2) = '" + kairos["DBORAHFMSTS0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
