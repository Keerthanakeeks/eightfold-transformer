import re


SKILLS = [
    "Python",
    "SQL",
    "Java",
    "Spark",
    "AWS"
]


def parse_notes(path):

    with open(path, "r") as f:
        text = f.read()

    # Extract years of experience
    years_match = re.search(r"(\d+)\s+years", text)

    years = int(years_match.group(1)) if years_match else None

    # Extract skills
    skills_found = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            skills_found.append(skill)

    return {
        "years_experience": years,
        "skills": skills_found
    }