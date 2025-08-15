# Input : 721
# 7    2    1 
def SumDigits(No):
    iDigit = 0
    iSum = 0
    
    while(No != 0 ):
        iDigit = No % 10
        iSum = iSum + iDigit 
        No = No // 10
    
    return iSum
            
def main():
    
    print("Enter  number : ")
    Value = int(input())
    iRet = 0
    
    iRet = SumDigits(Value)
    
    print(f"Summation of digitis = {iRet}")
    
    
if __name__ == "__main__":
    main()