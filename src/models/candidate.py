from pydantic import BaseModel


class Candidate(BaseModel):
    candidate_id: str
    full_name: str | None = None
    emails: list[str] = []
    phones: list[str] = []
    headline: str | None = None
    years_experience: float | None = None
    skills: list[str] = []
    provenance: list[dict] = []
    overall_confidence: float = 0.0