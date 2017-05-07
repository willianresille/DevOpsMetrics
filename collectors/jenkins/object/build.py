#import subBuild

class Build(object):

    def __init__(self, valueBuildsJson):
        for builds in valueBuildsJson:
            for keyBuilds,valueBuilds in builds.items():
                if type(valueBuilds) == list:
                    pass
                #    self.listSubBuilds = subBuilds(valueBuilds)
                else:
                    if(keyBuilds == "duration"):
                        self.duration = valueBuilds
                    elif(keyBuilds == "timestamp"):
                        self.timestamp = valueBuilds
                    elif(keyBuilds == "number"):
                        self.number = valueBuilds
                    elif(keyBuilds == "result"):
                        self.result = valueBuilds

    def setDuration(self, duration):
        self.duration = duration

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def setNumber(self, number):
        self.number = number

    def setResult(self, result):
        self.result = result
