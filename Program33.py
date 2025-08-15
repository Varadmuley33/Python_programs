def SumFactors(iNo):
    iSum = 0 
    
   
    for i in range (1,(iNo//2) + 1 ):
        if(iNo % i == 0 ):
            iSum += i 
            
    return iNo
    
def main ():
    print("Enter number :")
    iValue = int(input())
    
    iRet = 0 
    iRet = SumFactors(iValue)
    
    print(f"Summation  of Factors of {iValue} is : {iRet}")
    
    
    
if __name__ == "__main__":
    main()