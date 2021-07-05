command = ""
isStarted = False

while True:
    command = input("> ").lower()
    
    if command == "start":
        if isStarted:
            print("Car is already Started...")
        else:
            isStarted = True
            print ("Car started...")
    elif command == "stop":
        if not isStarted:
            print("Car is already stopped..")
        else:
            isStarted = False
            print("Car Stopped...")
    elif command == "help":
        print("""
Start - to start the car
Stop - to stop the car
quit - to quit 
        """)
    elif command == "quit":
        break
    else:
        print("Sorry!, I don't understand that")