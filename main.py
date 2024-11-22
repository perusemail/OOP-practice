class device:
    def __init__(self,name):
        self.name = name
    def power_on(self):
        print("power on")

class computer(device):
    def open_file(self):
        print("file opened")

x = device("Phone")
z = computer("abc")
