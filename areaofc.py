#circle
#get input radius of the circle
r=int(input("Input the radius of the circle:"))
#calculate the area of the circle
a=3.14159*r**2
#diplay the area of the circle
print("The area of the circle with radius",r,"is",a)


#extension
import os


# this will return a tuple of root and extension
split_tup = os.path.splitext('my_file.txt')
print(split_tup)

# extract the file name and extension
file_name = split_tup[0]
file_extension = split_tup[1]

print("Input the Filename: ", file_name)
print("The File extension of the file is: ", file_extension)

