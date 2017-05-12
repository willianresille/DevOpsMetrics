# coding: utf-8
import json

from models import Job, Build, SubBuild, HealthReport


class JenkinsParser(object):

    def parse(self, content):
        data = json.loads(content)
        job = Job()
        job.name = data['name']
        job.buildable = data['buildable']
        job.builds = self._parse_builds(data['builds'])
        job.health_report = self._parse_health_report(data['healthReport'])
        job.last_build = self._parse_single_build(data['lastBuild'])

        job.last_successful_build = self._parse_single_build(data['lastSuccessfulBuild'])
        job.last_unsuccessful_build = self._parse_single_build(data['lastUnsuccessfulBuild'])

        return job

    def _parse_builds(self, builds_raw):
        builds = []
        for b in builds_raw:
            build = Build()
            build.duration = b['duration']
            build.number = b['number']
            build.result = b['result']
            build.timestamp = b['timestamp']
            build.subbuilds = self._parse_subbuilds(b['subBuilds'])
            builds.append(build)

        return builds

    def _parse_health_report(self, health_report_raw):
        health_reports = []
        for item in health_report_raw:
            health_report = HealthReport()
            health_report.description = self._get_value_from(item, 'description')
            health_report.score = self._get_value_from(item, 'score')
            health_reports.append(health_report)

        return health_reports

    def _parse_single_build(self,single_build_raw):
        last_build = Build()
        last_build.duration = self._get_value_from(single_build_raw, 'duration')
        last_build.number = self._get_value_from(single_build_raw, 'number')
        last_build.result = self._get_value_from(single_build_raw, 'result')
        last_build.timestamp = self._get_value_from(single_build_raw, 'timestamp')

        return last_build

    def _get_value_from(self, dicionario, key):
        if dicionario and key in dicionario:
            return dicionario[key]
        return None
        

    def _parse_subbuilds(self, subbuilds_raw):
        subbuilds = []
        for b in subbuilds_raw:
            subbuild = SubBuild()
            subbuild.duration = b['duration']
            subbuild.number = b['buildNumber']
            subbuild.job_name = b['jobName']
            subbuilds.append(subbuild)

        return subbuilds
