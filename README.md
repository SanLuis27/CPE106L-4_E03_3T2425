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
├── main.py           # Entry point for launching the full application
├── users.txt         # Sample user data
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## 🚀 Getting Started

1. Clone the Repository
```bash
git clone https://github.com/your-username/RePlate.git](https://github.com/SanLuis27/CPE106L-4_E03_3T2425.git
cd RePlate
```

2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

3. Run the App
```bash
python main.py
```

---

## 🧪 Sample Credentials

| Username     | Password     | Role       |
|--------------|--------------|------------|
| donor1       | password123  | Donor      |
| recipient1   | securepass   | Recipient  |

---

## 📊 Features

- 🔐 Secure login for donors and recipients

- 📝 Donors can add/view food donations

- 📦 Recipients can request food and track deliveries

- 🗺️ Map integration for delivery tracking

- 💬 Chat system for real-time updates

- 📈 Reports showing food saved and delivery progress

---

## 👨‍🏫 Client
This project is developed for Sir. Dionis Padilla as part of the CPE106L-4-E03 course at Mapúa University.

---

## 👥 Contributors
- Derrick C. Lee
- Juan Miguel S. San Luis

---

## 📃 License
This project is for academic purposes under Mapúa University's guidelines.
