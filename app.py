from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Привіт з Render.com! Лабораторна робота №1 успішна!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)