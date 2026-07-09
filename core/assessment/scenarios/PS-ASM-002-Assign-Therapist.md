---
id: PS-ASM-002
title: Assign Therapist
capability: Assessment
version: 0.81R
status: Business Review Draft
knowledge_confidence: 90%
---

# Assign Therapist

## Purpose
Assign a qualified therapist.

## Trigger
Assessment created.

## Preconditions
Qualified therapist available.

## Main Success Flow
1. Verify customer identity.
2. Prepare assessment record.
3. Execute assessment activity.
4. Record findings.
5. Save assessment outcome.

## Postconditions
Therapist assigned.

## Related Business Rules
- BR-ASM-001 Assessment record must be retained.
- BR-ASM-002 Recommendation is based on completed assessment.

## Evidence
- VRC workshop sessions
- BA consolidation
