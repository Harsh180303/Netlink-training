class Addition:
    def __init__(self):
        self.num1 = 5
        self.num2 = 6

    def getnum(self):
        new_num = self.num1 + self.num2
        return new_num
    

add = Addition()
print(add.getnum())