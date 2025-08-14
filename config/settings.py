"""
Configuration settings for the AI Sales Forecaster application.
"""

# Server configuration
HOST = "127.0.0.1"
PORT = 8000
DEBUG = True

# Application settings
APP_NAME = "AI Sales Forecaster"
APP_VERSION = "1.1"
APP_DESCRIPTION = "An API to upload sales data and get AI-powered forecasts."

# Model parameters
DEFAULT_PROPHET_PARAMS = {
    "yearly_seasonality": True,
    "weekly_seasonality": True,
    "daily_seasonality": False
}

DEFAULT_SARIMAX_ORDER = (1, 1, 1)
DEFAULT_SARIMAX_SEASONAL_ORDER = (1, 0, 1, 12)  # The last value gets replaced based on frequency

DEFAULT_RF_PARAMS = {
    "n_estimators": 100,
    "random_state": 42,
    "n_jobs": -1
}

# Data processing
DEFAULT_LAG_FEATURES = 7
EXOGENOUS_FEATURES = ['month', 'day_of_week', 'day_of_year']
