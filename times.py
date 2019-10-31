def table():
	usr= input("Please enter number for your multiplication table >> ")
	usr = int(usr)
	
	for i in range(30): 
	    
	    ans = i*usr
	    print("%s x %s = %s" %(usr, i, ans))
	input("Press Enter")
table()
