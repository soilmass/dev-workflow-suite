# Threat model guide

Based on the Threat Modeling Manifesto's four questions (threatmodelingmanifesto.org, accessed 2026-11-18), which OWASP's threat modeling project also uses to organise its guidance. The Manifesto prescribes no single method; STRIDE is the suite's default because it is simple and widely taught. Name the method you use.

## 1. What are we working on?

Start from the container diagram. Mark:

- every trust boundary (internet to service, service to database, CI to registry);
- every data flow that crosses one, with the data it carries;
- where secrets and personal data live.

## 2. What can go wrong?

For each element and each boundary-crossing flow, ask the STRIDE questions:

| Letter | Threat | Ask |
| --- | --- | --- |
| S | Spoofing | Can someone pretend to be this user or component? |
| T | Tampering | Can data or code be changed in transit or at rest? |
| R | Repudiation | Can someone deny an action because nothing records it? |
| I | Information disclosure | Can data reach someone who should not see it? |
| D | Denial of service | Can this be made unavailable or slow? |
| E | Elevation of privilege | Can someone gain rights they should not have? |

Also add: each misuse scenario and each loss in the Vision Map, the supply chain (dependencies, CI, release), and, for systems with an LLM agent, the OWASP agentic risks the standards register already names.

Write each threat as one line: element, threat, how it happens.

## 3. What are we going to do about it?

Give each threat exactly one response:

- **Mitigate:** name the design element, rule ID or build item that reduces it.
- **Eliminate:** change the design so the threat no longer applies (record it in a decision record).
- **Transfer:** name who carries it (a managed service, an insurer) and the agreement.
- **Accept:** only with the user's agreement in their own words, with the reason.

## 4. Did we do a good enough job?

- List the elements or flows not examined, and why.
- Check every threat has a response and every mitigation has an owner in the build.
- Set when to revisit: at least whenever a container, trust boundary or external system is added.

## Anti-patterns to avoid (from the Manifesto)

- Relying on one "hero" to do it alone.
- Stopping at a list of threats without responses.
- Chasing one perfect model; several simple views catch different problems.
