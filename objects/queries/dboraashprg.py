class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHPRG",
            "collection": "ORAHAS",
            "filterable": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, program label, sum(kairos_count)/ashcoeff() value from ORAHAS where program != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
