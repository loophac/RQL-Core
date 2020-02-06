import shelve

def mainInterface():
  print("RQL v1.0.0.")
  command = (input(">"))
  if command == "create":
    nstar_system = input("Name for new Star System:") 
    d = shelve.open(nstar_system)
    mainInterface()
  elif command == "store":
    sStarSystem = input("What Star System do you want to store in?")
    d = shelve.open(sStarSystem)
    sPlanet = input("Which planet?")
    dataTW = input("What to store:")
    d[sPlanet] = dataTW
    d.close
    mainInterface()
  elif command == "view":
    vStarSystem = input("What Star System to view?") 
    d = shelve.open(vStarSystem)
    vPlanet = input("Planet to view?")
    vdata = d[vPlanet]
    print(vdata)
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "index":
    iStarSystem = input("What Star System to view?") 
    d = shelve.open(iStarSystem) 
    klist = list(d.keys())
    print(klist)
    input("Press Enter to Continue...")
    mainInterface()
  elif command == "delete":
    dStarSystem = input("What Star System to open?") 
    d = shelve.open(dStarSystem)
    dKey = input("What Planet to delete?")
    del d[dKey]
    print("Deleted.")
    input("Press Enter to Continue...")
    mainInterface()


    

mainInterface()