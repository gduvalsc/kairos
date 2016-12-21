class UserObject(dict):
    def __init__(s):
        if "DBORAHFMSAS0" not in kairos: kairos['DBORAHFMSAS0']=''
        if 'DBORAHFMSAS0' not in kairos: kairos['DBORAHFMSAS0'] = ''
        object = {
            "type": "query",
            "id": "DBORAHFMSASCHOICE",
            "collection": "ORAHQS",
            "nocache": True,
            "request": "select distinct force_matching_signature label from ORAHQS where substr(force_matching_signature,1,2) = '" + kairos["DBORAHFMSAS0"]+ "' order by label"
        }
        super(UserObject, s).__init__(**object)
