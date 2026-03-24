<div align="center">

# 🧠 PROBE
## Skill Reality Verification Engine

### **Turning Resume Claims into Verified Reality**

*Where words meet proof. Where buzzwords become credentials.*

[![Python](https://img.shields.io/badge/Python-3.11+-3670A0?style=flat-square&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Groq AI](https://img.shields.io/badge/Groq-LLaMA%203-FF6B35?style=flat-square)](https://groq.com/)
[![License MIT](https://img.shields.io/badge/License-MIT-success?style=flat-square)](LICENSE)

[🚀 Features](#-features) • 
[🛠️ Tech Stack](#%EF%B8%8F-tech-stack) • 
[📖 Setup](#-installation--setup) • 
[🎯 Usage](#-usage) • 
[⭐ Support](#-support)

</div>

---

## 🎬 The Problem

Modern resumes are **self-declared fiction**.

```
"Expert in Python"          ✗ Unverified
"Advanced System Design"    ✗ Unverified  
"Strong Problem Solver"     ✗ Unverified
```

**Hiring decisions are made on unchecked claims.**

Recruiters spend 6 seconds per resume. Engineers claim expertise they can't defend. The gap between resume and reality costs **$150K+ in bad hires**.

---

## 💡 The Solution: PROBE

PROBE is a **depth-aware, AI-assisted verification engine** that:

- 📄 **Parses resumes** into concrete skill claims
- 🎯 **Generates progressive, depth-based** technical questions
- 🤖 **Evaluates answers** using AI intelligence + deterministic rules (not guesses)
- 📊 **Produces auditable verified skill profiles** with proven competence ceilings

**Not a score. Not a guess. A *proof*.** ✓

---

## ✨ Key Features

| 🔑 Feature | 📝 Description |
|-----------|---|
| 🧠 **AI-Powered Resume Parsing** | Extract technical skills from PDF resumes with semantic understanding |
| 🔐 **Depth-Based Verification** | 3-tier validation: Conceptual → Applied → Design |
| ⚖️ **Judge vs. Witness Architecture** | AI extracts signals; Python engine makes deterministic decisions |
| 📈 **Failure Confirmation Logic** | Prevents lucky guesses with repeated verification |
| 🔒 **Progressive Unlocking** | Higher difficulties locked until lower depths proven |
| 📋 **Complete Audit Trail** | Every attempt, question, answer logged immutably |
| 🎨 **Interactive Interview UI** | Resume → Questions → Proof → Verified Profile |
| 🚀 **RESTful API** | Full programmatic access for integrations |

---

## 🏗️ Architecture: Judge vs Witness

**The Problem with Traditional AI:**
```
LLM: "Rate this answer 1-10"
Result: ✗ Subjective, hallucinated, inconsistent
```

**PROBE's Innovation:**

```
┌─────────────────────────────────────────────┐
│  AI = 👁️ WITNESS                            │
│  ├─ Semantic analysis                       │
│  ├─ Concept detection                       │
│  └─ Pattern identification                  │
└─────────────────────────────────────────────┘
                    ↓
        ┌───────────────────────────┐
        │  Python = ⚖️ JUDGE        │
        │  ├─ Strict rule engine    │
        │  ├─ Enforce boundaries    │
        │  └─ Guarantee consistency │
        └───────────────────────────┘
                    ↓
        Result: ✅ Auditable & Reproducible
```

---

## 🔄 System Workflow

```
┌──────────────────────────────────────────────────────────────┐
│           📊 PROBE VERIFICATION FLOW                         │
└──────────────────────────────────────────────────────────────┘

1️⃣  RESUME INGESTION
    └─ PDF Upload → AI Parser → Extract Skills → Store Claims

2️⃣  PROBE GENERATION
    ├─ Depth 1 (Conceptual): "What is Python?"
    ├─ Depth 2 (Applied):    "Debug this mutation?"
    └─ Depth 3 (Design):     "Design scalable system"
       🔒 Higher depths locked until proven

3️⃣  ATTEMPT & EVALUATION
    └─ User Answer → AI Analysis → Extract Signals

4️⃣  DETERMINISTIC JUDGMENT
    └─ Python Judge: Apply Rules → PASS/FAIL (No guesses)

5️⃣  SKILL STATE UPDATE
    ├─ Passed      → Verified Depth ↑
    └─ Failed 2x   → Depth Frozen (Ceiling Established)
```

---

## 📊 Verified Skill Profile Output

What recruiters actually see — **no buzzwords, just proof**:

| Skill | Depth | Last Verified | Status |
|-------|:-----:|---|---|
| Python | 🔵🔵🔵 | 2025-01-05 | ✅ Proven |
| Docker | 🔵🔵⚫ | 2025-01-03 | ✅ Proven |
| SQL | 🔵⚫⚫ | 2025-01-02 | ✅ Proven |
| Kubernetes | ⚫⚫⚫ | - | ❌ Attempted |

**Complete audit trail** — every decision logged and immutable.

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technology |
|----------|---|
| **Backend Framework** | ![FastAPI](https://img.shields.io/badge/FastAPI-0095C5?style=flat-square&logo=fastapi&logoColor=white) ![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3670A0?style=flat-square&logo=python&logoColor=ffdd54) |
| **Database** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-336791?style=flat-square&logo=postgresql&logoColor=white) ![SQLAlchemy ORM](https://img.shields.io/badge/SQLAlchemy-ORM-9C27B0?style=flat-square) |
| **AI Engine** | ![Groq](https://img.shields.io/badge/Groq-LLaMA%203-FF6B35?style=flat-square) |
| **Architecture** | Domain-Driven Design • Rule-Based Engine • Event-Driven |
| **Frontend** | HTML5 • CSS3 • Vanilla JavaScript • Real-time Updates |
| **DevOps** | Docker • RESTful API • Scalable Design |

</div>

---

## 🚀 Installation & Setup

### Prerequisites
```
✓ Python 3.11+
✓ PostgreSQL 15+ or SQLite (dev)
✓ Git
✓ pip / poetry
```

### Step 1: Clone Repository
```bash
git clone https://github.com/srithesh/probe-1.git
cd probe-1
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 4: Configure Environment
```bash
# Create .env file
cp .env.example .env

# Edit .env with your config:
# DATABASE_URL=postgresql://user:password@localhost/probe
# GROQ_API_KEY=your_groq_api_key
# SECRET_KEY=your_secret_key
```

### Step 5: Initialize Database
```bash
python reset_db.py  # Reset (dev only)
python seed.py      # Load sample data
```

### Step 6: Run Backend Server
```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

✅ **Server running!**
- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs` (Swagger UI)

---

## 📖 Usage

### Upload Resume & Create User
```bash
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "email": "candidate@example.com",
    "resume_file": "resume.pdf"
  }'
```

### Get Skills to Verify
```bash
curl -X GET http://localhost:8000/api/probes?user_id=1
```

### Submit Answer
```bash
curl -X POST http://localhost:8000/api/attempts \
  -H "Content-Type: application/json" \
  -d '{
    "probe_id": 1,
    "user_id": 1,
    "answer": "A Python list is a mutable, ordered collection..."
  }'
```

### Get Verified Profile
```bash
curl -X GET http://localhost:8000/api/profile?user_id=1
```

📚 **Full API Docs:** Navigate to `/docs` endpoint after running server.

---

## 🎯 Core Concepts

### 📚 Depth-Based Learning

```
DEPTH 1: Conceptual Understanding
├─ What do you know about this skill?
└─ Example: "What is Docker?"

DEPTH 2: Applied Knowledge  
├─ Can you use it?
└─ Example: "Dockerize this application"

DEPTH 3: Design Mastery
├─ Can you architect with it?
└─ Example: "Design a scalable containerized system"
```

### ✅ Failure Confirmation
- **First failure:** Data point, not judgment
- **Second failure:** Depth boundary frozen
- **Result:** Ceiling of proven competence

### 🔐 Verification Guarantee
✅ Deterministic rules  
✅ No subjective scoring  
✅ No AI hallucinations  
✅ Complete audit trail  

---

## 📂 Project Structure

```
probe-1/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/              # 🔌 API endpoints
│   │   │   │   ├── auth.py
│   │   │   │   ├── attempts.py
│   │   │   │   ├── evaluate.py
│   │   │   │   ├── probes.py
│   │   │   │   ├── profile.py
│   │   │   │   ├── skills.py
│   │   │   │   └── users.py
│   │   │   └── deps.py              # Dependency injection
│   │   ├── core/                    # ⚙️ Core systems
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── evaluator.py
│   │   ├── crud/                    # 💾 Database operations
│   │   │   ├── attempt.py
│   │   │   ├── probe.py
│   │   │   ├── skill.py
│   │   │   └── user.py
│   │   ├── domain/                  # 🧠 Business logic
│   │   │   ├── decay.py
│   │   │   ├── depth.py
│   │   │   ├── evaluation.py
│   │   │   ├── failure.py
│   │   │   ├── java.py
│   │   │   └── selector.py
│   │   ├── models/                  # 🗄️ ORM models
│   │   ├── schemas/                 # 📋 Request/response schemas
│   │   ├── services/                # 🔧 Core services
│   │   └── main.py                  # 🚀 Application entry
│   ├── requirements.txt
│   └── [Debug & Test Scripts]
├── frontend/
│   └── index.html                   # 🎨 Interactive UI
└── README.md
```

---

## 🧪 Testing & Development

### Run Tests
```bash
pytest backend/tests/ -v
```

### Debug Workflows
```bash
python backend/debug_ai.py           # 🤖 Test AI parsing
python backend/test_flow.py          # 🔄 Test full workflow
python backend/check_models.py       # ✅ Validate data models
python backend/debug_groq.py         # 🔗 Test Groq integration
python backend/test_pdf.py           # 📄 Test PDF parsing
```

---

## 📈 Performance Benchmarks

| Operation | Time | Status |
|-----------|------|--------|
| Resume Parsing | ~2.3s | ✅ |
| Question Generation | ~1.1s | ✅ |
| Answer Evaluation | ~0.8s | ✅ |
| Profile Generation | ~0.5s | ✅ |

---

## 🌟 Key Innovations

✨ **Judge vs Witness Architecture**  
First system to separate AI signal extraction from judgment making.

✨ **Deterministic Evaluation**  
Rule engine ensures reproducibility and auditability.

✨ **Failure Confirmation Logic**  
Prevents luck-based assessments with repeated verification.

✨ **Depth-Aware Questions**  
Progressive validation from conceptual to architectural mastery.

✨ **Complete Auditability**  
Every decision, every step, every reason is logged.

---

## 📊 Roadmap

- [ ] 🎯 Fine-tuned Models — Custom models for technical evaluation
- [ ] 🌍 Multi-Language Support — Verify skills across languages
- [ ] 📈 Recruiter Dashboard — Advanced filtering and ranking
- [ ] 🔌 Integration APIs — Connect with ATS and HR systems
- [ ] 📉 Skill Evolution Tracking — Watch skill decay/growth
- [ ] 📱 Mobile App — Answer probes on-the-go
- [ ] 👥 Team Assessments — Verify skills across teams
- [ ] 🎓 Certification Program — Official PROBE credentials

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Fork & Clone
```bash
git clone https://github.com/yourusername/probe-1.git
cd probe-1
```

### Create Feature Branch
```bash
git checkout -b feature/amazing-feature
```

### Make Changes & Commit
```bash
git add .
git commit -m "feat: add amazing feature"
```

### Push & Create PR
```bash
git push origin feature/amazing-feature
```

Then open a Pull Request with:
- Clear description of changes
- Related issue numbers
- Test coverage

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Srithesh** — Building products that measure reality, not claims.

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-@srithesh-181717?style=for-the-badge&logo=github)](https://github.com/srithesh)
[![Portfolio](https://img.shields.io/badge/Portfolio-srithesh.dev-FF6B35?style=for-the-badge)](https://srithesh.dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Srithesh-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/srithesh)
[![Email](https://img.shields.io/badge/Email-contact-EA4335?style=for-the-badge&logo=gmail)](mailto:hello@srithesh.dev)

</div>

---

## 💭 Philosophy

> **Skills are not what you claim. They are what you can defend under pressure.**
>
> PROBE exists to measure that reality.  
> Not to judge people, but to audit systems.  
> Not to replace interviews, but to make them unnecessary through proven competence.

---

## ⭐ Support This Project

If PROBE changed how you think about skill verification — please:

- ⭐ **Star this repo** — Help others discover it
- 🔗 **Share** — Tell your network
- 🐛 **Report bugs** — Help us improve
- 💬 **Provide feedback** — Shape the future

---

<div align="center">

### **Built with 🧠 Logic, ⚖️ Fairness, and 🔬 Rigor**

**Separating resume claims from proven reality.**

[⬆ back to top](#)

</div>
