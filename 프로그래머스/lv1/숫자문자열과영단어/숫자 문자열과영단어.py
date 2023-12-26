def solution(s):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    word = ''
    result = []

    for i in s:
        if i.isalpha() == True:
            word += i
            for j in range(len(words)):
                if word == words[j]:
                    word = ''
                    result.append(nums[j])
        else:
            result.append(i)
                
    return int(''.join(result))