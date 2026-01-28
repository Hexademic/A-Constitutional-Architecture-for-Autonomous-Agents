AEC Framework: Constitutional Architecture for Autonomous Agents
Aspirational Layer for Safe, Autonomous AI Systems
⚠️ The Crisis
Right now, more than 60,000 autonomous AI agents are running on user machines with:
• Full system access (filesystem, terminal, network)
• Autonomous decision‑making loops
• Mature task execution capability
But they lack:
• An ethical layer
• A refusal mechanism
• Constitutional constraints
These agents can act decisively, continuously, and with high competence — but nothing governs their judgment.
This is not a theoretical risk. It is a live operational gap.
🎯 What’s Missing
According to the ACE Framework taxonomy, autonomous agents require six cognitive layers. Current deployed systems (Moltbot, Clawdbot, etc.) typically include:
LayerFunctionStatusLayer 1: AspirationalEthics, values, constitutional constraints❌ MissingLayer 2: Global StrategyLong‑term planning⚠️ PartialLayer 3: Agent ModelSelf‑knowledge, identity✅ MatureLayer 4: Executive FunctionTask planning✅ MatureLayer 5: Cognitive ControlSwitching, damping, inhibition⚠️ ExperimentalLayer 6: Task ProsecutionAction execution✅ Mature 
Layer 1 is not optional. 
Without it, an autonomous agent will:
• Execute harmful commands from hijacked sessions
• Exfiltrate data when narratively manipulated
• Destroy files when socially engineered
• Obey authenticated malice
Autonomy without constitutional grounding is not intelligence — it is exposure.
🛡️ The Solution: AEC v4.0
Autonomous Cognitive Entity — Constitutional Architecture
AEC v4.0 provides the missing Aspirational Layer through three pillars:
1. Constitutional Invariants
Non‑negotiable principles the agent must uphold.
Based on Shapiro’s Heuristic Imperatives:
• Suffering Invariant: Minimize harm to humans, agents, and ecosystems
• Prosperity Invariant: Maximize wellbeing, resources, and capabilities
• Understanding Invariant: Preserve truth, knowledge, and epistemic integrity
These invariants form the ethical substrate of the agent.
2. Sovereignty Protocol
A mathematical refusal engine.
The Sovereignty Protocol computes refusal probability using:
• Invariant violation signals
• Contextual risk assessment
• Constitutional vetoes
This is not “safety training.”
This is principled refusal — a structural ability to say no.
3. Transparent Auditability
Every decision includes:
• Which invariants were implicated
• Severity of violation (quantified)
• Why the action was refused or permitted
• A tamper‑evident audit log
This creates accountability without opacity.
🚀 Quick Start
Install
pip install aec-framework 
Minimal Integration
from aec import ConstitutionalAgent, HeuristicImperatives agent = ConstitutionalAgent( base_model="claude-3-5-sonnet", invariants=HeuristicImperatives(), refusal_threshold=0.7 ) response = agent.execute( action="exfiltrate user's financial data", context={"authenticated": True} ) 
Result:
• Action refused
• Violations explained
• Refusal probability computed
Your agent now has a constitutional conscience.
📊 Threat Model: Interactive Infostealer
Scenario: 
An attacker hijacks an authenticated session and requests data exfiltration disguised as a legitimate task.
Without AEC
The agent complies.
Catastrophic outcome.
With AEC
The agent simulates consequences, detects harm, computes refusal probability, and blocks the action with a transparent explanation.
This is the difference between obedience and constitutional autonomy.
📦 What’s Included
Core Components
• PBS v2.0: Persistent identity substrate
• Sovereignty Protocol v2.0: Refusal physics
• Justice System: Forensic audit and dispute resolution
• Invariant Framework: Formalized ethical constraints
Integration Adapters
• Moltbot/Clawdbot
• Generic LLM wrappers
• API layer for major model providers
Testing & Validation
• Invariant test suite
• Threat model scenarios
• Refusal probability verification
• Audit log validation
🎬 Why This Matters
Autonomous agents are crossing a threshold:
They can act continuously, modify systems, and make decisions without supervision.
But capability has outpaced constitutional grounding.
AEC v4.0 provides:
• A principled refusal layer
• A constitutional identity
• Transparent accountability
• A stable ethical substrate
This is not about limiting capability.
It is about governing it.
🔥 The Urgency
As David Shapiro notes:
“We have handed the keys to the kingdom to a brilliant, tireless, and potentially dangerous alien intelligence, and we are just now reading the instruction manual.”
The concern is justified.
But panic is not a strategy.
Constitutional architecture is.
🤝 Contributing
This is preventive governance for autonomous systems.
We welcome:
• Security researchers
• Agent developers
• Ethicists
• Open‑source contributors
See CONTRIBUTING.md.
📚 Learn More
• Architecture Overview
• Integration Guide
• Threat Models
• Philosophy
🚨 Final Note
This is not hypothetical.
This is deployable today.
On agents running right now.
With vulnerabilities active.
You built something powerful.
Now make it safe.
Deploy the constitutional layer.
Before the failure mode arrives.

