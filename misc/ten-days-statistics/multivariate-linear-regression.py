from sklearn import linear_model
import os

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fm = input().split()

    f = int(fm[0])
    m = int(fm[1])
    x = []
    y = []
    for i  in range(m):
        f_i = list(map(float, input().rstrip().split()))
        x.append(f_i[:-1])
        y.append(f_i[-1])

    outputs = input().split()
    outputs = int(outputs[0])
    features = []
    for i in range(outputs):
        features.append(list(map(float, input().rstrip().split())))
 
    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    a = lm.intercept_
    b = lm.coef_

    for feat in features:
        y_pred = a
        for i in range(len(feat)):
            y_pred += b[i]*feat[i]
        fptr.write('{0:.2f}\n'.format(y_pred))

    fptr.close()