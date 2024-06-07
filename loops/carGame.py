"""Car Game"""


def query_help():
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")


def car_game():
    while(True):
        query = input("Enter Car 🚗 command : ").lower()
        status = 'stop'
        if query == 'help':
            query_help()
        elif query == 'start':
            if status == 'stop':
                status = 'start'
                print("Car has Started ")
            elif status == 'start':
                print("Car is already started")
        elif query == 'stop':
            if status == 'start':
                status = 'stop'
                print("Car stopped")
            elif status == 'stop':
                print("Car is already stopped")
        elif query == 'quit':
            return
        else:
            print("Wrong Input Enter again")


if __name__ == '__main__':
    car_game()
    print("Exited Game 🎮")
