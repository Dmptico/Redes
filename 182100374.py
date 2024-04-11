vlan = int(input("Ingrese el numero de la VLan porfavor:"))

vlanswitch1 = [10,20,30,99]
vlanswitch2 = [40,50,60,200]

if vlan in vlanswitch1:
	print("La VLAN pertenece al Switch 1")
else:
	print("la VLAN no pertenece al Switch 1")
if vlan in vlanswitch2:
	print("La VLAN pertenece al Switch 2")
else:
	print("La VLAN no pertence al Switch 2")
