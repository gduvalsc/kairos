class UserObject(dict):
    def __init__(s):
        s.dict = {}
        object = {
            "type": "function",
            "id": "pxwev",
            "name": "pxwev",
            "numparameters": 1,
            "function": s.pxwev,
        }
        super(UserObject, s).__init__(**object)
    def pxwev(s, x):
        return True if x[0:2] in 'PX' else False
    def __hash__(s):
        return hash("pxwev")
