#Strings concantenation
youtuber = "name" #some string variable

# a few ways to do this
n = 0
print("subscribe to " + youtuber, n)
n = n+1
print("subscribe to {}" .format(youtuber), n)
n=n+1
print(f"subscribe to {youtuber}{n}")

adj = input("enter adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is {adj}! It is because {verb1}. Stay hydrated like {verb2} and \
    {famous_person}!"
print(madlib)
    

