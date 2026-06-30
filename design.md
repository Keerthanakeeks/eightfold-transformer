# Multi-Source Candidate Data Transformer

## Problem Statement

Build a system that ingests candidate information from multiple sources, normalizes the data, resolves conflicts, and generates a unified candidate profile in a configurable JSON format.

The solution is designed to handle messy real-world data while remaining modular, testable, and extensible.

---

## Architecture

CSV Parser
↓
Notes Parser
↓
Normalization Layer
↓
Merge Resolver
↓
Confidence Scorer
↓
Projection Engine
↓
JSON Output

---

## Agent Roles

### CSV Agent
Reads structured candidate information from CSV files and converts it into an internal representation.

### Notes Agent
Extracts skills, experience, and additional information from recruiter notes.

### Normalization Agent
Standardizes names, emails, phone numbers, and skills into a common schema.

### Resolver Agent
Merges conflicting information using predefined source-priority rules.

### Confidence Agent
Assigns confidence scores based on data completeness and source reliability.

### Projection Agent
Produces configurable output JSON according to user-defined mappings.

---

## Agent Interaction Flow

1. The CSV Agent ingests structured candidate data from CSV files.
2. The Notes Agent extracts skills and years of experience from recruiter notes.
3. The Normalization Agent standardizes names, emails, phone numbers, and skill formats.
4. The Resolver Agent combines data from multiple sources and applies source-priority rules to resolve conflicts.
5. The Confidence Agent assigns confidence scores to fields based on source quality and completeness.
6. The Projection Agent generates the final output according to the configuration file.

This modular agent-based design separates responsibilities, making the system easier to maintain, test, and extend.

---

## Design Decisions

- Structured CSV data has higher priority than free-text recruiter notes.
- Missing values are represented as null values or empty lists.
- Duplicate skills are automatically removed.
- Configuration files determine the final output structure.
- The system is designed to support additional data sources in the future.

---

## Conflict Resolution Logic

| Field | Priority Rule |
|--------|----------------|
| Full Name | CSV > Notes |
| Email | CSV only |
| Phone | CSV only |
| Skills | Union of all sources |
| Experience | Notes > CSV |
| Headline | CSV > Generated |

The resolver ensures deterministic behavior when multiple sources provide conflicting information.

---

## Edge Cases Handled

- Missing emails
- Empty skills lists
- Missing recruiter notes
- Duplicate skill entries
- Partial candidate records
- Missing years of experience
- Null or malformed values
- Empty configuration fields

---

## Testing Strategy

The project includes unit tests covering:

- Candidate data merging
- Edge case handling
- Projection logic
- Missing field scenarios

Pytest is used to ensure correctness and maintainability.

---

## Future Improvements

- LLM-based parsing for unstructured resumes.
- Support for PDF and LinkedIn profile ingestion.
- Advanced confidence scoring mechanisms.
- Provenance tracking for every field.
- Interactive conversational recruiter agents.
- Multi-language resume support.
- Real-time candidate enrichment APIs.

---

## Conclusion

The solution follows a modular, agent-based architecture that cleanly separates parsing, normalization, conflict resolution, confidence estimation, and projection responsibilities. This design improves scalability, maintainability, and testability while enabling future AI-driven enhancements.