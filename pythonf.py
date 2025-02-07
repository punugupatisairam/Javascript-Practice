# print("this is sairam")
# a = 20
# b = 30
# print("add",a+b)

#bigger from both numbers
# if a>b:
#         print("a is bigger")
# else:
#         print("b is bigger")


#1)
# def myfun():
#     print("this is priamry function")
# myfun()

#2)
# def getting(value):
#     print("value of argument" + value)
    
# getting("data")

#3)
# def function(a,b):
#     return a+b
# res = function(2,3)
# print("addition is ",res)

#4)
# def multiple(first,second):
#     print("multiple parameters",first +" "+second)
# multiple("sairam","sudhakar")

#5)
# def multipleargs(**args):
#     print("when you don't know how many args passing",args["a"],args["c"])
# multipleargs(a="paul",b="joseph",c="peter")

#6)
# def param(country = "u.s"):
#     print("it's a function call of " + country)

# param("israel")  # Output: it's a function call of israel
# param("canada")  # Output: it's a function call of canada
# param()          # Output: it's a function call of u.s (default value used)
# param("u.k")     # Output: it's a function call of u.k

#7)

# def listof(fruites):
#     for f in fruites:
#         print(f)
# deliciouslist = ["banana","apple","custard apple","kiwi"]
# listof(deliciouslist)

#8)
def tupleof(animals):
    for ani in animals:
        print("animals is",ani) 
tupleani = ("dog","cat","rat","insuct","bactiria")
tupleof(tupleani) 

#9)
def dictionary(birds):
    for b in birds:
        print(b)
birdsdic = ({"elijah":"crow","noah":"pegions"})
dictionary(birdsdic)
