class UserObject(dict):
    def __init__(s):
        if "EBSQUEEXER" not in kairos: kairos['EBSQUEEXER']=''
        object = {
            "type": "query",
            "id": "EBSALLQUEEXER",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Running executions' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and queue_name = '" + kairos["EBSQUEEXER"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
