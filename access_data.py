import pickle
import json

def saveData(format,file,data):
    if format.lower()=='binary' or format.lower()=='bin':
        try:
            with open(file, mode="wb") as pickleFile:
                pickle.dump(data, pickleFile)
        except:
            print("File Not Found.")

    elif format.lower()=='text' or format.lower()=='txt':
        try:
            with open(file, mode="w") as jsonFile:
                json.dump(data,jsonFile,indent=4)
        except:
            print("File Not Found.")

def loadData(format,file):
    if format.lower()=='binary' or format.lower()=='bin':
        try:
            with open(file, mode="rb") as pickleFile:
                data = pickle.load(pickleFile)
                return data
        except:
            print("File Not Found.")

    elif format.lower()=='text' or format.lower()=='txt':
        try:
            with open(file) as jsonFile:
                data=json.load(jsonFile)
                return data
        except Exception as e:
            print(e)
            print("File Not Found.")    
    else:
        print("Format must be either text or binary.")