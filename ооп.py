
class Tesla:
    a = 0
    power = 580
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    def get_power_Tesla(self):
        print(f'battery level of tesla is {Tesla.power}')
        if Tesla.power == 580:
            print('battery of Tesla id full now')
    def charge_Tesla(self):
        while Tesla.power < 580:
            Tesla.power +=1
        print('charging required')
    def driving(self):
        while Tesla.power > 0:
            Tesla.power -=1
            print('car rides')
            if Tesla.power == 240:
                print('car need to be charged')
                Tesla.a = int(input(': '))
                if Tesla.a == 1:
                    print('car started to charge')
                    Tesla.charge_Tesla(self)
                    break
                else:
                    print('car keeps moving')
                    Tesla.power -=1
        print('car is empty')
    def light(self):
        Tesla.power -=1
        print('light is on')
    def windscreen(self):
        Tesla.power -=1
        print('windscreen is on')
car1=Tesla('Tesla','S','2009')
car1.light()
car1.windscreen()
car1.get_power_Tesla()
car1.driving()
del car1




