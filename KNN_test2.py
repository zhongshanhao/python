import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from sklearn import datasets

def dist_sort(x):
    return x[0]

def train(X,y,T,k):
    res = []
    for a in T[:,...]:
        B = a - X
        Z = B[...,0]**2 + B[...,1]**2
        C = np.vstack((Z,y))
        C = sorted(C.T,key=dist_sort)
        predict = 0
        count = []
        for i in range(k):
            count.append(0)
        for i in range(k):
            count[int(C[i][1])] += 1
        max = 0
        for j in range(k):
            if max < count[j]:
                max = count[j]
                predict = j
        res.append(predict)
    return res

def main(k):
    test_flag = 0   #0表示选择花萼的长度和宽度作测试 2选择花瓣
    iris = datasets.load_iris()
    if test_flag == 0:
        X = iris.data[:,:2]
    else:
        X = iris.data[:,2:]
    y = iris.target
    features = iris.feature_names
    h = .02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h)) #生成网格型二维数据对
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])  #给不同区域赋以颜色
    cmap_bold = ListedColormap(['#FF0000', '#003300', '#0000FF'])   #给不同属性的点赋以颜色
    z = train(X,y,np.c_[xx.ravel(), yy.ravel()],k)
    C = np.array(z).reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, C, cmap=cmap_light)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xlabel(features[test_flag])
    plt.ylabel(features[test_flag+1])
    plt.title('KNN(k=' + str(k) + ',feature=' + features[test_flag][:5] + ')')
    plt.savefig('KNN(k=' + str(k) + ',feature=' + features[test_flag][:5] + ').png', dpi=200)
    plt.show()

if __name__=='__main__':
    for k in range(3,10,2):
        main(k)


