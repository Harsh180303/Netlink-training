'''
class Ai_model:
    def __init__(self, algo, provider):
        self.algo = algo
        self.provider = provider

    def get_details(self,):
        print(f"machine learning algorithm: {self.algo}")
        print(f"provider is: {self.provider}")

class ChatGPT(Ai_model):
    def __init__(self, algo, provider, model_name, token_limit):
        super().__init__(algo, provider)
        self.model_name = model_name
        self.token_limit = token_limit

    def get_model_details(self):
        print()
        self.get_details()
        print(f"Model name is {self.model_name}")
        print(f"{self.model_name}'s token limit is {self.token_limit}")


algo = input("Enter machine learning algorithm: ")
provider = input("Enter provider name of your ai: ")
model_name = input("Enter model name: ")
token = input("Enter the token limit: ")

my_ai_agent = ChatGPT(algo, provider, model_name, token)
my_ai_agent.get_model_details()
'''


'''
class Payment_gateway:
    def __init__(self, receiver, sender, transection_Id, amount):
        self.receiver = receiver
        self.sender = sender
        self.transection_Id = transection_Id  # dynamic
        self.amount = amount
    
    def get_information(self):
        print(f"{self.sender} paid Rs. {self.amount} to {self.receiver} and transection ID is {self.transection_Id}")

class UPI(Payment_gateway):
    def __init__(self, receiver, sender, transection_Id, amount, cashback, transections_left):
        super().__init__(receiver, sender, transection_Id, amount)
        self.cashback = cashback    # dynamic 
        self.transections_left = transections_left  # dynamic 
    
    def get_all_information(self):
        self.get_information()
        print(f"{self.sender} got Rs. {self.cashback} cashback and has {self.transections_left} transections left.")

sender = input("Enter sender's name: ")
reciever = input("Enter reciever's name: ")
amount = int(input("Enter the amount to be paid: "))
transection_id = int(input("your transection id: "))  # dynamic 
cashback = int(input("Cashback recieved: "))    # dynamic 
transections_left = int(input("No. of transection left: "))  # dynamic 
payment = UPI(reciever, sender, transection_id, amount, cashback, transections_left)
payment.get_information()
print("=============================== Full infromation ===============================")
payment.get_all_information()
'''

'''
class IOT_devices:
    def __init__(self, deviceId, name):
        self.id = deviceId
        self.name = name

    def basic_details(self):
        print(f"Device Id is: {self.id}")
        print(f"Name is: {self.name}")

class AC(IOT_devices):
    def __init__(self, deviceId, name, temperature):
        super().__init__(deviceId, name)
        self.temp = temperature

    def get_all_details(self):
        self.basic_details()
        print(f"And temperature is: {self.temp}")

device = AC(183249845, "AC", 26)
device.get_all_details()
'''