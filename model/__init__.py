from .random_forest import RandomForest
from .sarimax import Sarimax
from .orbit import Orbit
from .LSTM import MyLSTM
from .GRU import MyGRU
from .arima import MyARIMA
from .prophet import train_prophet_model
from .xgboost import MyXGboost
from .neural_prophet import Neural_Prophet
from .garch import GARCHModel


MODELS = {'random_forest': RandomForest,
          'sarimax': Sarimax,
          'orbit': Orbit,
          'lstm': MyLSTM,
          'gru': MyGRU,
          'arima': MyARIMA,
          'prophet': train_prophet_model,
          'xgboost': MyXGboost,
          'neural_prophet': Neural_Prophet,
          'garch': GARCHModel
          }
