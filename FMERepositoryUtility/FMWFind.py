import json


class FMWFind:
    CONFIG = "fmw.json"

    def __init__(self, repo_name, fmw_name, parameters, prop_find, log):
        self.parameters = parameters
        self.log = log
        with open(FMWFind.CONFIG) as fmw_config_json:
            self.fmw_config = json.load(fmw_config_json)
        self.prop_find = prop_find
        self.prop_find.clear()
        self.match = []

    def find(self):
        for parameter in self.parameters:
            self.prop_find.find(parameter)
            for match in self.prop_find.matches:
                if len(match["props"])>0:
                    self.match.append(match["props"])
