import math

#for calculating volume of water in a cylindrical aquarium

Radius = float(input("Please enter the radius of the container in inches"))
Height = float(input("Please enter the height of the container in inches"))
Volume = ((3.1415*(Radius*Radius)*Height)*0.004329)

print (Volume)
