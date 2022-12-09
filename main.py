import argparse
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main():

    # 加載手寫數字資料集
    digits = datasets.load_digits()

    # 查看前 10 個手寫數字圖像
    for i in range(10):
        print(digits.data[i].reshape(8, 8))
        print("Label:", digits.target[i])

    # 將資料拆分為訓練集和測試集
    X_train, X_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.25, random_state=0
    )

    # 輸出結果
    print(f'start ！')

    # 建立 KNN 模型
    knn = KNeighborsClassifier(n_neighbors=3)

    # 訓練模型
    knn.fit(X_train, y_train)

    # 使用測試集評估模型性能
    accuracy = knn.score(X_test, y_test)
    print("Accuracy: {:.2f}%".format(accuracy * 100))


if __name__ == '__main__':
    main()
