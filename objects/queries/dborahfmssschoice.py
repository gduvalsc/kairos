class UserObject(dict):
    def __init__(s):
        if "DBORAHFMSSS0" not in kairos: kairos['DBORAHFMSSS0']=''
        if 'DBORAHFMSSS0' not in kairos: kairos['DBORAHFMSSS0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHFMSSSCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct force_matching_signature label from ORAHQS where substr(force_matching_signature,1,2) = '" + kairos["DBORAHFMSSS0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
