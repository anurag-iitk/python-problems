# Return a new set of identical items from two sets

def check_element(set1,set2):
    newSet = set1.intersection(set2)
    return newSet
    

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = check_element(set1,set2)
print(result)