# Eightfold Candidate Transformer

## Overview
This project transforms candidate information from multiple sources into a unified profile.

## Features
- CSV candidate parsing
- Recruiter notes parsing
- Data normalization
- Conflict resolution
- Confidence scoring
- Provenance tracking
- Configurable output projection
- Edge case handling
- Unit tests

## Setup

Activate environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install pandas pytest pydantic typer python-dateutil pycountry
```

Run:

```powershell
python src/main.py
```

Run tests:

```powershell
pytest
```