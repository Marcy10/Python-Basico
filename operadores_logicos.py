# variables 
num1 =2 
num2 = 2
#OL 
#AND 
print(num1 == num2 and num1 <= num2) # 1 1 - V 
print(num1 == num2 and num1 > num2) # 1 0 - V 
print(num1 < num2 and num1 > num2)# 0 0 - F 
print(num1 < num2 and num1 >= num2) # 0 1 - F 

#ejemplo1 
usuario = input ("digite el usuario:") 
contraseña = input (" digite la contraseña:")
#ADN 
print( usuario== "marcylozano15"and contraseña == "Marcy2006+") 


#OR 
print(num1 == num2 or num1 <= num2) # 0 1 - V 
print(num1 <= num2 or num1 > num2) # 1 0 - V 
print(num1 > num2 or num1 > num2)# 0 0 - F 
print(num1 > num2 or num1 >= num2) # 0 1 - F 

#NOT 
print(not True) #F
print(not False)#V
