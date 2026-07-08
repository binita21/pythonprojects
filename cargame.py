command = ""
started = False
stopped = False
while command != 'quit':
    command = input("Enter state of your car:")
    if command == 'start':
        if started:
            print("Car already started.")
        else:
            print("Car started!! Ready to go.")

    elif command == 'stop':
        if not stopped:
            print("Car stopped.")
        else:
            print("Car already stopped...")
    elif command == 'quit' :
        print("exit")
    elif command == 'help':
        print("car_state = start-----> To start the car.")
        print("car_state = stop -----> To stop the car.")
        print("car_state = quit -----> To exit.")
    else:
        print("No such commands.")
