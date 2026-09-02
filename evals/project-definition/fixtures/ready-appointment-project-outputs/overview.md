# Project / Product Overview

> Generated from `evals/project-definition/fixtures/ready-appointment-project.md` to serve as a worked example of skill output. This file is illustrative documentation, not a live evaluation case.

## Metadata

- **Document ID:** OVR-001
- **Type:** OVR
- **Project:** Trainer Appointment Booking (pilot)
- **Owner:** [not yet assigned]
- **Status:** Draft
- **Last updated:** [set on save]
- **Authoritative destination:** [not yet chosen — draft only]

## Summary

A simple appointment-booking service that lets independent personal trainers publish available session times so clients can book directly, without coordinating manually over messages.

## Problem / Opportunity

Independent personal trainers currently coordinate session times manually over messages. A lightweight self-serve booking flow is intended to replace that manual coordination for a small pilot group.

## Intended Outcomes

- Trainers publish availability without manual back-and-forth.
- Clients book a valid, still-available slot on their own.
- No two clients can successfully book the same slot.

## Users / Beneficiaries

- **Trainer** — publishes available appointment slots and manages bookings.
- **Client** — views availability and books a slot.

## Scope

### In scope

- Trainers define available appointment slots.
- Clients view available slots for a trainer.
- Clients book one available slot.
- Trainers view upcoming bookings.
- A booked slot no longer appears as available to another client.
- Clients cancel a booking up to 24 hours before the appointment.

### Out of scope

- Online payments.
- Multi-trainer organizations.
- Membership subscriptions.
- Automated marketing campaigns.

## Major Capabilities / Work Areas

- Slot publishing (trainer)
- Slot browsing and booking (client)
- Booking cancellation (client)
- Upcoming-bookings view (trainer)

## Key Constraints

- The first release should remain simple enough for a small pilot group.
- No specific implementation technology has been selected. — [ASSUMPTION] treat as open until a decision record exists.

## Important Decisions

- [DECISION REQUIRED] Notification channel (e.g., email, SMS, none for pilot) — not yet decided.

## Major Risks / Unknowns

- [QUESTION] Reporting/analytics beyond the upcoming-bookings view is not yet decided; out of scope for this release unless resolved.
- [QUESTION] The source does not state whether a cancelled booking makes that slot available again.
- [RISK] Double-booking prevention is a stated success criterion, but simultaneous booking-attempt behavior is not yet defined — see REQ-001 §13 and §14.

## Related Documentation

- **Requirements:** REQ-001 (`requirements.md` in this same folder)
- **Research:** not applicable for this pilot
- **Decisions:** none recorded yet — notification channel decision is open
- **Architecture:** not currently required; no technical constraint or complexity has been identified that justifies an Architecture Overview

## Next Definition Actions

- Decide notification channel and record as a Decision Record if it materially affects scope.
- Confirm whether analytics/reporting is truly out of scope for the pilot or deferred only.
