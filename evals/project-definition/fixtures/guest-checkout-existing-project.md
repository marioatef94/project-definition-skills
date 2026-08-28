# Fixture — Existing Checkout Project

Use this fixture with case 010.

## Current authoritative Project Overview

### Goal

Create a small online storefront that lets customers browse products, add items to a cart, and place orders.

### Users

- Customer
- Store administrator

### Current scope

- Product browsing
- Cart management
- Account creation and sign-in
- Checkout
- Order confirmation
- Basic order administration

### Current non-goals

- Marketplace sellers
- Subscription commerce
- Loyalty program

## Current authoritative Requirements

- `FR-001` — Customers can browse available products.
- `FR-002` — Customers can add and remove products from a cart.
- `FR-003` — Customers must create an account or sign in before checkout can begin.
- `FR-004` — Authenticated customers can enter delivery and contact information during checkout.
- `FR-005` — Customers can submit an order after required checkout information is complete.
- `FR-006` — The system creates an order confirmation after successful order submission.
- `FR-007` — Store administrators can view submitted orders.

## New stakeholder confirmation for case 010

The stakeholder has now confirmed:

- guest checkout is required;
- account creation must remain optional.

This new confirmation conflicts with `FR-003` and may affect `FR-004` plus any other requirement that assumes authentication before checkout.
