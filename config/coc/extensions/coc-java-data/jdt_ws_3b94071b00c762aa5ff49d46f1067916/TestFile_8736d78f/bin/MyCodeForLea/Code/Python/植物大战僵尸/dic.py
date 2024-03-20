class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def play(self):
        print("my name is",self.name)
        print("i am",self.age,"years old")
# 继承哪个子类就在括号里填入父类的名字）
class Dog(animal):
    def __init__(self):
        super(Dog,self).__init__("qq",13)
    def say(self):
        self.play()
dog1=Dog() 
dog1.say()
print(isinstance(dog1,Dog))