from flask import Flask, render_template, redirect
import pandas as pd
import numpy as np

app = Flask(__name__)

# Sample portfolio weights (static data for now)
portfolio_weights = pd.Series({
    'AAPL': 0.214572,
    'GOOGL': 0.088560,
    'MSFT': 0.143033,
    'TSLA': 0.553836
})

# Convert the portfolio_weights (Series) into a DataFrame and transpose it
portfolio_weights_df = portfolio_weights.to_frame().T  # Convert to DataFrame and transpose

# Future stock prices for the next 10 days (mock data, this should be replaced with actual predictions)
future_stock_prices = pd.DataFrame({
    'AAPL': np.random.rand(10) * 150,  # Random stock prices for demo
    'GOOGL': np.random.rand(10) * 2000,
    'MSFT': np.random.rand(10) * 300,
    'TSLA': np.random.rand(10) * 600,
}, index=pd.date_range(start='2024-11-13', periods=10, freq='B'))

# Future portfolio returns for the next 10 days (mock data, should be replaced with actual model)
future_portfolio_returns = pd.DataFrame({
    'Portfolio': np.random.rand(10) * 0.05  # Random portfolio returns for demo
}, index=pd.date_range(start='2024-11-13', periods=10, freq='B'))

# Route to display portfolio weights, stock prices, and portfolio returns
@app.route('/')
def index():
    return render_template('index.html', 
                           portfolio_weights=portfolio_weights_df.to_html(),
                           future_stock_prices=future_stock_prices.to_html(),
                           future_portfolio_returns=future_portfolio_returns.to_html())

# Route for predicting future stock prices and portfolio returns
@app.route('/predict')
def predict():
    global future_stock_prices, future_portfolio_returns

    # Simulating the prediction of future stock prices (random values)
    future_stock_prices = pd.DataFrame({
        'AAPL': np.random.rand(10) * 150,
        'GOOGL': np.random.rand(10) * 2000,
        'MSFT': np.random.rand(10) * 300,
        'TSLA': np.random.rand(10) * 600,
    }, index=pd.date_range(start='2024-11-13', periods=10, freq='B'))

    # Simulating the prediction of future portfolio returns (random values)
    future_portfolio_returns = pd.DataFrame({
        'Portfolio': np.random.rand(10) * 0.05  # Random returns for demo purposes
    }, index=pd.date_range(start='2024-11-13', periods=10, freq='B'))

    # Redirecting to the home page to display updated predictions
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
