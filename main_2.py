from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Текущее время</title>
        <style>
            body {{
                display: flex; 
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                color: #048;
                font-size: 48px;
            }}
            .time {{
                font-weight: bold;  /* Делаем шрифт жирным */
            }}
        </style>
    </head>
    <body>
        <div class="time">Текущая дата и время: {current_time}</div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
