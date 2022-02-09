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


def main():
    app.run(port=8080, host='')


if __name__ == '__main__':
    main()
