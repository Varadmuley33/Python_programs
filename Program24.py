def Factorial(No):
    ifact = 1
    
    for i in range (1 , No+1):
        ifact = ifact * i
        
    return ifact
    
    
        
         
def main():
    
    print("Enter  number : ")
    Value = int(input())
    
    iRet = Factorial(Value)
    
    print(f"Factorial is  : {iRet}")
   
    
if __name__ == "__main__":
    main()