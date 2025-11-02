

def calculate(num1,operator,num2):

    if operator== 'add':

                 return num1+num2
    

    elif operator== 'subtract':
                  
                  return num1-num2
    

    elif operator== 'multiply':
            
                  return num1* num2
    

    elif operator== 'divide':
            
                  if num2 ==0:
                          
                          return 'Error: Cannot divide by zero'
                  

                          
                  else:
                          return num1/num2
                  

result =calculate(8,'add', 5)
print(f'the result is{result}')

result =calculate(8 , 'subtract',5)
print (f'the result is {result}')

result =calculate(8,'multiply', 5)
print (f'the result is {result}')

result =calculate (8,'divide',5)
print (f'the result is {result}')

