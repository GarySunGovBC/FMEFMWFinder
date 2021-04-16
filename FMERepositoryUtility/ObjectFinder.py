from past.types import basestring

from FMERepositoryUtility.PropFound import PropFound


class ObjectFinder:

    def __init__(self, targets):
        self.prop_found = PropFound(targets)

    def init(self):
        self.prop_found.init()

    def found(self):
        return self.prop_found.found()

    def report(self):
        return self.prop_found.report()

    def find(self, items, props):
        if len(props) == 0:
            return
        if isinstance(items, dict):
            for prop in props:
                self.prop_found.find(items[prop], prop, items.keys())
