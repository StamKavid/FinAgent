import numpy as np
import pandas as pd
from arch import arch_model
from sklearn.metrics import mean_absolute_error, mean_squared_error

class GARCHModel:
    def __init__(self, data, exog_data=None, train_size=0.8):
        self.data = data
        self.exog_data = exog_data
        self.train_size = int(len(data) * train_size)
        self.train = data[:self.train_size]
        self.test = data[self.train_size:]
        self.exog_train = exog_data[:self.train_size] if exog_data is not None else None
        self.exog_test = exog_data[self.train_size:] if exog_data is not None else None

    def fit(self):
        self.model = arch_model(self.train, vol='Garch', p=1, q=1, x=self.exog_train)
        self.model_fit = self.model.fit(disp='off')

    def forecast(self):
        self.forecast_result = self.model_fit.forecast(horizon=len(self.test), x=self.exog_test)
        self.predictions = self.forecast_result.mean.values[-1, :]

    def evaluate(self):
        mase = self.calculate_mase(self.test.values, self.predictions, self.train.values)
        mape = self.calculate_mape(self.test.values, self.predictions)
        rmse = np.sqrt(mean_squared_error(self.test.values, self.predictions))
        mae = mean_absolute_error(self.test.values, self.predictions)
        return {"MASE": mase, "MAPE": mape, "RMSE": rmse, "MAE": mae}

    @staticmethod
    def calculate_mase(y_true, y_pred, y_train):
        naive_forecast = np.roll(y_train, shift=1)[1:]
        mae_naive = np.mean(np.abs(y_train[1:] - naive_forecast))
        return mean_absolute_error(y_true, y_pred) / mae_naive

    @staticmethod
    def calculate_mape(y_true, y_pred):
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100