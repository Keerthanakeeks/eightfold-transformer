import json

from parser.csv_parser import parse_csv
from parser.notes_parser import parse_notes
from merger.resolver import merge_candidate_data
from projector.config_projection import project_data


# Read sources
csv_data = parse_csv("samples/candidate.csv")
notes_data = parse_notes("samples/recruiter_notes.txt")

# Merge
profile = merge_candidate_data(csv_data, notes_data)

# Load configuration
with open("samples/config.json") as f:
    config = json.load(f)

# Apply projection
output = project_data(profile, config)

# Save final JSON
with open("output.json", "w") as f:
    json.dump(output, f, indent=4)

print("✅ Config-based output generated!")