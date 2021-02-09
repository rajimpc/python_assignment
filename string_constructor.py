def sentence_constructor(s,ln,ans,wrd,arr):
    if ln == 0:
        if ans in dictionary:
            x = wrd + " " + ans
            print("("+x.strip()+")",end= "")
            arr.append(1)
    else:
        if ans+s[0] in dictionary:
            sentence_constructor(s[1:],ln-1,'',wrd + " " + ans+s[0],arr)
        sentence_constructor(s[1:],ln-1,ans+s[0],wrd,arr)


if __name__=='__main__':
    print('Input no. of test case')
    no_test_case=int(input())
    print('Input no. of words in dictionary')
    no_words_dict=int(input())
    print('Input words in dictionary')
    dictionary_words=str(input())
    dictionary_words = dictionary_words.split()
    print('Input string')
    input_string = input()
    
    # no of test case to run
    for temp in range(no_test_case):
        dictionary = {}
        for elements in dictionary_words:
            dictionary[elements] = 1
        elements = []
        len_string=len(input_string)
        
        tt(input_string,len_string,'','',elements)
        if len(elements) == 0:
            print("No_match",end=" ")
        #print()
