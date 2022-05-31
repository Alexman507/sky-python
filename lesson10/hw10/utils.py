import json

from config import DATA_PATH


def load_data(path=DATA_PATH):
    """Загрузка данных кандидатов"""
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all_candidates():
    """Получает список кандидатов"""
    data = load_data()
    return data


def get_candidates_by_pk(pk):
    """Получает кандидата по ID"""
    candidates = load_data()
    for candidate in candidates:
        if candidate["id"] == pk:
            return candidate


def get_candidates_by_skill(skill_name):
    """Получает кандидата по навыкам"""
    skill_name = skill_name.lower()
    candidates = load_data()
    skilled_candidates = []
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name in skills:
            skilled_candidates.append(candidate)
            continue
    return skilled_candidates
