
class SubBuild(Build):

    def __init__(self,subBuilds):
        self.subBuilds = [];
        #SubBuilds
        for subBuildsAndCauses in subBuilds:
            for keySubBuildsAndCauses,valueSubBuildsAndCauses in subBuildsAndCauses.items():
                if(keySubBuildsAndCauses == "parentJobName"):
                    self.parentJobName = valueSubBuildsAndCauses
                if(keySubBuildsAndCauses == "causes"):
                    print("         "+keySubBuildsAndCauses)
                elif(keySubBuildsAndCauses != "_class"):

                    print("         "+keySubBuildsAndCauses+": "+str(valueSubBuildsAndCauses))
                if type(valueSubBuildsAndCauses) == list:
                    for causes in valueSubBuildsAndCauses:
                        for keyCauses,valueCauses in causes.items():
                            if(keyCauses != "_class"):
                                print("             "+keyCauses+": ",valueCauses)
                self.subBuilds.append(self)

            for teste in self.subBuilds:
                print("------------------------------------||-------------------------------------------")
                print(teste.parentJobName)

    def setParentJobName(self, parentJobName):
        self.parentJobName = parentJobName

    def setParentBuildNumber(self, parentBuildNumber):
        self.setParentBuildNumber = parentBuildNumber

    def setJobName(self, jobName):
        self.jobName = jobName

    def setBuildNumber(self, buildNumber):
        self.setBuildNumber = buildNumber

    def setPhaseName(self, phaseName):
        self.phaseName = phaseName
