from time import time

import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class NeuralNetwork:
    def __init__(self, input=[], output=[]):
        self.input = input
        data_0 = []
        for el in output:
            for num, element in enumerate(el):
                if num == 0:
                    data_0.append(str(element))
        self.output_goalpt = data_0
        data_1 = []
        for el in output:
            for num, element in enumerate(el):
                if num == 1:
                    data_1.append(str(element))
        self.output_goaltot = data_1
        data_2 = []
        for el in output:
            for num, element in enumerate(el):
                if num == 2:
                    data_2.append(str(element))
        self.output_esito = data_2
        self.X_train = None
        self.X_test = None
        self.y_train_goalpt = None
        self.y_test_goalpt = None
        self.y_train_goaltot = None
        self.y_test_goaltot = None
        self.y_train_esito = None
        self.y_test_esito = None

    def conformData(self):
        '''
        La funzione trasforma i database in numerici
        :param dataset:  Il database estratto dal file csv
        :return: riempie gli elementi della classe
        '''

        # iloc permette di lavorare sulla tabella il primo : per le righe, il secondo per le colonne

        try:
            # conversion data
            Le = LabelEncoder()
            for i in range(len(self.input[0])):
                self.input[:, i] = Le.fit_transform(self.input[:, i])

            for i in range(len(self.output_goalpt[0])):
                self.output_goalpt[:, i] = Le.fit_transform(self.output_goalpt[:, i])

            for i in range(len(self.output_goaltot[0])):
                self.output_goaltot[:, i] = Le.fit_transform(self.output_goaltot[:, i])

            output_mapping = {
                '1': 1,
                '2': 2,
                'X': 3
            }

            self.output_esito = [*map(output_mapping.get, self.output_esito)]

            self.train_test_split_generation(0.2)


        except ValueError:
            print("dataset empty")

    def regression_metrics(self, pred):
        '''
        MSE = mean square error
        RMSE = root mean square error
        MAE = Mean absolute error
        MAPE = Mean absolute percentage error
        R2 = quare r (meglio che sia 1)
        MPD = devianza di poisson
        MGD = devianza di gamma
        :param pred:
        :return:
        '''
        acc = {}
        acc["MSE"] = metrics.mean_squared_error(self.y_test, pred)
        acc["RMSE"] = metrics.mean_squared_error(self.y_test, pred, squared=False)
        acc["MAE"] = metrics.mean_absolute_error(self.y_test, pred)
        acc["MAPE"] = metrics.mean_absolute_percentage_error(self.y_test, pred)
        acc["R2"] = metrics.r2_score(self.y_test, pred)
        acc["MPD"] = metrics.mean_poisson_deviance(self.y_test, pred)
        acc["MGD"] = metrics.mean_gamma_deviance(self.y_test, pred)
        return acc

    def train_test_split_generation(self, test_size):
        self.X_train, self.X_test, self.y_train_esito, self.y_test_esito = train_test_split(self.input,
                                                                                            self.output_esito,
                                                                                            test_size=test_size)
        self.X_train, self.X_test, self.y_train_goalpt, self.y_test_goalpt = train_test_split(self.input,
                                                                                              self.output_goalpt,
                                                                                              test_size=test_size)
        self.X_train, self.X_test, self.y_train_goaltot, self.y_test_goaltot = train_test_split(self.input,
                                                                                                self.output_goaltot,
                                                                                                test_size=test_size)

    def knn(self):
        '''
        Se prima andava tutto bene adesso performiamo una knn
        :return: modello, accuratezza del modello
        '''
        knn = neighbors.KNeighborsClassifier(n_neighbors=20, weights='uniform')

        # self.y_train = self.y_train.astype('int')

        knn.fit(self.X_train, self.y_train_goalpt)
        knn.fit(self.X_train, self.y_train_goaltot)
        knn.fit(self.X_train, self.y_train_esito)

        prediction = knn.predict(self.X_test)

        # acc = self.regression_metrics(prediction)

        acc = metrics.accuracy_score(self.y_test_esito, prediction)

        print("original: ", self.y_test_esito)
        print("predict: ", prediction)
        return knn, acc


if __name__ == "__main__":
    tipo = set()

    start = time()

    csv_base = "./src/db/csv/"
    import_path = csv_base + 'prova1_2022-04-14.cvs'
    dataset = pd.read_csv(import_path, header=None, delimiter=',')

    nn = NeuralNetwork(input=dataset.iloc[:, :-3].values, output=dataset.iloc[:, -3:].values)

    nn.conformData()

    model, accuracy = nn.knn()

    print("acc: ", accuracy)

    '''print("accuracy: ", accuracy["MSE"])
    print("accuracy: ", accuracy["RMSE"])
    print("accuracy: ", accuracy["MAE"])
    print("accuracy: ", accuracy["MAPE"])
    print("accuracy: ", accuracy["R2"])'''

    print("total time = ", time() - start)

    # create model

    # saving model

    # open existing model

    '''
    col = read_csv('dataNN.csv')
    X = col.drop(columns=['y', 'x1'])
    y = col['y']
    print(X)
    modello = linear_model.LinearRegression()
    modello.fit(X.values, y.values)
    print(modello.predict([[1000], [21]]))
    '''
