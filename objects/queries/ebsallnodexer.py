class UserObject(dict):
    def __init__(s):
        if "EBSNODEXER" not in kairos: kairos['EBSNODEXER']=''
        object = {
            "type": "query",
            "id": "EBSALLNODEXER",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Running executions' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name not like 'FNDRS%' and node_name = '" + kairos["EBSNODEXER"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
