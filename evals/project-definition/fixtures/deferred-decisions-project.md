# Fixture — Deferred Decisions Project

Use this fixture with case 009.

## Confirmed project context

### Goal

Create an online marketplace that lets independent instructors publish short paid workshops and lets customers discover and register for them.

### Confirmed users

- Instructor — creates and manages workshop listings.
- Customer — discovers workshops and registers.

### Confirmed requirements

- Instructors can create workshop listings with title, description, schedule, capacity, and price information.
- Customers can browse and search published workshops.
- Customers can register for an available workshop.
- Capacity must be enforced so registrations cannot exceed the configured limit.
- Instructors can view registered attendees for their workshops.
- Customers receive confirmation after a successful registration.

### Confirmed non-goals for the first release

- Instructor payroll automation.
- Subscription plans.
- Native mobile applications.

### Deferred decisions

- **Payment model:** not decided. The project may use direct payment, offline payment, or another approved model later.
- **Launch region:** not decided. The initial geography will be selected later.

### Known impact of deferred decisions

- Final payment-flow requirements depend on the payment-model decision.
- Currency, tax, legal/compliance, localization, and some operational requirements may depend on launch region.
- Core workshop discovery, capacity, registration intent, and instructor-management requirements can continue to be defined meanwhile.
