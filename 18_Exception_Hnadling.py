try:
    a  = int(input("Enter your number: "))
    print(a + 3)
except Exception as e:
    print("some error ocurred: ",e)
    #if error posibility ocuured then used try except 