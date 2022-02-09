from typing import Union

from flask import Flask, render_template

from static.const import ALL_PROFESSIONS

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title: str) -> render_template:
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof: str) -> render_template:
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<lst>')
def list_prof(lst: str) -> Union[render_template, str]:

    if lst not in ('ol', 'ul'):
        return f'Неверный параметр {lst}'

    return render_template(
        'list_prof.html',
        lst=lst,
        professions=ALL_PROFESSIONS
    )


@app.route('/answer')
@app.route('/auto_answer ')
def auto_answer() -> render_template:
    # test_param — временные данные, потом их подменят на обработанные формы.
    test_param = {
        'title': 'Анкета',
        'surname': 'Сабельникова',
        'name': 'Влада',
        'education': 'Лицей Академии Яндекса',
        'profession': 'программист',
        'sex': 'female',
        'motivation': 'За это много платят',
        'ready': 'True'
    }
    title = test_param.pop('title')
    return render_template('auto_answer.html', title=title, param=test_param)


def main():
    app.run(port=8080, host='')


if __name__ == '__main__':
    main()
