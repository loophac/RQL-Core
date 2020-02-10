import shelve
#import os
import glob

def mainInterface():
  print("RQL v1.0.1")
  command = (input(">"))
  if command == "create":
    nstar_system = input("Name for new Star:\n>") 
    d = shelve.open(nstar_system + ".star")
    mainInterface()
  elif command == "help":
    print('''RQL v1.0.1 \n create - makes a new star \n store - stores data in planet. Creates planet if not made, overwrites star otherwise.\n view - view the data in a planet \n ''')
  elif command == "store":
    sStarSystem = input("What Star do you want to store in?\n>")
    d = shelve.open(sStarSystem + ".star")
    sPlanet = input("Which planet?\n>")
    planetBuffer = ""
    d[sPlanet] = planetBuffer
    dataTW = input("What would you like to store?\n>")
    temp = list(d[sPlanet]) 
    temp.append(dataTW)
    d[sPlanet] = temp
    d.close
    mainInterface()
  elif command == "view":
    vStarSystem = input("What Star to view?\n>") 
    d = shelve.open(vStarSystem + ".star")
    vPlanet = input("Planet to view?\n>")
    vdata = d[vPlanet]
    print(vdata)
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "index planet":
    iStarSystem = input("What Star to view?\n>") 
    d = shelve.open(iStarSystem + ".star") 
    klist = list(d.keys())
    print(klist)
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "delete":
    dStarSystem = input("What Star to open?\n>") 
    d = shelve.open(dStarSystem + ".star")
    dKey = input("What Planet to delete?\n>")
    del d[dKey]
    print("Deleted.")
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "where":
    qStar = input("What Star to Query?\n>")
    d = shelve.open(qStar + ".star")
    qString = input("Search term:\n>")
    qList = list(d.keys())
    qPlanetResult = [s for s in qList if any(xs in s for xs in qString)]
    #qData = d[qPlanetResult]  
    #qDataResult = qData.find(qString) 
    print(qPlanetResult)
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "index star":
    sList = glob.glob("*.star")
    print(sList)
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "ammend":
    aStarSystem = input("What Star to view?\n>")
    d = shelve.open(aStarSystem + ".star", writeback=False)
    aPlanet = input("Which planet to amend?\n>")
    aData = input("What would you like to ammend?\n>")
    temp = list(d[aPlanet]) 
    temp.append(aData)
    d[aPlanet] = temp  
    mainInterface()






    

mainInterface()