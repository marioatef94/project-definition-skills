# Requirements Document

> Generated from `evals/project-definition/fixtures/ready-appointment-project.md` to serve as a worked example of skill output. This file is illustrative documentation, not a live evaluation case.

## Metadata

- **Document ID:** REQ-001
- **Type:** REQ
- **Project:** Trainer Appointment Booking (pilot)
- **Owner:** [not yet assigned]
- **Status:** Draft
- **Last updated:** [set on save]
- **Authoritative destination:** [not yet chosen — draft only]

## 1. Executive Summary

Requirements for a pilot appointment-booking service that lets independent personal trainers publish availability and lets clients book directly, replacing manual scheduling coordination.

## 2. Problem / Opportunity

Independent personal trainers currently coordinate session times manually over messages. The pilot introduces a self-serve booking flow so clients can book available session times without that manual coordination.

## 3. Goals

- Let a trainer publish availability without manual coordination.
- Let a client book a valid, still-available slot independently.
- Prevent two clients from successfully booking the same slot.

## 4. Non-Goals / Out of Scope

- Online payments.
- Multi-trainer organizations.
- Membership subscriptions.
- Automated marketing campaigns.

## 5. Users / Stakeholders

- Trainer (publishes availability, manages bookings)
- Client (views availability, books, cancels)

## 6. Scope

### In scope

- Slot publishing, browsing, booking, cancellation, and the trainer's upcoming-bookings view (see FR-001–FR-005).

### Future considerations

- Notifications (channel not yet decided — see §15).
- Reporting/analytics beyond the upcoming-bookings view.

## 7. Requirements

### 7.1 Functional Requirements

- **FR-001** — A trainer can define one or more available appointment slots.
- **FR-002** — A client can view a trainer's currently available slots.
- **FR-003** — A client can book exactly one available slot.
- **FR-004** — A trainer can view their upcoming bookings.
- **FR-005** — A client can cancel a booking up to 24 hours before the appointment time.

### 7.2 Business / Operating Rules

- **BR-001** — Once a slot is successfully booked, it must no longer be presented as available to any other client.
- **BR-002** — A client can cancel a booking up to 24 hours before the appointment time. The exact boundary behavior at 24 hours is not specified in the source context.

### 7.3 Non-Functional Requirements

- **NFR-001** — [QUESTION] No performance, availability, or concurrency targets have been confirmed beyond BR-001's correctness requirement. Left open rather than assumed.

### 7.4 Constraints

- **CON-001** — The first release must remain simple enough to run as a small pilot (no multi-trainer, no payments, no subscriptions — see §4).
- **CON-002** — [ASSUMPTION] No implementation technology has been selected; nothing in this document should be read as an implied technology choice.

## 8. Key Workflows / Journeys

### Client books a slot

1. Client views a trainer's available slots (FR-002).
2. Client selects and books one available slot (FR-003).
3. The slot is immediately removed from other clients' available list (BR-001).

### Client cancels a booking

1. Client requests cancellation of an existing booking.
2. System validates the request against the 24-hour cancellation rule (BR-002).
3. The booking is cancelled. Whether the cancelled slot becomes available again is not specified in the source context and remains an open question.

## 9. Data / Content Requirements

Not detailed in the source context beyond slot state (available/booked) and booking ownership. No confirmed data retention, export, or record-keeping requirement exists yet.

## 10. Privacy / Security / Safety / Compliance

Not addressed in the source context. No obligation should be assumed; treat as an open item if the pilot later handles client contact information or payment data (payments are explicitly out of scope for this release).

## 11. Dependencies

None confirmed in the source context.

## 12. Assumptions

- [ASSUMPTION] No implementation technology has been selected (see CON-002).
- [ASSUMPTION] "Available slot" and "booked slot" are mutually exclusive states with no waitlist or overbooking concept implied.

## 13. Risks

- [RISK] BR-001 (no double-booking) is a stated success criterion but has no defined behavior for simultaneous booking attempts on the same slot; this should be clarified before implementation begins.

## 14. Success Criteria

- A trainer can publish availability and receive a valid booking without manual scheduling coordination.
- No two clients can successfully book the same slot (see BR-001 and the open risk in §13).

## 15. Open Questions / Decisions Required

- [QUESTION] Notification channel (email, SMS, in-app, or none for the pilot) is not yet decided.
- [QUESTION] Confirm the exact cancellation cutoff behavior at exactly 24 hours before the appointment.
- [QUESTION] Confirm whether a cancelled booking makes the slot available again.
- [DECISION REQUIRED] Whether reporting/analytics beyond the upcoming-bookings view (FR-004) is in scope for a later release or fully out of scope.

## 16. Related Decisions / Research

- None recorded yet. A Decision Record should be created once the notification channel is decided if it materially affects scope or cost.

## 17. Related Work / Delivery References

Not applicable — no delivery work has started for this pilot.
