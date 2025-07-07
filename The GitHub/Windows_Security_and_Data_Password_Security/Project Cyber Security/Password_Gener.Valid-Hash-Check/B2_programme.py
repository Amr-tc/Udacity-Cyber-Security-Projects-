#Defined variables
cri1 = 0
cri2 = 0
cri3 = 0
cri4 = 0
pass_scr = "None"
def pass_valid(inputpass):
    #Global was used to replace return
    global cri1, cri2, cri3, cri4
    #Check Password lenght
    if len(inputpass) >= 12:
        cri1 += 1
    #Check Password Upper cases
    for char in inputpass:
        if char.isupper():
            cri2 += 1
    #Check Password lower cases       
    for char in inputpass:
        if char.islower():
            cri3 += 1
    #Check Password Digits
    for char in inputpass:
        if char.isdigit():
            cri4 += 1
#Password input
input_pass = input("Enter Your password: ")
pass_valid(input_pass)

#Conditional if for checking all criteria
if cri1 != 0 and cri2 != 0 and cri3 != 0 and cri4 != 0:
    pass_scr = "Complaint"
    print (pass_scr)
#else Conditional for weak Passwords
else:
    print ("Non-Compliant","Your Password Should Contain :")
    if cri1 == 0:
        print ("--> 12 characters or more")
    if cri2 == 0:
        print ("--> UPPER CASES")
    if cri3 == 0:
        print ("--> lower cases")
    if cri4 == 0:
        print ("--> digits")
