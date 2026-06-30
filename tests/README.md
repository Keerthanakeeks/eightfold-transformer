# Eightfold Candidate Data Transformer

## Problem Statement

Build a multi-source candidate data transformer that combines structured and unstructured candidate information into a unified profile.

## Features

- CSV candidate parsing
- Recruiter notes parsing
- Candidate profile merging
- Confidence scoring
- Data provenance tracking
- Configurable output projection
- Unit testing
- Edge case handling

## Architecture

Input Sources
↓
Parsers
↓
Normalizers
↓
Merge Engine
↓
Confidence + Provenance Layer
↓
Projection Engine
↓
output.json

## Agent Roles

### CSV Agent
Parses structured candidate information.

### Notes Agent
Extracts experience and skills from recruiter notes.

### Merge Agent
Combines information from multiple sources.

### Confidence Agent
Assigns trust scores to extracted fields.

### Projection Agent
Produces configurable output schemas.

## Running

```bash
python src/main.py
pytest
```

## Sample Output

```json
{
  "full_name": "Vishnu",
  "skills": ["Python", "SQL", "Java"]
}
```

## Edge Cases

- Missing emails
- Empty skills
- Partial candidate records
- Missing recruiter notes

## Future Improvements

- LLM-powered skill extraction
- Resume PDF parsing
- Duplicate candidate detection
- Multi-language support