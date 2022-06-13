from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    """Выводит на странице всех кандидатов ссылками
    (я не понял, как в хтмл грамотно прокинуть id, если
    не через зип-словарь)"""
    load_ = utils.load_candidates_from_json()
    names = [name['name'] for name in load_]
    id_ = [pk['id'] for pk in load_]
    dict_ = dict(zip(names, id_))
    global dict_
    return render_template('list.html', names=names, dict_=dict_)


@app.route('/candidate/<int:x>')
def page_candidates_by_pk(x):
    """Выводит карточку кандидата на страницу"""
    candidate_data = utils.get_candidate(x)
    name = candidate_data['name']
    position = candidate_data['position']
    picture = candidate_data['picture']
    skills = candidate_data['skills']
    html_code = render_template('card.html', name=name, position=position, picture=picture, skills=skills)

    return html_code


@app.route('/search/<candidate_name>')
def page_candidates_by_name(name):
    candidates = utils.get_candidates_by_name(name)
    if len(candidates) == 0:
        return "Нет таких кандидатов"
    html_code = render_template('search.html', name=name, len_=len(candidates), dict_=dict_)
    return html_code


@app.route('/skill/<skill>')
def page_candidates_by_name(name):
    candidates = utils.get_candidates_by_name(name)
    if len(candidates) == 0:
        return "Нет таких кандидатов"
    html_code = render_template('search.html', name=name, len_=len(candidates), dict_=dict_)
    return html_code


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
