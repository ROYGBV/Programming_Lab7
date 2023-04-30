class device(object):
    def __init__(self, wattage, voltage):
        self.wattage = wattage
        self.voltage = voltage

    def parameters(self):
        return("The device consumes {} Watt".format(self.wattage)
               + '\n' + "The device requires a {} Volt socket".format(self.voltage) + "\n")

class kettle(device):
    def __init__(self, wattage, voltage):
        super().__init__(wattage, voltage)

    def turn_on(self):
        print("The button has been pushed")
        print(self.__boil(), self.__check_temp(), self.__beep(), self.__turn_off(), '', sep="\n")

    def __boil(self):
        return("Warming up the water")

    def __check_temp(self):
        return("Checking the water temperature")

    def __beep(self):
        return("Beep sound")

    def __turn_off(self):
        return("Automatic shutdown")

class microwave(device):
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

print("--Microvave--")
m = microwave(700, 240)
m.turn_on()
print(m.parameters())

print("--Kettle--")
k = kettle(300, 240)
k.turn_on()
print(k.parameters())