class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHMAC",
            "collection": "ORAHAS",
            "filterable": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, machine label, sum(kairos_count)/ashcoeff() value from ORAHAS where machine != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
