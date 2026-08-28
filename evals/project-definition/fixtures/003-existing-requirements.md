# Appointment Scheduling Requirements

## Goal

Provide a simple appointment-scheduling service that lets customers book appointments with participating service providers and lets provider staff manage those appointments.

## Target Users

- Customers who want to book and manage appointments.
- Provider staff who manage the provider's appointment calendar.

## Functional Requirements

### FR-001 — Browse availability

Customers can view available appointment time slots for a selected provider.

### FR-002 — Create booking

Customers can book an available appointment time slot.

### FR-003 — Booking confirmation

Customers receive a confirmation message after a booking is successfully created.

### FR-004 — Confirmation notification

The service sends the customer a booking confirmation when an appointment is created successfully.

### FR-005 — Customer cancellation

Customers can cancel a booked appointment up to 24 hours before the appointment start time.

### FR-006 — Late cancellation

Customers can cancel a booked appointment until 2 hours before the appointment start time.

### FR-007 — Staff calendar management

Provider staff can view, create, reschedule, and cancel appointments for their provider.

## Business Rules

### BR-001 — Available-slot booking

A customer may book only a time slot currently shown as available.

## Constraints

- The initial service must support both customer-created and staff-created bookings.

## Open Questions

- None currently recorded.
