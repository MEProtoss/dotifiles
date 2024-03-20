class car:
    year = 2023
    mpg = 30
    speed = 55


    def accelerate(self):
        car.speed = min (car.speed +5,120)
        return car.speed


    def brake(self):
        car.speed = min (0,car.speed-10)
        return car.speed


car1= car()
print(car1.speed)
car1.accelerate()
print(car1.speed)
car1.brake()
print(car.speed)
