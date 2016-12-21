class UserObject(dict):
    def __init__(s):
        if "EBSPRGEXER" not in kairos: kairos['EBSPRGEXER']=''
        object = {
            "type": "query",
            "id": "EBSALLPRGEXER",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Running executions' label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name = '" + kairos["EBSPRGEXER"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
