try:
    aList = [1,2,3]

    print(aList[3])

#except(IndexError, NameError)
except IndexError:
    print("Sorry that index doesn't exist")

except:
    print("An Unknown error occured")