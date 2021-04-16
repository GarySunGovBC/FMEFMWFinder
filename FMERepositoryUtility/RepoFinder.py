import json


class RepoFinder:
    CONFIG = "repo.json"

    def __init__(self, repo, object_finder):
        self.repo = repo
        with open(RepoFinder.CONFIG) as repo_config_json:
            self.repo_config = json.load(repo_config_json)
        self.object_finder = object_finder
        self.object_finder.init()

    def find(self):
        """ compare 2 repo """
        self.object_finder.find(self.repo, ["owner", "name", "description"])
