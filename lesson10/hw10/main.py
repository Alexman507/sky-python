from flask import Flask, render_template
import utils
import visual

app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = utils.get_all_candidates()
    html_code = visual.build_html_for_some_candidate(candidates)
    return html_code


@app.route('/candidates/<int:pk>')
def page_candidates_by_pk(pk):
    candidate = utils.get_candidates_by_pk(pk)
    if candidate is None:
        return "Нет такого кандидата"
    html_code = visual.build_html_for_one_candidate(candidate)
    return html_code


@app.route('/skills/<skill>')
def page_candidates_by_skills(skill):
    candidates = utils.get_candidates_by_skill(skill)
    if len(candidates) == 0:
        return "Нет таких кандидатов"
    html_code = visual.build_html_for_some_candidate(candidates)
    return html_code


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
