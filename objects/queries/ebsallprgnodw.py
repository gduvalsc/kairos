class UserObject(dict):
    def __init__(s):
        if "EBSPRGNODW" not in kairos: kairos['EBSPRGNODW']=''
        object = {
            "type": "query",
            "id": "EBSALLPRGNODW",
            "collection": "EBS12CM",
            "nocache": True,
            "userfunctions": ['ebscoeff'],
            "request": "select timestamp, 'Waiting nodes' label, sum(waitcount * 1.0) / ebscoeff() value from EBS12CM where prg_name = '" + kairos["EBSPRGNODW"] + "' group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
