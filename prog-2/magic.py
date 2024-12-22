class animal:
    def speak():
       pass
class dog (animal):
    def speak(self):
        return ('woof')  
    def __str__(self):
        return ('dog')

      
class cat (animal):
    def speak(self):
        return ('meow')
    def __str__(self):
        return 'cat'

class cow (animal):
    def speak(self): 
        return ('mooo') 
    def __str__(self):
        return 'cow'

def display(animals):
    for animal in animals:
        print(f'{animal} : {animal.speak()} '  )  


animals=[dog(),cat(),cow()]
print(display(animals))