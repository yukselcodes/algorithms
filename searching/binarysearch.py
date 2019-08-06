
"""
Binary search is another algorithm which finds a given element out of a list,
this method follows divide & conquer strategy,
O(logn) time complexity for this algorithm,
works on a SORTED list
"""

def search(elements, left, right, element):
    
    if right >= left:
        
        middle = left + (right - left) / 2

        if elements[middle] == element:
            return "{0} is found in index {1}".format(element, middle)
        elif elements[middle] >= element:
            return search(elements, left, middle-1, element)
        else:
            return search(elements, middle+1, right, element)
    else:
        return "{0} is not an element of the given list.".format(element)


if __name__ == "__main__":
    """
    Little test for our search method above :-)
    """
    print(search([1,2,3,4,5], 0, len([1,2,3,4,5])-1, 4))
    print(search([1,2,3,4,5], 0, len([1,2,3,4,5])-1, 6))