#input the filename:
a=(input("Input the filename:"))
#identify file type
import pathlib
ext = pathlib.Path(a).suffix

#print file type
print("The extension of the file is:",ext)

   
            

