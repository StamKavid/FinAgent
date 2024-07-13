# Import the model we are using
from prophet import Prophet
import numpy as np

import pandas as pd
import os
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import joblib
import warnings

warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)

class CryptoData(BaseModel):
    date: str
    features: Dict[str, float]

class PredictionResponse(BaseModel):
    date: str
    prediction: float

def load_data(df):
    X = df.drop(df.iloc[:, :6].columns.tolist() + [col for col in df.columns if 'OTHERS' in col], axis=1)
    y = df['ADJ_CLOSE']
    return y, X

def prepare_data(y: pd.Series, X: pd.DataFrame):
    
    # Create a new DataFrame with all columns at once
    df = pd.concat([
        pd.DataFrame({'ds': y.index, 'y': y.values}),
        X
    ], axis=1)
    
    # Add day of week and is_weekend features
    df['DAY_OF_WEEK'] = df['ds'].dt.dayofweek
    df['IS_WEEKEND'] = df['DAY_OF_WEEK'].isin([5, 6]).astype(int)
    
    return df

def train_prophet_model(df: pd.DataFrame, external_regressors: List[str]):
    model = Prophet(
        daily_seasonality=True,
        weekly_seasonality=True,
        yearly_seasonality=True,
        changepoint_prior_scale=0.05,
        seasonality_prior_scale=10
    )
    for regressor in external_regressors:
        model.add_regressor(regressor)
    
    model.fit(df)
    return model

def evaluate_model(model: Prophet, df: pd.DataFrame, period: str = '30 days'):
    cv_results = cross_validation(model, initial='730 days', period=period, horizon='1 days')
    performance = performance_metrics(cv_results)
    return cv_results, performance

def plot_results(model: Prophet, df: pd.DataFrame, cv_results: pd.DataFrame):
    # Plot forecast
    future = model.make_future_dataframe(periods=30)
    for col in df.columns:
        if col not in ['ds', 'y']:
            future[col] = df[col].iloc[-1]  # Use last known value for external regressors
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        forecast = model.predict(future)
    
    fig1 = model.plot(forecast)
    plt.title('Prophet Forecast')
    plt.savefig('forecast.png')
    plt.close()

    # Plot components
    fig2 = model.plot_components(forecast)
    plt.savefig('components.png')
    plt.close()

    # Plot cross-validation results
    fig3, ax = plt.subplots()
    ax.plot(cv_results['ds'], cv_results['y'], 'k.', alpha=0.5, label='Actual')
    ax.plot(cv_results['ds'], cv_results['yhat'], 'b-', label='Predicted')
    ax.fill_between(cv_results['ds'], cv_results['yhat_lower'], cv_results['yhat_upper'], color='b', alpha=0.3)
    ax.legend()
    plt.title('Cross-validation Results')
    plt.savefig('cv_results.png')
    plt.close()

    # Plot train/validation loss
    fig4, ax = plt.subplots()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        train_pred = model.predict(df[['ds'] + [col for col in df.columns if col not in ['y']]])
    train_loss = np.abs(df['y'] - train_pred['yhat'])
    val_loss = np.abs(cv_results['y'] - cv_results['yhat'])
    ax.plot(df['ds'], train_loss, label='Train Loss')
    ax.plot(cv_results['ds'], val_loss, label='Validation Loss')
    ax.legend()
    plt.title('Train/Validation Loss')
    plt.savefig('train_val_loss.png')
    plt.close()

def main():
    model_path = 'prophet_model.joblib'
    
    # Check if the model already exists
    if os.path.exists(model_path):
        print("Loading existing model...")
        model = joblib.load(model_path)
    else:
        print("Training new model...")
        # Load and prepare data
        y, X = load_data('y_data.csv', 'x_data.csv')
        df = prepare_data(y, X)

        # Split data into train and test sets
        train_df, test_df = train_test_split(df, test_size=0.2, shuffle=False)

        # Train model
        external_regressors = [col for col in df.columns if col not in ['ds', 'y', 'day_of_week', 'is_weekend']]
        model = train_prophet_model(train_df, external_regressors)

        # Save model
        joblib.dump(model, model_path)

    # Evaluate model
    _, X = load_data('y_data.csv', 'x_data.csv')
    df = prepare_data(_, X)
    cv_results, performance = evaluate_model(model, df)
    print("Model Performance:")
    print(performance)

    # Plot results
    plot_results(model, df, cv_results)

    return model

# FastAPI app
app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
async def predict(data: CryptoData):
    try:
        model = joblib.load('prophet_model.joblib')
        future = pd.DataFrame({
            'ds': [pd.to_datetime(data.date)],
            **data.features
        })
        
        # Add day of week and is_weekend features
        future['day_of_week'] = future['ds'].dt.dayofweek
        future['is_weekend'] = future['day_of_week'].isin([5, 6]).astype(int)
        
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            forecast = model.predict(future)
        
        return PredictionResponse(
            date=data.date,
            prediction=forecast['yhat'].iloc[0],
            confidence_interval={
                'lower': forecast['yhat_lower'].iloc[0],
                'upper': forecast['yhat_upper'].iloc[0]
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    main()

