name="joy"
if(len(name)==2):
    print("failed")
    
else:
    if(len(name)<3):
        print("the name length must be miximum 3")
    else:
        print("success")


name="hare"
if(len(name)==3):
    print("failed")
else:
    if(len(name)>3):    
       print("the name length must be 3")
    else:
        print("success")



name="m"
phone=""
if(len(name)==0 or len(phone)==0):
    print("true")

name="krishna"
phone="01245"
email="565"
if(len(name)==0 or len(phone)==0 or len(email)==0):
    print("failed")
else:
     if(len(name)<2):
         print("the name must be minimum 2")
     elif(len(phone)!=11):
         print("the phone number size must be equal to 11")
     elif(len(email)>3):
         print("the email length must be maximus 3")
     else:
         print("success")

name="sree"
phone="01747862417"
if(len(name)==0 or len(phone)==11):
    print("the phone number must be equal to 11")
else:
     print("success")


name="trilaksha"
phone="014585"
if(len(name)<2 or len(name)>8):
    print("the name length must be between 2 and 8")
else:
    print("success") 
