from art import logo
print(logo)
#calculator functions
# add


def add(n1, n2):
  return n1 + n2
#substraction

def substract(n1, n2):
  return n1 - n2  

 #multiply 
def multiply(n1, n2):
  return n1 * n2
#division
def divide(n1, n2):
  return n1 / n2

operations = { "+" : add, 
              "-" : substract,
              "*" : multiply, 
              "/" : divide,
}
def calculator():
  n1 = float(input("what's the first number?: "))
  
  
  for symbol in operations:
    print(symbol)
  
  
  reapeat = False 
  while not reapeat :
     
     
  
      operation_symbol = input("Pick an operation symbol from the line above: ")
      n3 = float(input("what's the next number?: "))
      
    
      
      answer = operations[operation_symbol](n1, n3)
      print(f"{n1} {operation_symbol} {n3} = {answer}")
  
      continu_cal = input(f"type 'y' to keep calculating with {answer} or type 'n' to start a new calculation ")
      if continu_cal == 'y':
        n1 = answer
  
      else:
        reapeat = True
        calculator()

calculator()