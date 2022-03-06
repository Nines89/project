from sklearn import linear_model
from pandas import read_csv


if __name__ == "__main__":
        col = read_csv('dataNN.csv')
        X = col.drop(columns=['y', 'x1'])
        y = col['y']
        print(X)
        modello = linear_model.LinearRegression()
        modello.fit(X.values, y.values)

        print(modello.predict([[1000], [21]]))
