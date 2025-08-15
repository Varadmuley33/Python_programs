#input HELLO

# output H E L L O 



def Display(Data):
    
    for ch in (Data):
        print(ch ,end="\t")
    
        
def main ():
    
    print("Enter the value :")
    iValue = int(input())
    
    Display(iValue)
    
   
 
    
if __name__ == "__main__":
    main()
    
    
    
    