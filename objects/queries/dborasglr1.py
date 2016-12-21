class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGLR1",
            "collection": "DBORASTA",
            "request": "select timestamp, 'logical reads' label, sum(value) value from DBORASTA where statistic in ('consistent gets', 'db block gets') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
