class UserObject(dict):
    def __init__(s):
        s.dict = {}
        object = {
            "type": "function",
            "id": "match",
            "name": "match",
            "numparameters": 2,
            "function": s.match,
        }
        super(UserObject, s).__init__(**object)
    def match(s, x, r):
        import re
        return True if re.match(r,x) else False
    def __hash__(s):
        return hash("match")
