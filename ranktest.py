def count_substring(string, sub_string):
    count=0
    for word in string:
        for word in sub_string:
            count+=1
    

    return count

a=input('enter: ')
print(count_substring(a))