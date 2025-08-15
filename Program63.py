def Replace(data):
    iCount = 0 
   
    
    output = ""
    
    for ch in data:
        if(ch == 'a' ):
            output.append('_')  # error here append dosent work 
        else:
            output.append(ch)
              
              
    return output
    


def main ():
    
    print("Enter string:")
    str = input()
    
    strX = Replace(str)
    
    print(f"Updated string is : {strX}")
 
    
if __name__ == "__main__":
    main()
    
    
    
    