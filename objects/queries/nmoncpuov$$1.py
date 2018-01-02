class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPUOV$$1",
            "collections": [
                "NMONLPAR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, id as label, value as value from NMONLPAR where id in ('PhysicalCPU', 'poolCPUs', 'PoolIdle', 'entitled', 'virtualCPUs', 'VirtualCPUs', 'poolCPUS', 'poolIdle')) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)