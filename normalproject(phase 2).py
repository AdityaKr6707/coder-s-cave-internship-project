# app.py

from flask import Flask, render_template_string
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    # Obtain the current date and time
    now = datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    
    # HTML content with inline CSS styling
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Clock</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #e0e0e0;
                font-family: 'Verdana', sans-serif;
            }
            .time-display {
                font-size: 2.5em;
                background-color: #222;
                color: #fafafa;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 0 8px rgba(0,0,0,0.3);
            }
        </style>
    </head>
    <body>
        <div class="time-display">
            {{ formatted_time }}
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(html_content, formatted_time=formatted_time)

# Run the app with debug mode enabled
if __name__ == '__main__':
    app.run(debug=True)
