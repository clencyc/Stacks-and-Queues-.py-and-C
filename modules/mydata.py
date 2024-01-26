#1. Create a file name mydata
#2. Use what you learned in part 8 to find out
#      how to open a file without with (Open in try)
#3. Catch FileNotFoundError
#4. In else print contents
#5. In finally
#6. Open nonexistent file mydata3
try:
    myFile = open("mydata2", encoding="utf-8")

except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else:
    print("File :", myFile.read())
    myFile.close()

finally:
    print("Finished working with File")