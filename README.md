# fitness-studio

# 🧘‍♀️ Fitness Studio Booking API

A simple RESTful API built with **Django** and **Django REST Framework** that allows clients to view available fitness classes (like Yoga, Zumba, HIIT), book a spot, and view their bookings.

## 🚀 Features

- 📆 View all upcoming fitness classes
- ✅ Book a class (if slots are available)
- 📩 Retrieve bookings by client email
- 🕓 Handles timezone conversion (Classes created in IST)
- 🧪 Basic input validation and error handling

---

## 📦 Technology Stack

- Python 3.13
- Django 5.0.10
- Django REST Framework
- SQLite (in-memory or local)

---

## 🧱 Endpoints

### `GET /classes/`

Returns a list of all upcoming fitness classes.

**Response Example:**

```json
[
  {
    "id": 1,
    "name": "Yoga",
    "datetime": "2025-06-06T08:00:00Z",
    "instructor": "Alice",
    "available_slots": 5
  }
]
