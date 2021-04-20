import json

from FMERepositoryUtility.FMERepositoryFind import FMERepositoryFind
from FileLogger.Logger import AppLogger

CONFIG = "app.json"
SECRET_CONFIG = "secret.json"
JOB_CONFIG = "job.json"

# read app settings
with open(CONFIG) as app_config_json:
    app_config = json.load(app_config_json)
with open(SECRET_CONFIG) as secrect_config_json:
    secrect_config = json.load(secrect_config_json)
with open(JOB_CONFIG) as job_config_json:
    job_config = json.load(job_config_json)
log = AppLogger("output\\log.txt", True)
result = AppLogger("output\\result.txt", True)


def create_job():
    return FMERepositoryFind(app_config, secrect_config, job_config, log, result)


try:
    job = create_job()
    job.execute()
    for line in job.fmw_found_list:
        result.write_line(line)
except Exception as e:
    log.write_line(e)
