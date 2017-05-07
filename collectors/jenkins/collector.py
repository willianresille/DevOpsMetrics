import json
from object.job import Job

job = Job()
with open('Formatted JSON.json') as data_file:
    job_json = json.load(data_file)

for keyJobJson,valueJobJson in job_json.items():

    if(keyJobJson == "name"):
        job.setName(valueJobJson)
        print("Nome: "+job.name)

    if(keyJobJson == "buildable"):
        job.setBuildable(valueJobJson)
        print("Habilitado: " +str(job.buildable))

    if(keyJobJson == "healthReport"):
        print("Health Report: ")
        job.setHealthReport(valueJobJson)
        print("     Description: "+job.healthReport.description)
        print("     Score: "+str(job.healthReport.score))

    if(keyJobJson == "lastBuild"):
        print("Ultimo Build: ")
        for keyLastBuild,valueLastBuild in valueJobJson.items():
            if(keyLastBuild != "_class"):
                print("     "+keyLastBuild+": ",valueLastBuild)

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
        #dict
        print("Ultimo Build com Sucesso: ")
        if(type(valueJobJson) == dict):
            for k,y in valueJobJson.items():
                if(k != "_class"):
                    print("     "+k+": ",y)
        else:
            print("         "+str(valueJobJson))

    if(keyJobJson == "lastUnsuccessfulBuild"):
        #dict
        print("Ultimo Build sem sucesso: ")
        if(type(valueJobJson) == dict):
            for k,y in valueJobJson.items():
                if(k != "_class"):
                    print("     "+k+": ",y)
        else:
            print("         "+str(valueJobJson))
    #print("\n")
