class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAPHR",
            "collection": "DBORASTA",
            "request": "select timestamp, statistic label,  sum(value) value from DBORASTA where statistic in ('consistent gets','db block gets','physical reads','consistent gets direct','db block gets direct','physical reads direct','consistent gets from cache','db block gets from cache',',physical reads cache','physical read total IO requests','lob reads','physical reads direct (lob)') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
