def merge_candidate_data(csv_data, notes_data):

    merged = {
        "full_name": csv_data.get("full_name"),
        "emails": csv_data.get("emails", []),
        "phones": csv_data.get("phones", []),
        "headline": csv_data.get("headline"),
        "years_experience": notes_data.get("years_experience"),
        "skills": notes_data.get("skills", [])
    }

    # Track where each field came from
    merged["_provenance"] = {
        "full_name": "candidate.csv",
        "emails": "candidate.csv",
        "phones": "candidate.csv",
        "headline": "candidate.csv",
        "years_experience": "recruiter_notes.txt",
        "skills": "recruiter_notes.txt"
    }

    # Confidence scores
    merged["_confidence"] = {
        "full_name": 1.0,
        "emails": 1.0,
        "phones": 1.0,
        "headline": 0.95,
        "years_experience": 0.80,
        "skills": 0.85
    }

    return merged