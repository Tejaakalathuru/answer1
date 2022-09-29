def totalCount(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print ("% d : % d"%(key, value))
 
if __name__ == "__main__":
    my_list =[1,2,3,4,5,6,7,8,9] 
    totalCount(my_list)
