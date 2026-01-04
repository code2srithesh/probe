# PROBE // Skill Reality Verification Engine

> **A deterministic engine that converts resume claims into verified, depth-bounded skill profiles using AI-assisted semantic analysis.**

![Python](https://img.shields.io/badge/Python-FastAPI-blue?style=flat&logo=python)
![AI](https://img.shields.io/badge/AI-Groq%20Llama%203-purple?style=flat)
![Database](https://img.shields.io/badge/DB-SQLAlchemy-green?style=flat)

---

## ⚡ The Problem: Resume Inflation
In modern hiring, resumes are static, unverified documents. Candidates claim "Expert" status in tools they have only touched once. 
**PROBE** solves this by treating a resume as a set of **unverified claims** that must be audited through a progressive interrogation engine.

## 🏗 System Architecture

The system follows a strict **"Witness vs. Judge"** architecture to prevent AI hallucinations from affecting the evaluation.

```mermaid
graph TD
    A[Resume PDF] -->|Parsing Layer| B(Groq LPU)
    B -->|JSON Extraction| C{Skill Database}
    C -->|Unverified Claims| D[Probe Generator]
    D -->|Level 1-3 Questions| E[User Attempt]
    E -->|Raw Answer| F[Groq Semantic Analyzer]
    F -->|Semantic Signals| G[Python Rule Engine]
    G -->|Deterministic Pass/Fail| H[Verified Profile]

💎 Why PROBE is Unique? (Technical Differentiators)
Unlike standard "AI Interview" tools that blindly trust LLM outputs, PROBE uses a Hybrid Evaluation Architecture designed to eliminate hallucinations and enforce standardization.

1. The "Judge vs. Witness" Protocol
Most AI apps use the LLM as the Judge (asking "Rate this answer 1-10"). This leads to subjective, inconsistent grading.

PROBE uses the LLM only as a Witness (Semantic Extractor). It asks: "Does the answer contain the concept of 'Big O Notation'?"

The Python Engine acts as the Judge. It applies deterministic logic: If concept_present == True AND accuracy == High THEN Pass.

Result: Grading is consistent, reproducible, and immune to "AI Mood."

2. The "Reality Gap" Visualization
Resumes suffer from inflation. A candidate might claim "Expert" status in 10 skills.

PROBE introduces the Verified High-Water Mark.

It visualizes the delta between Claimed Skill (Level 10) vs. Verified Reality (Level 3).

This provides a single, quantified metric for recruiter trust: "The Candidate is 30% Verified."

3. Latency-Optimized via Groq LPU
Real-time interrogation requires sub-second responses.

Instead of standard GPU inference (which can take 2-5 seconds), PROBE utilizes Groq’s LPU (Language Processing Unit) architecture.

This achieves <300ms inference speeds, making the "AI Interrogator" feel instant and conversational rather than sluggish.

4. Progressive Disclosure State Machine
The system implements a Dependency Graph for questioning.

A user cannot attempt a Level 3 (System Design) probe until they have cryptographically verified Level 2 (Debugging).

This prevents "lucky guesses" and ensures a solid foundation before testing advanced concepts.