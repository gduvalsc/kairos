class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHHSES",
            "collection": "ORAHAS",
            "filterable": True,
            "userfunctions": ['ashcoeff'],
            "request": "select timestamp, blocking_inst_id||' - '||blocking_session  label, sum(kairos_count)/ashcoeff() value from ORAHAS where blocking_session != '' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
