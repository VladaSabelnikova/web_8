from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title: str) -> render_template:
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof: str) -> render_template:
    if prof in ('инженер', 'строитель', 'программист'):
        return render_template('training.html', number=1)
    return render_template('training.html', number=2)


def main():
    app.run(port=8080, host='')


if __name__ == '__main__':
    main()
