'''Problem: Sort a list of people's ages. Works for an list of numbers with a known finite boundary.'''

def sort(age_list):
    sorted_list = [0] * 130
    final_list = []

    for i in range(len(age_list)):       # in this step the element at the index of sorted_list that corresponds to the age of a person in the age_list is incremented for every person with the same age.
        sorted_list[age_list[i]] += 1
    for i in range(len(sorted_list)):    # the final sorted list is being constructed. 
        for j in range(sorted_list[i]):
            final_list.append(i)
    return final_list

#Testing the function
print(sort([12,44,2,9,7,0,6,1,4,8,77,100,55]))
    
