class Job():

    def __init__(self,name,buildable, builds, lastSuccessfulBuild, lastUnsuccessfulBuild, healthReport):
        self.name = name
        self.buildable = buildable
        Build.__init__(builds)
        self.lastSuccessfulBuild = lastSuccessfulBuild
        self.lastUnsuccessfulBuild = lastUnsuccessfulBuild
        self.healthReport = healthReport
