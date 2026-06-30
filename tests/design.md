# Design Document

## System Overview

The system transforms candidate information from multiple sources into a canonical profile.

## Architecture

CSV Source
↓

CSV Parser Agent
↓

Normalization Agent
↓

Merge Agent
↓

Confidence Agent
↓

Projection Agent
↓

Output JSON

## Agent Responsibilities

### CSV Agent
Reads structured candidate information.

### Notes Agent
Extracts years of experience and skills.

### Merge Agent
Combines conflicting information using source priority rules.

### Confidence Agent
Assigns reliability scores.

### Projection Agent
Builds configurable output structures.

## Conflict Resolution Logic

Priority:

1. CSV data
2. Recruiter notes

Structured sources are treated as more reliable.

## Confidence Logic

| Field | Confidence |
|--------|-------------|
| Name | 1.0 |
| Email | 1.0 |
| Phone | 1.0 |
| Headline | 0.95 |
| Skills | 0.85 |
| Experience | 0.80 |

## Provenance Tracking

Each field records its origin:

- candidate.csv
- recruiter_notes.txt

## Edge Cases

- Missing emails
- Missing skills
- Empty notes
- Partial profiles

## Assumptions

- Candidate names are unique.
- Structured data is more reliable.
- Recruiter notes supplement missing information.

## Future Work

- LLM-based extraction
- Resume PDF support
- Duplicate detection
- Batch processing