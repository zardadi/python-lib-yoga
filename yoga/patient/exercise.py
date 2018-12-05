#file Exercise.py

class Exercise():
    _registery = []
    def __init__(self, name, time):
        self._registery.append(self) 
        self.name=name
        self.time=time
    def display(self):
        print("Name of exercise: ", self.name)
        print("Time of exercise in minutes: ", self.time)
        return(0)