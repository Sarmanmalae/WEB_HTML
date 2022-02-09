from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Задача 1</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/index')
def mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Задача 1</title>
                  </head>
                  <body>
                    <h1>И на Марсе будут яблони цвести!</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def ad():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Задача 2</title>
                  </head>
                  <body>
                    <p>Человечество вырастает из детства.</p>
                    <p>Человечеству мала одна планета.</p>
                    <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p>И начнем с Марса!</p>
                    <p>Присоединяйся!</p>
                  </body>
                </html>"""


@app.route('/image_mars')
def ex3():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <p>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    </p>
                    <p>
                    Вот такая она, красная планета
                    </p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
