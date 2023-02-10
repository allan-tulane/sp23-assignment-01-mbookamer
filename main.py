"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)
    pass

def longest_run(mylist, key):
    ### TODO
    array = [] #initialize a separate list of consecutive times 'key' appears to return the max
    count = 0 #base value
    for i in range(len(mylist)):
        if key == mylist[i]:
            count +=1
        
        elif (key != mylist[i]) or (i == len(mylist) - 1): #if we reach a new key value OR we are at the end of our list we want to stop
            array.append(count) #want to save the current number of consecutive key values
            count = 0 #no longer consecutive so we go back to 0
            
    return max(array) #we want the longest run of consecutive values so we take the max value
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


