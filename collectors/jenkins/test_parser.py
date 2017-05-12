# coding: utf-8
import unittest
from parser import JenkinsParser


class TestParser(unittest.TestCase):

    def setUp(self):
        with open('json/formatted.json', 'r') as f:
            self.content = f.read()

    def test_parse_do_job(self):
        parser = JenkinsParser()
        job = parser.parse(self.content)
        self.assertEquals('teste', job.name)
        self.assertEquals(job.buildable, True)

        last_build = job.last_build
        self.assertEquals(9998, last_build.duration)
        self.assertEquals(2, last_build.number)
        self.assertEquals('SUCCESS', last_build.result)
        self.assertEquals(1493396815561, last_build.timestamp)

        last_successful_build = job.last_successful_build
        self.assertEquals(9998, last_successful_build.duration)
        self.assertEquals(2, last_successful_build.number)
        self.assertEquals('SUCCESS', last_successful_build.result)
        self.assertEquals(1493396815561, last_successful_build.timestamp)

        last_unsuccesful_build = job.last_unsuccessful_build
        self.assertEquals(None, last_unsuccesful_build.duration)
        self.assertEquals(None, last_unsuccesful_build.number)
        self.assertEquals(None, last_unsuccesful_build.result)
        self.assertEquals(None, last_unsuccesful_build.timestamp)

        health_report = job.health_report[0]
        self.assertEquals('Estabilidade de builds: Nenhuma builds recente falhou.', health_report.description)
        self.assertEquals(100, health_report.score)

        builds = job.builds
        self.assertEquals(2, len(builds))


        first_build = builds[0]
        self.assertEquals(2, first_build.number)
        self.assertEquals(9998, first_build.duration)
        self.assertEquals('SUCCESS', first_build.result)
        self.assertEquals(1493396815561, first_build.timestamp)


        first_subbuild = first_build.subbuilds[0]
        self.assertEquals(1, first_subbuild.number)
        self.assertEquals('5 ms', first_subbuild.duration)
        self.assertEquals('teste1', first_subbuild.job_name)



if __name__ == '__main__':
    unittest.main()
