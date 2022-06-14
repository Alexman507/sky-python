from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def form_page():
    return render_template('form.html')


@app.route('/search')
def search_page():
    s = request.args['s']
    return f'Вы ввели слово {s}'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
