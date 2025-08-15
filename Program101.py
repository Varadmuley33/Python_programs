class Node:
    def __init__(self,No):
        self.Data = No
        self.Next = None
        
class SinglyLL:
    def __init__(self):
        self.First = None
        self.iCount = 0
        
        
###################################################################################

       
    def InsertFirst(self,No):
        newn = Node(No)
        
        if(self.First == None): #LL is empty
            self.First = newn

        else:                    # LL contains atleast 1 node
            newn.Next = self.First
            self.First = newn
            
        self.iCount = self.iCount + 1 
        
###################################################################################
        
    def InsertLast(self,No):
        newn = Node(No)
        
        if(self.First == None): #LL is empty
            self.First = newn

        else:
            temp = self.First
            
            while(temp.Next != None):
                temp = temp.Next 
                
            temp.Next = newn                  
            
            
        self.iCount = self.iCount + 1 
            
            
###################################################################################
    
    def Display(self):
        temp = self.First
        while (temp != None):
            
            print(f" | {temp.Data} | -> ", end=" ")
            temp = temp.Next
            
        print()
            
    
    
###################################################################################

    def Count(self):
        return self.iCount
    
    
###################################################################################
        
        
    def DeleteFirst(self):
         
        
        if(self.First == None):
            return
        else:
            temp = self.First
            self.First = self.First.Next
            del temp
            
            
        self.iCount = self.iCount - 1
            
    def DeleteLast(self):
        
        if(self.First == None):
            return
        elif(self.First.Next == None):
            del self.First
            self.First = None
            
        else:
            temp = self.First
            
            while(temp.Next.Next != None):
                temp = temp.Next
                
            del temp.Next
            
            temp.Next = None
  
        self.iCount = self.iCount - 1
        
        
    


def main ():
    print("Demonstration of singly linear link List")
    
    sobj = SinglyLL()
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    
    
    sobj.Display()
    iRet = sobj.Count()
    print(f"Number in linked list are : {iRet}")
    
    sobj.InsertLast(101)
    sobj.InsertLast(111)
    sobj.InsertLast(121)
    
     
    sobj.Display()
    iRet = sobj.Count()
    print(f"Number in linked list are : {iRet}")
    
    sobj.DeleteFirst()
    sobj.Display()
    iRet = sobj.Count()
    print(f"Number in linked list are : {iRet}")
    
    
    sobj.DeleteLast()
    sobj.Display()
    iRet = sobj.Count()
    print(f"Number in linked list are : {iRet}")
    
    
    
    
    
   
   
if __name__ == "__main__":
    main()
    
    
    
    