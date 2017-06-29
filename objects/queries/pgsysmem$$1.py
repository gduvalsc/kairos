class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSMEM$$1",
            "collections": [
                "vpsutil_virtual_memory"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'Total size' label, total value from vpsutil_virtual_memory union all select timestamp, 'Available size' label, available value from vpsutil_virtual_memory union all select timestamp, 'Used size' label, used value from vpsutil_virtual_memory union all select timestamp, 'Free size' label, free value from vpsutil_virtual_memory union all select timestamp, 'Active size' label, active value from vpsutil_virtual_memory union all select timestamp, 'Inactive size' label, inactive value from vpsutil_virtual_memory union all select timestamp, 'Buffers size' label, buffers value from vpsutil_virtual_memory union all select timestamp, 'Cached size' label, cached value from vpsutil_virtual_memory) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)