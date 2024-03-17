from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <html>
    <head>
        <style>
            .header {
                font-size: 25px;
                font-weight: bold;
            }
            .success-message {
                color: green;
            }
        </style>
    </head>
    <body>
        <div class="header">Dominusoft Devops Project</div>
        <div class="success-message">Localhost on port 5000 is running successfully</div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
