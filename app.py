from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle stock data and visualization
@app.route('/plot', methods=['POST'])
def plot():
    # Get the stock symbol from the form
    stock_symbol = request.form.get('stock_symbol')
    
    if stock_symbol:  # Corrected this line, added closing conditional statement

        # Example: Get stock data (you'll need to replace this with your actual API call)
        # For demonstration, using pandas to generate a simple data frame (this is where you'll get your data)
        data = pd.DataFrame({
            'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
            'Price': range(100, 200)  # Dummy data for stock prices
        })

        # Plot the data using matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(data['Date'], data['Price'], label=f'Stock price of {stock_symbol}')
        plt.title(f'{stock_symbol} Stock Price Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()

        # Save plot to a PNG image and encode it to base64
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        img_b64 = base64.b64encode(img.getvalue()).decode('utf-8')
        img.close()

        # Return the HTML with the image embedded
        return render_template('plot.html', img_data=img_b64, stock_symbol=stock_symbol)
    else:
        return "No stock symbol provided!", 400

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
