
class Node:
    """ A Node of an ItalianQueue. 
        Holds both data and group provided by the user. 
    """
    
    def __init__(self, initdata, initgroup):
        self._data = initdata
        self._group = initgroup
        self._next = None

    def get_data(self):
        return self._data

    def get_group(self):
        return self._group
    
    def get_next(self):
        return self._next

    def set_data(self,newdata):
        self._data = newdata

    def set_next(self,newnext):
        self._next = newnext

class ItalianQueue:
    """ An Italian circular queue, v1.  
    
        - Implemented as a LinkedList
        - Worst case enqueue is O(n)
        - has extra methods, for accessing groups and tail:
            - top_group()
            - tail()
            - tail_group()
                        
        Each element is assigned a group; during enqueing, queue is scanned from head to tail
        to find if there is another element with a matching group. 
            - If there is, element to be enqueued is inserted after the last element in the same group sequence
            - otherwise the element is inserted at the end of the queue
    """
    
    def __init__(self):
        """ Initializes the queue. Note there is no capacity as parameter
                
            - Complexity: O(1)
        """
                    
        self._head = None
        self._tail = None
        self._size = 0
       
    def to_python(self):
        """ Returns this ItalianQueue as a regular Python list, in the form [(v1,g1), (v2,g2), ...]. 
            
            This method is very handy for testing.
            
            WARNING: use it ONLY for testing!
        """
        python_list = []
        current = self._head        
        
        while (current != None):
            python_list.append((current.get_data(), current.get_group()))
            current = current.get_next()                       
        return python_list        
        
    def __str__(self):
        """ For potentially complex data structures like this one, having a __str__ method is essential to 
            quickly inspect the data by printing it. 
        """
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str((current.get_data(), current.get_group())))            
            current = current.get_next()            
        
        return "ItalianQueue: " + ",".join(strings)
    
    
    
    def size(self):
        """ Return the size of the queue.
        
            - Complexity: O(1)
        """
        return self._size
    
    def is_empty(self):
        """ Return True if the queue is empty, False otherwise.
        
            - Complexity: O(1)
        """
        return self._head == None

    
    def top(self):
        """ Return the element at the head of the queue, without removing it. 
        
            - If the queue is empty, raises LookupError.            
            - Complexity: O(1)
        """
        if self._head != None:
            return self._head.get_data()
        else:
            raise LookupError("Queue is empty !")    
    
    def top_group(self):
        """ Return the group of the element at the head of the queue, without removing it. 
        
            - If the queue is empty, raises LookupError.
            - Complexity: O(1)
        """
        if self._head != None:
            return self._head.get_group()
        else:
            raise LookupError("Queue is empty !")    

    def tail(self):
        """ Return the element at the tail of the queue (without removing it). 
        
            - If the queue is empty, raises LookupError.            
            - Complexity: O(1)
        """
        if self._tail != None:
            return self._tail.get_data()
        else:
            raise LookupError("Queue is empty !")    
    
    def tail_group(self):
        """ Return the group of the element at the tail of the queue (without removing it). 
        
            - If the queue is empty, raises LookupError.
            - Complexity: O(1)
        """
        if self._tail != None:
            return self._tail.get_group()
        else:
            raise LookupError("Queue is empty !")    
            
                        
    def enqueue(self, v, g):
        """ Enqueues provided element v having group g, with the following criteria:
        
            Queue is scanned from head to find if there is another element with a matching group:
                - if there is, v is inserted after the last element in the same group sequence
                - otherwise v is inserted at the end of the queue

            - Complexity: O(n)
        """
        
        new_node = Node(v,g)
        self._size += 1        
        
        if self._head == None:     # empty queue
            self._head = new_node
            self._tail = new_node
        else:                      # non-empty queue
            current = self._head
            prev = self._head                
            found_group = False
            
            while current != None:            
                if found_group:                                    
                    if current.get_group() != g: # time to insert                      
                        new_node.set_next(current)                    
                        prev.set_next(new_node)                         
                        return
                else: # didn't previously find group                                        
                    if current.get_group() == g:
                        found_group = True

                prev = current
                current = current.get_next()
            
            # if it already found group end, it means it already returned
            self._tail.set_next(new_node)
            self._tail = new_node

    
    def dequeue(self):
        """ Removes head element and returns it.
            
            - If the queue is empty, raises a LookupError.
            - Complexity: O(1)
        """
        
        if self._head != None:
            self._size -= 1
            ret = self._head.get_data()
            self._head = self._head.get_next()
            if self._head == None:
                self._tail = None
            return ret
        else:
            raise LookupError("Queue is empty !")                    
    