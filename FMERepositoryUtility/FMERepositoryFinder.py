from FMEAPI.ApiException import APIException
from FMERepositoryUtility.FMEServerJob import FMEServerJob
from FMERepositoryUtility.FMWFinder import FMWFinder
from FMERepositoryUtility.RepoFinder import RepoFinder


class FMERepositoryFinder(FMEServerJob):

    def do_fmw_job(self, repo, fmw):
        repo_name = repo["name"]
        fmw_name = fmw["name"]
        full_name = "%s\\%s" % (repo_name, fmw_name)
        if self.job_config["fmw_filter"]["on"]:
            if fmw_name not in self.job_config["fmw_filter"]["items"]:
                return
        #self.log.write_line("Finding in %s ..." % full_name)
        fmw = self.api.get_repo_fmw(repo_name, fmw_name)
        fmw_finder = FMWFinder(fmw, self.object_finder, self.log)
        try:
            fmw_finder.find()
            if self.object_finder.found():
                self.log.write_line("Found: %s, %s" % (fmw_name, self.object_finder.report()))
                self.result.write_line(fmw_name)
        except APIException as e:
            raise APIException("Error: %s. reason: %s" % (full_name, e.error["message"]))
    def do_repo_job(self, repo):
        try:
            repo_finder = RepoFinder(repo, self.object_finder)
            repo_finder.find()
            if self.object_finder.found():
                self.log.write_line("Found: %s, %s" % (repo["name"], self.object_finder.report()))
                self.result.write_line(repo["name"])
        except APIException as e:
            self.log.write_line("Error: %s. reason: %s" % (repo["name"], e.error["message"]))
