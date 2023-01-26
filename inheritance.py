class Animal:
    def speak(self):
        print("every animal speaks in different ways")
class dog(Animal):
    def speak(self):
        print("dog barks as bow-bow")
class cat(Animal):
    def speak(self):
        print("cat says meow-meow")
class pig(Animal):
    def speak(self):
        print("pig says wee-wee")
a=Animal()
a.speak()
d=dog()
d.speak()
c=cat()
c.speak()
p=pig()
p.speak()
