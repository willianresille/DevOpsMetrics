# coding: utf-8
class Build(object):
    duration = 0
    number = 0
    result = ''
    timestamp = 0
    sub_builds = []
    causes = ''

class SubBuild(object):
    duration = None
    build_number = 0
    job_name = ''
    parent_build_number = 0
    parent_job_name = ''
    phase_name = ''
    result = ''


class Job(object):
    name = ''
    buildable = False
    builds = []
    last_build = {}
    last_successful_build = {}
    last_unsuccessful_build = {}

class HealthReport(object):
    description = ''
    score = 0
