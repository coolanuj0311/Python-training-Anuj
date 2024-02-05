class Temp_Celsius:
    def __init__(self,temperature=0):
        print("Assigning temperature value")
        self._temperature=temperature
    def convert_to_fahrenheit(self):
        return (self.temperature*1.8)+32
    def get_temperature(self):
        print("Getting temperature value")
        return self._temperature
    def set_temperature(self,value):
        if value<-273:
            raise ValueError('Temperature below -273 is not possible')
        print("Setting temperature value")
        self._temperature=value
    temperature=property(get_temperature,set_temperature)
c=Temp_Celsius(5)
print(c.temperature)
c.temperature=100
print(c.temperature)
print(c.__dict__["_temperature"])
print(c.__dict__["temp"])

class Celsius:
    def __init__(self,temperature=0):
        self.temperature=temperature
    def to_fahrenheit(self):
        return (self.temperature*1.8)+32
    @property
    def temperature(self):
        print("Getting value")
        return self._temperature
    @temperature.setter
    def temperature(self,value):
        if value< -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature=value
c=Celsius(5)
print(c.temperature)
c.temperature=100
print(c.temperature)


