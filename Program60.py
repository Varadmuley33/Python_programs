def CountVowels(Data):
    iCount = 0 
   
    
    pattern = "aeiouAEIOU"
    for ch in Data:
        if(ch in pattern):
            iCount += 1
            
            
    return len(Data) - iCount
    


def main ():
    
    print("Enter string:")
    str = input()
    
    iRet = CountVowels(str)
    
    print(f"Frequency of vowels in {str} is {iRet}")
 
    
if __name__ == "__main__":
    main()
    
    
    
    