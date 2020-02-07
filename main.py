import shelve
import os
import glob

def mainInterface():
  print("RQL v1.0.1-dev")
  command = (input(">"))
  if command == "create":
    nstar_system = input("Name for new Star:") 
    d = shelve.open(nstar_system + ".star")
    mainInterface()
  elif command == "store":
    sStarSystem = input("What Star do you want to store in?")
    d = shelve.open(sStarSystem)
    sPlanet = input("Which planet?")
    dataTW = input("What to store:")
    d[sPlanet] = dataTW
    d.close
    mainInterface()
  elif command == "view":
    vStarSystem = input("What Star to view?") 
    d = shelve.open(vStarSystem + ".star")
    vPlanet = input("Planet to view?")
    vdata = d[vPlanet]
    print(vdata)
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "index planet":
    iStarSystem = input("What Star to view?") 
    d = shelve.open(iStarSystem + ".star") 
    klist = list(d.keys())
    print(klist)
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "delete":
    dStarSystem = input("What Star to open?") 
    d = shelve.open(dStarSystem + ".star")
    dKey = input("What Planet to delete?")
    del d[dKey]
    print("Deleted.")
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "where":
    qStar = input("What Star to Query?")
    d = shelve.open(qStar + ".star")
    qString = input("Search term:")
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




    

mainInterface()