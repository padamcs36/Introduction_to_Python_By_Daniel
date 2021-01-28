class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False #Initially TV is Off

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if self.on and 1 <= self.channel <= 120:
            self.channel = channel

    def getVolumeLevel(self):
        return  self.volumeLevel

    def setVolume(self, volumeLevel):
        if self.on and 1 <= self.volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1
    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1

def main():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)

    tv2 = TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.volumeUp()
    tv2.volumeDown()

    print(f"tv1 channel is {tv1.getChannel()} and volume is {tv1.getVolumeLevel()}")
    print(f"tv2 channel is {tv2.getChannel()} and volume is {tv2.getVolumeLevel()}")
    # print(f"set to channel number {tv1.setChannel(121)}") None
main() #calling main method.