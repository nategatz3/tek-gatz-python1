from Arithmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes associated with the user’s username, password, registration date, and more. Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

#TODO: create several more instance of the Arithmetic class and add different values

addition = ar.add()

addition

division = ar.divide()

division

remainders = ar.remainder()

remainders

multiplication = ar.multiply()

multiplication

bigproblem = ar.add() * ar.multiply()

bigproblem

alltogether = (ar.add() * ar.multiply()) / (ar.divide() - ar.multiply())

alltogether

mathiscool = (ar.divide() - ar.multiply())**2 / (ar.add() * ar.multiply()) * 0.5

mathiscool

goingforitall = ((ar.divide() - ar.multiply()**2) / (ar.add() * ar.multiply()) * 0.5 * 62 / (ar.multiply() / 5)) * ar.divide()

goingforitall