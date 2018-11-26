def most_frequent(seq):
    seq_list = list(seq)
    frequency_dict = {}
    for x in seq_list:
        if x in frequency_dict: frequency_dict[x] += 1
        else: frequency_dict[x] = 1
    max_value = max(sorted(frequency_dict.values()))
    most_freqList = [x for x in frequency_dict
                     if frequency_dict[x] == max_value]
    return most_freqList, max_value, frequency_dict

if __name__ == '__main__':
    c = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4,4,4,5,5,5,5]
    f = most_frequent(c)
    print(f)
    print(f[2])




        
    
    
        
        
        
        
    

