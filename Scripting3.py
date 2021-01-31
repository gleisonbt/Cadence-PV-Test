
#Insert here the password
password = "@Bruna_Ramos29/01*"

#Insert here the requirements
req = [('LEN', '>', 8), ('LETTERS', '=', 10), ('NUMBERS', '<', 7), ('SPECIALS', '>', 2)]

def password_validation(password,req):

    valid_password = True

    LEN, LETTERS, NUMBERS, SPECIALS = 0, 0, 0, 0

    LEN = len(password)

    for each in password: 
      
        # counting letters  
        if each.islower() or each.isupper(): 
            LETTERS += 1
       
        # counting digits 
        if each.isdigit(): 
            NUMBERS += 1            
      
        # counting special characters
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if each in special_characters: 
            SPECIALS += 1           

    #print(LEN, LETTERS, NUMBERS, SPECIALS) #If you want to print the results of password's type of characters

    #loop for each requirement in req if password is still valid
    for each_req in (each_req for each_req in req if valid_password):
        (first_value, second_value, third_value) = each_req
       
        #get the first_value and insert the content of the variable name in a aux variable named req1
        if first_value == 'LEN':
            req1 = LEN
                
        if first_value == 'LETTERS':
            req1 = LETTERS
            
        if first_value == 'NUMBERS':
            req1 = NUMBERS
            
        if first_value == 'SPECIALS':
            req1 = SPECIALS
   
        #get the comparison symbols and comparing the requirements with the password info                          
        if second_value == '<':
            if not req1 < third_value:
                valid_password = False

        if second_value == '>':
            if not req1 > third_value:
                valid_password = False

        if second_value == '=':
            if not req1 == third_value:
                valid_password = False                
             

    if valid_password:
        #print("Valid Password")
        return True
    else:
        #print("Invalid Password")
        return False

        
#test function
def test_password_validation():

    #Tests for one specific password and multiple reqs
    password = "@Bruna_Ramos29/01*" #LEN 18, LETTERS 10, NUMBERS 4, SPECIALS 4  
    
    valid_req = [[('LEN', '>', 8)], 
    [('LETTERS', '>', 6)],
    [('NUMBERS', '>', 2), ('SPECIALS', '>', 2)],
    [('LEN', '>', 8), ('LETTERS', '>', 6), ('NUMBERS', '>', 2), ('SPECIALS', '>', 2)]] 
    
    invalid_req = [[('NUMBERS', '>', 8)],
    [('SPECIALS', '>', 6)],
    [('LEN', '>', 2), ('SPECIALS', '<', 2)],
    [('LEN', '<', 8), ('LETTERS', '>', 6), ('NUMBERS', '>', 2), ('SPECIALS', '>', 2)]]    
    
    count_test = 0;
    passed_test = 0;
    
    #Valid Password Tests  
    for each_req in valid_req:
        test = password_validation(password,each_req)
        count_test += 1
        if test:
            passed_test += 1
        
    #Invalid Password Tests
    for each_req in invalid_req:
        test = password_validation(password,each_req)
        count_test += 1
        if not test:
            passed_test += 1    
    
    
    #Tests for different passwords based on a specific req 
    
    #password must have at least 8 characters containing at least 4 letters, 2 numbers and 2 specials
    req = [('LEN', '>', 7), ('LETTERS', '>', 3), ('NUMBERS', '>', 1), ('SPECIALS', '>', 1)]        
    valid_passwords = ["Bruna29/01@", "@Bruna29*", "BruR29**"]
    invalid_passwords = ["Bruna29/01", "@Bru29*", "*Bruna1*"]
    
    #Valid Password Tests
    for each_pass in valid_passwords:
        test = password_validation(each_pass,req)
        count_test += 1
        if test:
            passed_test += 1

    #Invalid Password Tests
    for each_pass in invalid_passwords:
        test = password_validation(each_pass,req)
        count_test += 1
        if not test:
            passed_test += 1        
  
    print("Of", count_test,"tests,", passed_test, "tests passed")

#Testing a specific password defined at the beggining of code       
print(password_validation(password,req))

#Running defined tests
test_password_validation()
