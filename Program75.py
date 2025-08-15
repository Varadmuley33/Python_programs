#input HELLO

# output H E L L O 
# H E L L O 
# H E L L O 
# H E L L O 


def Display(Data):
    
    for i in range (len(Data)):

        for ch in (Data):
             print(ch ,end="\t")
        print()
    
        
def main ():
    
    print("Enter the value :")
    str = input 
    
    Display(str)
    
   
 
    
if __name__ == "__main__":
    main()
    
    
    
    