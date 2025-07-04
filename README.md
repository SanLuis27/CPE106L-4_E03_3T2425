# 🥫 RePlate: Connecting Surplus to Need

RePlate is a food rescue and redistribution platform designed to reduce food waste and fight hunger. It connects donors (restaurants, stores, individuals) with recipients (shelters, food banks) through a user-friendly system that tracks donations, plans deliveries, and promotes sustainability.

---

## 📌 Project Overview

Every year, tons of edible food are wasted while many go hungry. RePlate aims to solve this by:

- Making it easy for donors to list surplus food
- Allowing recipients to request and track food deliveries
- Using smart routing to optimize pickups and drop-offs
- Providing insights through charts and reports

---

## 🧱 System Architecture

RePlate follows a **three-tier architecture**:

| Layer              | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| UI Layer           | Handles user interaction (e.g., login, menus)                              |
| Business Logic     | Processes user input and system rules (e.g., authentication)               |
| Data Access Layer  | Manages data storage and retrieval (e.g., user credentials, donations)     |

---

## 📂 File Structure

```bash
RePlate/
├── login_ui.py       # User interface for login
├── login_bl.py       # Business logic for authentication
├── login_dal.py      # Data access for user credentials
├── users.txt         # Sample user data
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation

---
