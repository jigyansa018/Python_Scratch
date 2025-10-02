def greetHello(name , ending): 
    #def is a reserve keyword
    print("Hello " +  name)
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print(ending)

#letter generator
def letterGenerator(name , date):
    st = f"Hi mam,\n This is {name} and I will not come to school on {date}"
    print(st)

#avaerage value
def average(a,b):
    return (a+b)/2

print("Execution function...")
greetHello("Isha" , "Thank you")
letterGenerator("Isha" , "2nd October")
print(average(3 , 4))
print("done")