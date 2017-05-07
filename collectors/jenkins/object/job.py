from healthReport import HealthReport
from build import Build
class Job(object):


    #def __init__(self,name,buildable, builds, lastSuccessfulBuild, lastUnsuccessfulBuild, healthReport):
    #    self.name = name
    #    self.buildable = buildable
    #    self.builds = Build(builds)
    #    self.lastSuccessfulBuild = Build(lastSuccessfulBuild)
    #    self.lastUnsuccessfulBuild = Build(lastUnsuccessfulBuild)
    #    self.healthReport = HealthReport(healthReport)

    def setName(self, name):
        self.name = name

    def setBuildable(self,buildable):
        self.buildable = buildable

    def setBuild(self,builds):
        self.builds = Build(builds)

    def setLastSuccessfulBuild(self, lastSuccessfulBuild):
        self.lastSuccessfulBuild = Build(lastSuccessfulBuild)

    def setLastUnsuccessfulBuild(self, lastUnsuccessfulBuild):
        self.lastUnsuccessfulBuild = Build(lastUnsuccessfulBuild)

    def setHealthReport(self, healthReport):
        self.healthReport = HealthReport(healthReport)

    def setLastBuild(self, lastBuild):
        self.lastBuild = Build(lastBuild)
