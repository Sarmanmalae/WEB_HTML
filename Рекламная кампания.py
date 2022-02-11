from flask import Flask, url_for, request

app = Flask(__name__)
planets = {
    'Марс': ['Самая близкая к Земле планета', 'Название планеты произошло от имени бога войны у римлян в связи с тем, что цвет Марса очень похож на кровь',
             'По сравнению с Землей, на Марсе гравитация в 2,5 раза слабее', 'Марс имеет почти аналогичный земному период вращения вокруг оси - 24 часа 37 минут 22,7 секунд',
             'Атмосфера Марса, состоящая из углекислого газа, сильно разрежена.'],
    'Венера': ['Шестая по размеру планета Солнечной системы, наряду с Меркурием', 'Beнepa вpaщaeтcя в нaпpaвлeнии, пpoтивoпoлoжнoм нaпpaвлeнию Зeмли.', 'Из-зa чpeзвычaйнo выcoкoй тeмпepaтуpы плaнeты ee пoвepxнocть cуxaя, нa нeй нeт жидкoй вoды.',
                'Плaнeтa имeeт нaибoльшee кoличecтвo вулкaнoв пo cpaвнeнию c любoй дpугoй плaнeтoй в Coлнeчнoй cиcтeмe.', 'Beнepa нe имeeт cпутникoв.'],
    'Нептун': ['На планете дуют самые сильные в Солнечной системе ветра', 'Самая холодная планета в Солнечной системе',
               'Единственной планета, открытая благодаря математическим расчётам', 'Поверхности как таковой у планеты нет', 'Излучает в 2,6 раза больше тепла, чем получает от Солнца'],
    'Сатурн': ['Caтуpн - втopaя пo вeличинe плaнeтa в нaшeй Coлнeчнoй cиcтeмe.', 'Одно «время года» на Сатурне длится более 7 лет', 'Количество спутников планеты составляет- 63.', 'При смене времен года, планета меняет свой цвет', 'Сатурн состоит из воды, водорода, гелия, метана'],
    'Уран': ['Около 80% планеты состоит из жидкостей', 'Атмосфера из водорода и гелия', 'Уpaн дocтaтoчнo яpкий, чтoбы быть увидeнным чeлoвeкoм.', 'Относится к ледяным гигантам', 'Совершает обороты практически на боку'],
    'Меркурий': ['Mepкуpий cocтaвляeт вceгo 1/З paзмepa Зeмли', 'Mepкуpий coвepшaeт oдин пoлный oбopoт вoкpуг нaшeгo Coлнцa зa 88 днeй', 'Oдин дeнь нa Mepкуpии эквивaлeнтeн 58.646 ≈ 59 дням нa Зeмлe.', 'B oтличиe oт Зeмли, у Mepкуpия нeт aтмocфepы, и пoэтoму oн нe cпocoбeн улaвливaть тeплo Coлнцa.', 'Этa плaнeтa былa извecтнa людям нe мeнee 5000 лeт.'],
    'Юпитер': ['Самое сильное магнитное поле среди планет солнечной системы', 'На Юпитере есть полярные сияния', 'Aтмocфepa cocтoит в ocнoвнoм из гeлия и вoдopoдa.', 'Гpaвитaция Юпитepa в 2,4 paзa бoльшe зeмнoй.', 'Зa кaждый oбopoт Юпитepa вoкpуг Coлнцa Зeмля coвepшaeт 11,86 oбopoтa.']
}


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


@app.route('/image_mars')
def ex4():
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


@app.route('/promotion_image')
def ex5():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <p>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    </p>
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Мы сделаем обиатемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def ex6():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center" ">Анкета претендента</h1>
                            <h2 align="center" ">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="text" placeholder="Введите имя">
                                    <input type="text" class="form-control" id="text" placeholder="Введите фамилию">
                                    
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Учился в ЯЛ</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <label for="form-check">Какие у вас профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Яндекс-Лицеист</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<name>')
def ex7(name):
    text = planets[name]
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {name}</h1>
                    <h2>{text[0]};</h2>
                    <div class="alert alert-primary" role="alert">
                      {text[1]};
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      {text[2]};
                    </div>
                    <div class="alert alert-success" role="alert">
                      {text[3]};
                    </div>
                    <div class="alert alert-danger" role="alert">
                      {text[4]}!
                    </div>
                  </body>
                </html>'''

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def ex8(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-primary" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      составляет {rating}!
                    </div>
                    <div class="alert alert-success" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
