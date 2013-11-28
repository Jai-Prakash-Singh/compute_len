#/usr/bin/env python 



def compute_len(s):
    length = 0 
    for index in s:
        length += 1
    return length 



if __name__ == "__main__":
    try:
        choice = int(raw_input(" Enter 1 for string  and 2 for List: "))
	if choice == 1:
	    string  = str(raw_input(" Enter a string: "))
	    length = compute_len(string)
	    print " The length of given string is %d"%(length)
	elif choice == 2:
	    loop = "y"
	    lst = []
	    i = 1
	    while loop == "yes" or loop =="y":
	        element = str(raw_input("enter %d element: "%i))
		lst.append(element)
		i += 1
		loop = raw_input(" want to add more element ? y/n: ")
		loop = loop.lower()
            print lst
	    length = compute_len(lst)
	    print " The length of given string is %d"%(length)
        else:
	    print " you entered wrong choice"
    except:
        print " error in input"



	    

