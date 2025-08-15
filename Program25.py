# Input : 721
# 7    2    1 
def DisplayDigits(No):
    iDigit = 0
    
    while(No != 0 ):
        iDigit = No % 10
        No = No // 10
        print(iDigit)
            
def main():
    
    print("Enter  number : ")
    Value = int(input())
    
    DisplayDigits(Value)
    
    
if __name__ == "__main__":
    main()