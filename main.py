import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":
    dataset =pd.read_csv('db/felicidad.csv')
    print(dataset.describe())

    X = dataset[['gdp', 'family', 'lifexp', 'freedom', 'corruption', 'generosity', 'dystopia']]
    Y = dataset[['score']]

    print(X.shape)
    print(Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)

    modelLinear = LinearRegression().fit(X_train, Y_train)
    Y_predict_linear = modelLinear.predict(X_test)

    modelLasso = Lasso(alpha=0.02).fit(X_train, Y_train)
    Y_predict_lasso = modelLasso.predict(X_test)

    modelRidge = Ridge(alpha=1).fit(X_train, Y_train)
    Y_predict_ridge = modelRidge.predict(X_test)

    modelEN = ElasticNet(random_state=0).fit(X_train, Y_train)
    Y_predict_elastic = modelEN.predict(X_test)

    linear_loss = mean_squared_error(Y_test, Y_predict_linear)
    print("Linear Loss: ", linear_loss)

    lasso_loss = mean_squared_error(Y_test, Y_predict_lasso)
    print("Lasso Loss: ", lasso_loss)

    ridge_loss = mean_squared_error(Y_test, Y_predict_lasso)
    print("Ridge Loss: ", ridge_loss)

    elastic_loss = mean_squared_error(Y_test, Y_predict_elastic)
    print("ElasticNet Loss: ", elastic_loss)

    print("=" * 32)
    print("- Coef LASSO")
    print(modelLasso.coef_)

    print("- Coef RIDGE")
    print(modelRidge.coef_)