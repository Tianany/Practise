class Car:
    def check_superCar_jalopy_familysedan(self):
        if self.topspeed >= 250:
            return "there car is a super car"
        elif self.topspeed <= 100:
            return "the car is jalopy"
        else:
            return "the car is family sedan"

        def __init__( self , make ,model, topspeed):
            self.make = make
            self.model = model
            self.topspeed = topspeed
car1 = Car('toyota','hilux', 300)
done1 =car1.check_superCar_jalopy_familysedan()
print("car make is ",car1.make)
print("car model is ",car1.model)
print(" car topspeed is ",car1.topspeed)
print(done1)







