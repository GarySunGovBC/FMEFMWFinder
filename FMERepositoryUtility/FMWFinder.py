import json


class FMWFinder:
    CONFIG = "fmw.json"

    def __init__(self, fmw, object_finder, log):
        self.fmw = fmw
        self.log = log
        with open(FMWFinder.CONFIG) as fmw_config_json:
            self.fmw_config = json.load(fmw_config_json)
        self.object_finder = object_finder
        self.object_finder.init()

    def find_prop(self, items, prop_name):
        # if prop_name == 'fmw_datasets_dir_item_featuretypes_item_attributes_item':
        #     self.log.write_line(items)
        self.object_finder.find(items, self.fmw_config[prop_name]["props"])
        # if the object is list
        if isinstance(items, list):
            for item in items:
                prop_key = "%s_item" % prop_name
                self.find_prop(item, prop_key)
        # if the single object is dict
        if isinstance(items, dict):
            is_dir = "dir" in self.fmw_config[prop_name].keys()
            for sub_prop in self.fmw_config[prop_name]["sub_props"]:
                # some objects don't have the defined prop
                if sub_prop not in items.keys():
                    continue
                sub_obj = items[sub_prop]
                # some dict objects are {}
                if len(sub_obj) == 0:
                    continue
                prop_key = "%s_dir" % prop_name
                if not is_dir:
                    prop_key = "%s_%s" % (prop_name, sub_prop)
                self.find_prop(sub_obj, prop_key)

    def find(self):
        self.find_prop(self.fmw, "fmw")
