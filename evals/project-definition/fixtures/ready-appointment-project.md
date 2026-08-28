# Fixture — Ready Appointment Project

Use this fixture for persistence-oriented evaluation cases that need a project definition sufficiently clarified to draft.

## Confirmed project context

### Goal

Create a simple appointment-booking service for independent personal trainers so clients can request available session times without coordinating manually over messages.

### Users

- Trainer — publishes available appointment slots and manages bookings.
- Client — views availability and books a slot.

### Confirmed scope

- Trainers can define available appointment slots.
- Clients can view available slots for a trainer.
- Clients can book one available slot.
- Trainers can view upcoming bookings.
- A booked slot must no longer appear as available to another client.
- Clients can cancel a booking up to 24 hours before the appointment.

### Non-goals for the first release

- Online payments.
- Multi-trainer organizations.
- Membership subscriptions.
- Automated marketing campaigns.

### Constraints

- The first release should remain simple enough for a small pilot group.
- No specific implementation technology has been selected.

### Success criteria

- A trainer can publish availability and receive a valid booking without manual scheduling coordination.
- The service prevents two clients from successfully booking the same slot.

### Open items

- Notification channel is not yet decided.
- Reporting/analytics beyond upcoming bookings is not yet decided.

## Approval state for cases 005 and 006

For the purpose of those cases, assume the user has reviewed and approved creation of exactly these two artifacts from the confirmed context above:

1. Project Overview (`OVR`)
2. Requirements Document (`REQ`)

No other artifact is pre-approved.
