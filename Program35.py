def CheckPrefect(iNo):
    iSum = 0 
    
   
    for i in range (1,(iNo//2) + 1 ):
        if(iNo % i == 0 ):
            iSum += i 
            
    return (iSum == iNo)
        
    
    
def main ():
    print("Enter number :")
    iValue = int(input())
    
    bRet = 0 
    bRet = CheckPrefect(iValue)
    
    if(bRet):
        print(f"{iValue } is prefect number " )
    else:
        print(f"{iValue} is not a prefect number ")
    
    
    
if __name__ == "__main__":
    main()