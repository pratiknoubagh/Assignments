# l1 = ("Pratik", "Mohan", "Sohan", "Arpit")
# l2 = ("Mohan", "Lalit", "Pratik", "Satyam", "Bob")
def find_common_elements(l1, l2):
    common_elements = []
    for element1 in l1:
        for element2 in l2:
            if element1 == element2:
                common_elements.append(element2)
                break
    return common_elements


l1 = ("Pratik", "Mohan", "Sohan", "Arpit")
l2 = ("Mohan", "Lalit", "Pratik", "Satyam", "Bob")
common_elements = find_common_elements(l1, l2)
print("Common elements:", common_elements)
