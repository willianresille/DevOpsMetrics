class HealthReport(object):

    def __init__(self, listHealthReport):
        for healthReport in listHealthReport:
            for key,value in healthReport.items():
                if(key == "score"):
                    self.score = value
                elif(key == "description"):
                    self.description = value
