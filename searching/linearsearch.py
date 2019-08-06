
"""
Linear search is an intuitive search algorithm which searches the given element 
in a list, sequentially, O(n) time complexity, the algorithm has.
"""

def search(element, elements):
    for index in range(len(elements)):
        if elements[index] == element:
            return "{0} is found in index {1}.".format(element, index)
    return "{0} is not an element of the given list.".format(element)



if __name__ == "__main__":
    """
    Little test for our search method above :-)
    """
    print(search(5, [1,2,3,4,5]))
    print(search(6, [1,2,3,4,5]))    