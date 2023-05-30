def solution(numbers):
    num_lst = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for index, i in enumerate(num_lst):
        numbers = numbers.replace(i, str(index))
    return int(numbers)