class UserObject(dict):
    def __init__(s):
        if "EBSPRGQUER" not in kairos: kairos['EBSPRGQUER']=''
        object = {
            "type": "query",
            "id": "EBSTOPPRGQUER",
            "collection": "EBS12CM",
            "filterable": True,
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, queue_name label, sum(executecount * 1.0) / ebscoeff() value from EBS12CM where prg_name = '" + kairos["EBSPRGQUER"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
