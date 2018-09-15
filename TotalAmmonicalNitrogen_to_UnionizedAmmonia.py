Temp = float(input("Please enter temperature in Fahrenheit"))
Sal = float(input("Please enter salinity in PPT"))
pH = float(input("Please enter pH"))
NH3 = float(input("Please enter Total Ammoniacal Nitrogen (TAN)"))

Kelvin = ((Temp+459.67)*5/9)
## "I" simply accounts for the concentration of solutes (typically salt) in the water
I = ((19.9273*Sal)/(1000-(1.005109*Sal)))
pka = (9.245 +(.116*I))
lolmath = (pka+0.0324*(298-Kelvin)+(.0415/Kelvin)-pH)
lolmath2_the_mathenning = ((1/(1+10**lolmath))*NH3)
print (lolmath2_the_mathenning)
