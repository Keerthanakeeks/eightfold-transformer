import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from merger.resolver import merge_candidate_data


def test_empty_skills():

    csv_data = {
        "full_name": "Vishnu"
    }

    notes_data = {}

    result = merge_candidate_data(csv_data, notes_data)

    assert result["skills"] == []


def test_missing_email():

    csv_data = {
        "full_name": "Vishnu",
        "emails": []
    }

    notes_data = {}

    result = merge_candidate_data(csv_data, notes_data)

    assert result["emails"] == []