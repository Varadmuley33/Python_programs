#input row : 5 col : 4 

'''
      * * * * 
      * * * * 
      * * * * 
      * * * * 

'''

def Display(iRow , iCol):
    
    
    for i in range (1,iRow+1,1):
        print("$\t"*iCol )
      
def main ():
    
    print("Enter number of rows  :")
    iValue1 = int(input())
    
    print("Enter number of columns :")
    iValue2 = int(input())
    
    Display(iValue1,iValue2)
    
   
 
    
if __name__ == "__main__":
    main()
    
    
    
    
