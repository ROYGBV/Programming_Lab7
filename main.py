class device(object):   #родительский класс
    def __init__(self, wattage, voltage):   #потребляемая мощность прибора и требуемое напряжение сети(120 В/240 В)
        self.wattage = wattage
        self.voltage = voltage

    def parameters(self):   #вывод мощности прибора и напряжения сети
        return("The device consumes up to {} Watt".format(self.wattage)
               + '\n' + "The device requires a {} Volt socket".format(self.voltage) + "\n")

class kettle(device):   #дочерний класс чайника, наследует wattage, voltage, функцию parameters
    def __init__(self, wattage, voltage):
        super().__init__(wattage, voltage)

    def turn_on(self):  #данная функция получает доступ к приватным функциям с двумя нижними подчёркиваниями(инкапсуляция)
        print("The button has been pushed")
        print(self.__boil(), self.__check_temp(), self.__beep(), self.__turn_off(), '', sep="\n")

    def __boil(self):   #эту и последующие функции с двумя нижними подчёркиваниями крайне не рекомендуется запускать, дабы не поломать программу(инкапсуляция)
        return("Warming up the water")

    def __check_temp(self):
        return("Checking the water temperature")

    def __beep(self):
        return("Beep sound")

    def __turn_off(self):
        return("Automatic shutdown")

class microwave(device):    #дочерний класс микроволновки
    def __init__(self, wattage, voltage):
        super().__init__(wattage, voltage)

    def turn_on(self):
        self.time = int(input("Type the time for warming up the content in minutes: "))
        while True:
            curwat = int(input("Type the necessary power in Watt(between 1 and {}): ".format(self.wattage)))
            if 1 <= curwat <= self.wattage:
                self.curwat = curwat
                break
            else:
                print("Invalid value!")
        print("Time and power have been set")
        print("Closing the door")
        print(self.__magnetron_start(), self.__wait(), self.__beep(), self.__turn_off(), '', sep="\n")

    def __magnetron_start(self):
        return("Turning on the magnetron")

    def __wait(self):
        return("Waiting for {} minutes".format(self.time))

    def __beep(self):
        return("Beep sound")

    def __turn_off(self):
        return("Automatic shutdown")

#для классов чайника и микроволновки можно использовать функции turn_on и parameters(полиморфизм)

print("--Microvave--")
m = microwave(700, 240)
m.turn_on()
print(m.parameters())

print("--Kettle--")
k = kettle(300, 240)
k.turn_on()
print(k.parameters())
