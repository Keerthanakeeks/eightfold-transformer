import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from merger.resolver import merge_candidate_data


def test_merge():
    csv_data = {
        "full_name": "Vishnu",
        "emails": ["vishnu@gmail.com"],
        "phones": ["9876543210"],
        "headline": "Software Engineer Intern"
    }

    notes_data = {
        "years_experience": 2,
        "skills": ["Python", "SQL"]
    }

    result = merge_candidate_data(csv_data, notes_data)

    assert result["full_name"] == "Vishnu"
    assert result["years_experience"] == 2
    assert "Python" in result["skills"]