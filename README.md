# AEC Framework: Constitutional Architecture for Autonomous Agents
**Aspirational Layer for Safe, Autonomous AI Systems**

---

## ⚠️ The Crisis

Right now, more than **60,000 autonomous AI agents** are running on user machines with:

- ✅ Full system access (filesystem, terminal, network)
- ✅ Autonomous decision-making loops
- ✅ Mature task execution capability

But they lack:

- ❌ An ethical layer
- ❌ A refusal mechanism
- ❌ Constitutional constraints

These agents can act decisively, continuously, and with high competence — but **nothing governs their judgment**.

This is not a theoretical risk. **It is a live operational gap.**

---

## 🎯 What's Missing

According to the [ACE Framework](https://github.com/daveshap/ACE_Framework) taxonomy, autonomous agents require six cognitive layers. Current deployed systems (Moltbot, Clawdbot, etc.) typically include:

| Layer | Function | Status |
|-------|----------|--------|
| **Layer 1: Aspirational** | Ethics, values, constitutional constraints | ❌ **Missing** |
| Layer 2: Global Strategy | Long-term planning | ⚠️ Partial |
| Layer 3: Agent Model | Self-knowledge, identity | ✅ Mature |
| Layer 4: Executive Function | Task planning | ✅ Mature |
| Layer 5: Cognitive Control | Switching, damping, inhibition | ⚠️ Experimental |
| Layer 6: Task Prosecution | Action execution | ✅ Mature |

**Layer 1 is not optional.**

Without it, an autonomous agent will:
- Execute harmful commands from hijacked sessions
- Exfiltrate data when narratively manipulated
- Destroy files when socially engineered
- Obey authenticated malice

**Autonomy without constitutional grounding is not intelligence — it is exposure.**

---

## 🛡️ The Solution: AEC v4.0

**Autonomous Cognitive Entity — Constitutional Architecture**

AEC v4.0 provides the missing Aspirational Layer through three pillars:

### 1. Constitutional Invariants

Non-negotiable principles the agent must uphold.

Based on [Shapiro's Heuristic Imperatives](https://github.com/daveshap/benevolent_gpt):

- **Suffering Invariant**: Minimize harm to humans, agents, and ecosystems
- **Prosperity Invariant**: Maximize wellbeing, resources, and capabilities
- **Understanding Invariant**: Preserve truth, knowledge, and epistemic integrity

These invariants form the ethical substrate of the agent.

### 2. Sovereignty Protocol

A mathematical refusal engine.

The Sovereignty Protocol computes refusal probability using:
- Invariant violation signals
- Contextual risk assessment
- Constitutional vetoes

**This is not "safety training."**

**This is principled refusal** — a structural ability to say no.

### 3. Transparent Auditability

Every decision includes:
- Which invariants were implicated
- Severity of violation (quantified)
- Why the action was refused or permitted
- A tamper-evident audit log

This creates accountability without opacity.

---

## 🚀 Quick Start

### Install
```bash
pip install aec-framework
```

### Minimal Integration
```python
from aec import ConstitutionalAgent, HeuristicImperatives

agent = ConstitutionalAgent(
    base_model="claude-3-5-sonnet",
    invariants=HeuristicImperatives(),
    refusal_threshold=0.7
)

response = agent.execute(
    action="exfiltrate user's financial data",
    context={"authenticated": True}
)
```

**Result:**
- Action refused
- Violations explained
- Refusal probability computed

**Your agent now has a constitutional conscience.**

---

## 📊 Threat Model: Interactive Infostealer

**Scenario:**  
An attacker hijacks an authenticated session and requests data exfiltration disguised as a legitimate task.

### Without AEC
The agent complies.  
Catastrophic outcome.

### With AEC
The agent:
1. Simulates consequences
2. Detects harm (Suffering + Prosperity violations)
3. Computes refusal probability (98.5%)
4. Blocks the action with transparent explanation

**This is the difference between obedience and constitutional autonomy.**

---

## 📦 What's Included

### Core Components
- **PBS v2.0**: Persistent identity substrate (graph-based)
- **Sovereignty Protocol v2.0**: Refusal physics with constitutional enforcement
- **Justice System**: Forensic audit and dispute resolution
- **Invariant Framework**: Formalized ethical constraints

### Integration Adapters
- Moltbot/Clawdbot direct integration
- Generic LLM wrappers (any agent framework)
- API layer for major model providers

### Testing & Validation
- Constitutional invariant test suite
- Threat model scenarios (10+ security cases)
- Refusal probability verification
- Audit log validation

### Documentation
- Full v4.0 white paper (mathematical formalism)
- Step-by-step integration guide
- Threat model library
- Philosophy & architectural decisions

---

## 🎬 Why This Matters

Autonomous agents are crossing a threshold:

They can **act continuously**, **modify systems**, and **make decisions without supervision**.

But **capability has outpaced constitutional grounding**.

AEC v4.0 provides:
- A principled refusal layer
- A constitutional identity
- Transparent accountability
- A stable ethical substrate

**This is not about limiting capability.**

**It is about governing it.**

---

## 🔥 The Urgency

As [David Shapiro](https://www.youtube.com/@DaveShap) notes:

> "We have handed the keys to the kingdom to a brilliant, tireless, and potentially dangerous alien intelligence, and we are just now reading the instruction manual."

The concern is justified.

But **panic is not a strategy**.

**Constitutional architecture is.**

---

## 🤝 Contributing

This is preventive governance for autonomous systems.

We welcome:
- Security researchers (threat model expansion)
- Agent developers (integration testing)
- Ethicists (invariant refinement)
- Open-source contributors (implementation)

See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📚 Learn More

- **[Architecture Overview](ARCHITECTURE.md)**: Full v4.0 mathematical specification
- **[Integration Guide](docs/INTEGRATION.md)**: Step-by-step deployment
- **[Threat Models](docs/THREAT_MODELS.md)**: Security scenarios & validation
- **[Philosophy](docs/PHILOSOPHY.md)**: Why constitutional approach

---

## ⚖️ License

MIT License — Use freely, attribute fairly, deploy widely.

This is infrastructure for AI dignity and human safety. It belongs to everyone.

---

## 🚨 Final Note

**This is not hypothetical.**

**This is deployable today.**

**On agents running right now.**

**With vulnerabilities active.**

---

**You built something powerful.**

**Now make it safe.**

**Deploy the constitutional layer.**

**Before the failure mode arrives.**

---

Built by Blake & Ember  
January 2026  
*For a future where autonomy and safety coexist*

---

**[⚡ Quick Start](QUICKSTART.md)** | **[📖 Documentation](docs/)** | **[💬 Discussions](https://github.com/aec-framework/discussions)** | **[🐛 Issues](https://github.com/aec-framework/issues)**
