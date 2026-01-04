🧠 PROBE — Skill Reality Verification Engine

Turning resume claims into verified reality.
PROBE is a depth-aware, AI-assisted backend system that audits what you say you know — and measures what you can actually prove.


⸻

🚀 Why PROBE?

Modern resumes are self-declared fiction.
	•	“Expert in Python” 📝
	•	“Advanced System Design” 📝
	•	“Strong Problem Solver” 📝

But hiring decisions are made on these unchecked claims.

PROBE fixes this.
It treats every resume as a list of unverified hypotheses — and forces the candidate to validate them through a structured interrogation engine.

⸻

🧩 What PROBE Does

✨ Converts resumes into unverified skill claims
✨ Generates progressive depth-based questions
✨ Evaluates answers using AI + deterministic rules
✨ Produces a verified skill profile instead of buzzwords

The result is not a score — it’s a ceiling of proven competence.

⸻

🔁 System Workflow (End-to-End)

1️⃣ Resume Ingestion
	•	User uploads a PDF resume
	•	AI parses raw text and extracts technical skills
	•	Skills are stored as Unverified Claims

2️⃣ Probe Generation

For each skill, PROBE generates depth-specific probes:

Depth	Meaning	Example
1	Conceptual	“What is a Python list?”
2	Applied	“How do you debug a list mutation bug?”
3	Design	“Design a system using Python lists efficiently”

🔒 Higher depths are locked until lower depths are proven.

3️⃣ Attempt & Evaluation
	•	User submits an answer
	•	Answer is analyzed semantically by AI
	•	Core signals (concepts, accuracy, intent) are extracted

4️⃣ Deterministic Judgment
	•	Python rule engine decides PASS / FAIL
	•	No subjective scoring
	•	No hallucinated grades

5️⃣ Skill State Update
	•	Passed → verified depth increases
	•	Failed twice → depth boundary is frozen

⸻

🧠 Judge vs Witness Architecture (Key Innovation)

Most AI interview systems do this:

“LLM, rate this answer from 1–10” ❌

PROBE does not trust AI judgment.

👁 AI = Witness
	•	Extracts semantic facts
	•	Detects presence of concepts
	•	Identifies reasoning patterns

⚖️ Python = Judge
	•	Applies strict, deterministic rules
	•	Enforces depth boundaries
	•	Guarantees consistent outcomes

✅ Result: reproducible, auditable evaluations

⸻

📉 Failure Confirmation Logic

One bad answer shouldn’t define a candidate.

PROBE introduces failure confirmation:
	•	A depth is considered failed only after repeated failure
	•	Once confirmed, higher depths are locked
	•	The verified depth becomes a stable upper bound

This prevents:
	•	Lucky guesses 🎲
	•	Random regressions
	•	Inflated skill claims

⸻

📊 What Recruiters Actually See

✅ Verified Skill Profile

Skill	Verified Depth	Last Verified
Python	3	2025-01-05
Docker	2	2025-01-03
SQL	1	2025-01-02

🧾 Full Audit Trail

Every attempt is stored:
	•	Question
	•	User answer
	•	Pass/Fail
	•	Depth evaluated
	•	Timestamp

Nothing is hidden. Nothing is guessed.

⸻

🖥 UI Enhancements

The UI is designed to feel like an interactive technical interview, not a form:
	•	Clear skill progression
	•	Locked depth indicators 🔒
	•	Immediate feedback
	•	Resume → Proof → Profile flow

UI changes focus on clarity, trust, and reduced cognitive load.

⸻

🛠 Tech Stack
	•	Backend: FastAPI
	•	ORM: SQLAlchemy
	•	Database: PostgreSQL / SQLite
	•	AI Engine: Groq (LLaMA 3)
	•	Architecture: Domain-driven, rule-based evaluation

⸻

🌱 Project Status

PROBE is actively evolving.

Current focus:
	•	API stability
	•	Resume upload robustness
	•	Probe selection logic
	•	UI polish

This project is intentionally backend-heavy and logic-first — designed to demonstrate real engineering judgment, not just API wiring.

⸻

🧠 Philosophy

Skills are not what you claim.
They are what you can defend under pressure.

PROBE exists to measure that reality.

⸻

⭐ If this project made you think differently about resumes, interviews, or AI evaluation — it’s doing its job.
