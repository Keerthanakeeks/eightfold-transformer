# Multi-Source Candidate Data Transformer

## Architecture

CSV Parser
↓
Notes Parser
↓
Normalizer
↓
Merger
↓
Confidence Scorer
↓
Projection Layer
↓
JSON Output

## Agent Roles

### CSV Agent
Reads structured candidate information.

### Notes Agent
Extracts skills and experience from recruiter notes.

### Normalization Agent
Standardizes names, emails, and phone numbers.

### Resolver Agent
Merges conflicting information using source priority rules.

### Confidence Agent
Assigns confidence scores to fields.

### Projection Agent
Generates configurable output JSON.

## Design Decisions

- CSV data has higher priority than free text.
- Missing values become null or empty lists.
- Duplicate skills are removed.
- Configuration controls output fields.

## Edge Cases Handled

- Missing emails
- Empty skills
- Missing notes
- Duplicate entries
- Partial candidate records