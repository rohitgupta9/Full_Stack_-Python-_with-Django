

def ckecktuple(tuple1):

	ele = tuple1[0]
	chk = True
	
	# Comparing each element with first item
	for item in tuple1:
		if ele != item:
			chk = False
			break;
			
	if (chk == True): print("value Are same")
	else: print("value are Different")			

# Driver Code
tuple1 = ['iNeuron', 'iNeuron', 'iNeuron', 'iNeuron', ]
ckecktuple(tuple1)
