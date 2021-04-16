from past.types import basestring


class PropFound:

    def __init__(self, targets):
        self.targets = targets

    def init(self):
        for target in self.targets:
            target["found"] = False

    def report(self):
        result = ""
        for target in self.targets:
            result += "%s = %s and " % (target["name"], target["value"])
        return result

    def found(self):
        for target in self.targets:
            if not target["found"]:
                return False
        return True

    def find(self, val, prop, keys):

        def check():
            ok = target["found"]
            if ok:
                return ok
            if not isinstance(val, basestring):
                return ok
            val_lower = val.lower()
            if "match" in target.keys() and target["match"] == "equal":
                ok = target["value"].lower() == val_lower
            else:
                ok = target["value"].lower() in val_lower
            if not ok:
                return ok
            return (target["name"] == "*") or (prop in keys and prop == target["name"])

        for target in self.targets:
            target["found"] = check()
