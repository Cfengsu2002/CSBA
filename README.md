# CSBA Mini Take-Home

# how to use
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Open: `http://127.0.0.1:8000/docs`  
Test: `pytest -v`

- **Assumptions:** `teamId` is valid, all `joinedAt` is sortable and not empty
- **Production improvements:** move to DB, add auth, logging/monitoring, and standardized error handling.
