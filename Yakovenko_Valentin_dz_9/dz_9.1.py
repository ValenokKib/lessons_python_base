from time import sleep

class Trafficlight:
    __color = 'Black'

    def running(self):
        while True:
            print('red')
            sleep(7)
            print('yellow')
            sleep(2)
            print('green')
            sleep(7)
            print('yellow')
            sleep(2)

a = Trafficlight()
a.running()