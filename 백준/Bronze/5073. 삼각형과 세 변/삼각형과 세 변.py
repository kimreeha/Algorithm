while True:
    nums = list(map(int, input().split()))
    if nums == [0,0,0]:
        break
    # 삼각형 조건을 만족하지 못하는 경우
    nums.sort()
    if sum(nums[:2]) <= nums[-1]:
        print('Invalid')
    elif len(set(nums)) == 1:
        print('Equilateral')
    elif len(set(nums)) == 2:
        print('Isosceles')
    else:
        print('Scalene')