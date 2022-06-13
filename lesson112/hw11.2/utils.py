import json

from config import DATA_PATH


def load_candidates_from_json(path=DATA_PATH):
    """возвращает список всех кандидатов"""
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["name"] == candidate_name:
            return candidate


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    skill_name = skill_name.lower()
    candidates = load_candidates_from_json()
    skilled_candidates = []
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name in skills:
            skilled_candidates.append(candidate)
            continue
    return skilled_candidates
