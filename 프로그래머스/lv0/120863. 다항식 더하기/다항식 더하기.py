def solution(polynomial):
    poly = polynomial.split(' + ')
    poly_x = [i.replace('x','') for i in poly if'x'in i]
    poly_x = str(sum([int(i) if i!=''else 1 for i in poly_x]))+'x'
    if poly_x == '1x':
        poly_x = poly_x.replace('1x','x')

    poly_num = str(sum([int(i) for i in poly if'x'not in i]))
    if poly_num == '0':
        return poly_x
    elif poly_x == '0x':
        return poly_num
    else:
        return poly_x+' + '+poly_num