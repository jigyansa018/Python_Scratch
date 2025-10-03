s = "Isha is a good girl"


with open("test.txt" , "w") as f:
    f.write(s)  
# with is a context manager
# test.txt is file Name
# w is a mode
# there are 3 types of mode such as read,write,append


fp = open("test.txt" , "w")
fp.write(s)
fp.close()
# fp is the file object here.

# Using append mode
with open("test.txt", "a") as f:
    f.write(s + "\n")   # Adding a newline so each write is separate
