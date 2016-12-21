class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPUOV",
            "collection": "NMONLPAR",
            "request": "select timestamp, id label, sum(value) value from NMONLPAR where id in ('PhysicalCPU', 'poolCPUs', 'PoolIdle', 'entitled', 'virtualCPUs', 'VirtualCPUs', 'poolCPUS', 'poolIdle') group by timestamp, label order by timestamp"
        }
        super(UserObject, s).__init__(**object)
