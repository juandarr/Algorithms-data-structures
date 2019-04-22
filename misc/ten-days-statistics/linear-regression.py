def linear_regression(x,y):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    for i,j in zip(x,y):
        sum_xy += i*j
        sum_x += i
        sum_y += j
        sum_x2 += i*i
    n = len(x)
    slope = (n*sum_xy - sum_x*sum_y)/(n*sum_x2-(sum_x**2))
    intercept = sum_y/n - slope *(sum_x/n)
    return (slope, intercept)

if __name__=='__main__':
    xl = [95, 85, 80, 70, 60]
    y = [85, 95, 70, 65, 70]
    slope,intercept = linear_regression(xl,y)
    print(slope*80+intercept)