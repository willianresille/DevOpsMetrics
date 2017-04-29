import pdb
import json


from pprint import pprint

with open('Formatted JSON.json') as data_file:
    data = json.load(data_file)

#pprint(data)

#name_job = str(data['name'])
#job_enable = str(data['buildable'])
#print("Nome do Job: " + name_job)
#print("Habilitado: " +job_enable)
#print("     Builds:")
#print("             Iniciado por:" +str(data[builds[actions[userName]]]))


for k,v in data.items():
    #print(k+": ",v)
    #if(k == "name"):
        #print("Nome: "+v)
    #if(k == "buildable"):
        #boolean
        #print("Habilitado: " +str(v))
    #if(k == "healthReport"):
        #dict
        #print("Health Report: " +str(v))
    #if(k == "lastBuild"):
        #dict
        #print("Ultimo Build: " +str(v))
    if(k == "builds"):
        #dict
        #pprint(v)
        for item in v:
            #print(item)
            for k1,k2 in item.items():
                if type(k2) == list:
                    #print(k2)
                    for item2 in k2:
                        for l1,l2 in item2.items():
                            print("         "+l1+": ",l2)
                            if type(l2) == list:
                                for t1 in l2:
                                    for key,value in t1.items():
                                        print("             "+key+": ",value)
                                    print("#########################################################################")
                    print("-----------------------------------------------------------------------------------------------------")
                else:
                    print("     "+k1+": ",k2)
                #print("\n")



        #print("Builds: " + str(json_data))
    #if(k == "lastSuccessfulBuild"):
        #dict
        #print("Ultimo Build com Sucesso: " +str(v))
    #if(k == "lastUnsuccessfulBuild"):
        #dict
        #print("Ultimo Build sem sucesso: " + str(v))
    #print("\n")
