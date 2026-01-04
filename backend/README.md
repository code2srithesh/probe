PROBE — Skill Reality Verification Engine

A backend system that converts resume skill claims into verified, depth-bounded evidence using deterministic logic and AI-assisted semantic analysis.

⸻

1. Why PROBE Exists

Resumes are narratives, not proofs.

Modern hiring relies on static documents where candidates self-report expertise (“Advanced in Python”, “Strong in System Design”). These claims are rarely audited, leading to inflated profiles and weak signal for recruiters and teams.

PROBE treats every skill on a resume as a hypothesis — not a fact.

The system forces each claim to survive structured interrogation. Skills are not rated by AI; they are verified through evidence.

⸻

2. Core Idea

PROBE is a Skill Reality Engine.
	•	A resume is parsed into unverified skill claims
	•	Each skill is tested through progressively deeper probes
	•	The user’s answers generate semantic signals
	•	A deterministic rule engine converts signals into pass/fail outcomes
	•	The highest depth ever passed becomes the user’s verified skill level

The result is not an opinion. It is a bounded, auditable skill profile.

⸻

3. System Architecture

PROBE follows a strict separation of concerns to avoid AI hallucinations contaminating evaluation.

graph TD
    A[Resume PDF] -->|Text Extraction| B[LLM Parser]
    B -->|Structured Skills JSON| C[(Skill Database)]
    C -->|Unverified Skills| D[Probe Generator]
    D -->|Depth-based Questions| E[User Attempt]
    E -->|Raw Answer| F[LLM Semantic Extractor]
    F -->|Signals Only| G[Deterministic Rule Engine]
    G -->|Pass / Fail| H[(Verified Skill State)]

The LLM never decides outcomes. It only extracts meaning.

⸻

4. Judge vs Witness Model (Key Design Principle)

Most AI interview tools ask an LLM:

“Rate this answer from 1 to 10.”

This makes the AI both interpreter and judge, resulting in inconsistent and non-reproducible grading.

PROBE breaks this loop
	•	LLM = Witness
	•	Extracts concepts, intent, terminology, and confidence signals
	•	Produces structured semantic data
	•	Python Engine = Judge
	•	Applies deterministic rules
	•	Produces the final pass/fail decision

Example:
	•	LLM reports: { mentions_big_o: true, correctness: high }
	•	Rule Engine decides: PASS

This makes evaluation:
	•	repeatable
	•	explainable
	•	debuggable

⸻

5. Progressive Depth Model

Each skill is evaluated across ordered depth levels.

Typical depth progression:
	•	Depth 1 – Conceptual
	•	“What is Docker?”
	•	Depth 2 – Applied
	•	“How would you debug a failing Docker container?”
	•	Depth 3 – Design / Tradeoffs
	•	“Design a containerized deployment for a high-traffic service.”

Rules:
	•	You cannot attempt a deeper probe without passing previous levels
	•	Passing a depth permanently verifies that level
	•	Failure at a depth caps the verified level

This prevents lucky guesses and forces foundational understanding.

⸻

6. Failure Semantics (Important)

Failure is not punishment. It is information.

PROBE treats failure as a boundary signal:
	•	One failure does not immediately downgrade a skill
	•	Repeated failure at the same depth confirms a ceiling
	•	Once confirmed, the verified depth is frozen until future revalidation

This ensures:
	•	stability in skill profiles
	•	resistance to noisy answers
	•	realistic representation of ability

⸻

7. Resume Parsing & Skill Ingestion

When a resume is uploaded:
	1.	PDF text is extracted
	2.	An LLM normalizes noisy resume language
	3.	Distinct technical skills are extracted
	4.	Skills are stored as unverified claims

No skill is considered valid until proven.

⸻

8. Data Model (Simplified)
	•	Skill – canonical skill (Python, Docker, SQL)
	•	Probe – question tied to a skill and depth
	•	Attempt – user’s answer + evaluation metadata
	•	UserSkill – verified depth + last verification timestamp

The database acts as an audit log, not just storage.

⸻

9. API Flow (High Level)
	•	POST /resume/upload → extract skills
	•	GET /next-probe → select next valid probe
	•	POST /evaluate → submit answer and evaluate

Each request advances the user through a deterministic state machine.

⸻

10. Why This Is Resume-Worthy

PROBE demonstrates:
	•	real backend system design
	•	state machines and progression logic
	•	hybrid AI + deterministic architecture
	•	auditability and reproducibility
	•	resistance to AI hallucination

This is not a CRUD app with an LLM wrapper.
It is a verification engine.

⸻

11. Future Extensions
	•	Time-based skill decay and revalidation
	•	Cross-skill dependency graphs
	•	Recruiter-facing trust metrics
	•	Skill heatmaps and progression timelines

⸻

12. Final Note

PROBE is built on a simple but uncomfortable truth:

If a skill cannot survive questioning, it was never real.

This system exists to replace confidence with evidence.