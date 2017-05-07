import json
from object.job import Job

job = Job()
with open('Formatted JSON.json') as data_file:
    job_json = json.load(data_file)

for keyJobJson,valueJobJson in job_json.items():

    if(keyJobJson == "name"):
        job.setName(valueJobJson)

    if(keyJobJson == "buildable"):
        job.setBuildable(valueJobJson)

    if(keyJobJson == "healthReport"):
        job.setHealthReport(valueJobJson)

    if(keyJobJson == "lastBuild"):
        job.setLastBuild(valueJobJson)

    if(keyJobJson == "builds"):
        #dict
        #Builds
        job.setBuild(valueJobJson)
        print(keyJobJson)
        for builds in valueJobJson:
            for keyBuilds,valueBuilds in builds.items():
                if type(valueBuilds) == list:
                    #SubBuilds
                    print("     "+keyBuilds)
                    for subBuildsAndCauses in valueBuilds:
                        for keySubBuildsAndCauses,valueSubBuildsAndCauses in subBuildsAndCauses.items():
                            if(keySubBuildsAndCauses == "causes"):
                                print("         "+keySubBuildsAndCauses)
                            elif(keySubBuildsAndCauses != "_class"):
                                print("         "+keySubBuildsAndCauses+": "+str(valueSubBuildsAndCauses))
                            if type(valueSubBuildsAndCauses) == list:
                                for causes in valueSubBuildsAndCauses:
                                    for keyCauses,valueCauses in causes.items():
                                        if(keyCauses != "_class"):
                                            print("             "+keyCauses+": ",valueCauses)
                else:
                    if(keyBuilds != "_class"):
                        print("     "+keyBuilds+": ",valueBuilds)
            print("-----------------------------------------------------------------------------------------------------")

    if(keyJobJson == "lastSuccessfulBuild"):
        job.setLastSuccessfulBuild(valueJobJson)

    if(keyJobJson == "lastUnsuccessfulBuild"):
        job.setLastUnsuccessfulBuild(valueJobJson)

    def imprimeBuild(build):
        if hasattr(build, 'number'):
            print("         Number: "+str(build.number))
        if hasattr(build, 'result'):
            print("         Result: "+build.result)
        if hasattr(build, 'duration'):
            print("         Duration:"+str(build.duration))
        if hasattr(build, 'timestamp'):
            print("         Timestamp: "+str(build.timestamp))

print("JOB:")
print("     Nome: "+job.name)
print("     Habilitado: " +str(job.buildable))
print("     Health Report: ")
print("         Description: "+job.healthReport.description)
print("         Score: "+str(job.healthReport.score))
print("     LastBuild:")
imprimeBuild(job.lastBuild)
print("     LastSuccessfulBuild:")
imprimeBuild(job.lastSuccessfulBuild)
print("     lastUnsuccessfulBuild:")
imprimeBuild(job.lastUnsuccessfulBuild)
