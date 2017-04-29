import json

with open('Formatted JSON.json') as data_file:
    job_json = json.load(data_file)

for keyJobJson,valueJobJson in job_json.items():

    if(keyJobJson == "name"):
        print("Nome: "+valueJobJson)

    if(keyJobJson == "buildable"):
        print("Habilitado: " +str(valueJobJson))

    if(keyJobJson == "healthReport"):
        print("Health Report: ")
        for healthReport in valueJobJson:
            for key,value in healthReport.items():
                if(key != "_class"):
                    print("     "+key+": ",value)

    if(keyJobJson == "lastBuild"):
        print("Ultimo Build: ")
        for keyLastBuild,valueLastBuild in valueJobJson.items():
            if(keyLastBuild != "_class"):
                print("     "+keyLastBuild+": ",valueLastBuild)

    if(keyJobJson == "builds"):
        #dict
        #Builds
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
