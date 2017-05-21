class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPUOV$$1",
            "collections": [
                "NMONLPAR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value value from NMONLPAR where id in ('PhysicalCPU', 'poolCPUs', 'PoolIdle', 'entitled', 'virtualCPUs', 'VirtualCPUs', 'poolCPUS', 'poolIdle')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)