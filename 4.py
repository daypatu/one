
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class LinkedList:  
    def __init__(self):
        self.first = None #first element of linked list
        self.last = None  #last element of linked list
        self.length = 0   #length of linked list

    def __str__(self):    #print LinkedList
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x):   #add element to LinkedList
        self.length+=1
        if self.first == None:
            
            self.last = self.first = Node(x, None)
        else:
            
            self.last.next = self.last = Node(x, None)

L = LinkedList()

n = input("input a length of linked list: ")   #creation of Linked List object with length equal to n
for i in range(1, n+1):
    L.add(i)

print L  
count = 0  #counter of operations
if L.length > 2:
    a = b = L.first
    """
 ___     ___     ___            ___     ___     ___
|_1_|-->|_2_|-->|_3_|-->....-->|n-2|-->|n-1|-->|_n_|
  ^                                              ^
  |                                              |
 first                                          last
 a, b
    """
    while b.next.next != None:
        b = b.next
        count +=1
    """
 ___     ___     ___            ___     ___     ___
|_1_|-->|_2_|-->|_3_|-->....-->|n-2|-->|n-1|-->|_n_|
  ^                                      ^       ^
  |                                      |       |
 first                                   b      last
  a
    """
    L.last.next = a.next
    a = a.next
    """
           ______________________________________                                       
          |                                      |
 ___     _V_     ___            ___     ___     _|_    
|_1_|-->|_2_|-->|_3_|-->....-->|n-2|-->|n-1|-->|_n_| 
  ^       ^                              ^       ^
  |       |                              |       |
 first    a                              b      last
    """
    L.first.next = L.last
    """
   ___________________________________________________
  |        ______________________________________     |                                  
  |       |                                      |    |
 _|_     _V_     ___            ___     ___     _|_   | 
|_1_|   |_2_|-->|_3_|-->....-->|n-2|-->|n-1|-->|_n_|<-
  ^       ^                              ^       ^
  |       |                              |       |
 first    a                              b      last
    """
    L.last = b
    L.last.next = None
    """
  ___________________________________________________
  |        ______________________________________     |                                  
  |       |                                      |    |
 _|_     _V_     ___            ___     ___     _|_   | 
|_1_|   |_2_|-->|_3_|-->....-->|n-2|-->|n-1|   |_n_|<-
  ^       ^                              ^       
  |       |                              |       
 first    a                             b,last 
    """
    
    while (a.next != b) and (a!= b):
        b = a
        """
       ___     ___     ___            _____     ___     _____
...-->|_i_|-->|i+1|-->|i+2|-->....-->|n-i-1|-->|n-i|-->|n-i+1|
        ^                                                 ^
        |                                                 |
       a, b                                              last
        """
        while b.next.next != None:
            b = b.next
            count += 1
        """
       ___     ___     ___            _____     ___     _____
...-->|_i_|-->|i+1|-->|i+2|-->....-->|n-i-1|-->|n-i|-->|n-i+1|
        ^                                        ^        ^
        |                                        |        |
        a                                        b      last
        """
        L.last.next = a.next
        """
                 _________________________________________
                |                                         |
       ___     _v_     ___            _____     ___     __|__
...-->|_i_|-->|i+1|-->|i+2|-->....-->|n-i-1|-->|n-i|-->|n-i+1|
        ^                                        ^        ^
        |                                        |        |
        a                                        b      last
        """
        a.next = L.last
        """
         _________________________________________________________
        |        _________________________________________        |
        |       |                                         |       |
       _|_     _v_     ___            _____     ___     __|__     |
...-->|_i_|   |i+1|-->|i+2|-->....-->|n-i-1|-->|n-i|-->|n-i+1|<---
        ^                                        ^        ^
        |                                        |        |
        a                                        b      last
        """
        a = L.last.next
        """
         _________________________________________________________
        |        _________________________________________        |
        |       |                                         |       |
       _|_     _v_     ___            _____     ___     __|__     |
...-->|_i_|   |i+1|-->|i+2|-->....-->|n-i-1|-->|n-i|-->|n-i+1|<---
                ^                                ^        ^
                |                                |        |
                a                                b      last
        """
        L.last = b
        L.last.next = None
        """
         _________________________________________________________
        |        _________________________________________        |
        |       |                                         |       |
       _|_     _v_     ___            _____     ___     __|__     |
...-->|_i_|   |i+1|-->|i+2|-->....-->|n-i-1|-->|n-i|   |n-i+1|<---
                ^                                ^        
                |                                |        
                a                               b,last 
        """
        
    
print L
print count
