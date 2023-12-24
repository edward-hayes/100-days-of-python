try: 
    file = open("test.file")
except:
    open("test.txt","w")
else:
    print("open failed")