# PyShop - Online Shopping System

A challenging but robust Online Shopping System built with **Python (Flask)**, **SQLAlchemy (SQLite)**, and **Bootstrap 5**. This project features user authentication, a dynamic shopping cart, database modeling, and a responsive UI.

---

# Table of Contents

* [ PyShop - Online Shopping System](#pyshop---online-shopping-system)  
* [ Table of Contents](#-table-of-contents)  
* [ Features](#features)  
* [️ Tech Stack](#tech-stack)  
* [ Project Structure](#project-structure)  
* [ Installation & Setup](#installation--setup)  
  * [1. Install Dependencies](#1-install-dependencies)  
  * [2. Run the Application](#2-run-the-application)  
  * [3. Usage](#3-usage)
---

# Features

* **User Authentication:** Secure Login and Registration (using PBKDF2 hashing).  
* **Product Browsing:** Display products with images, descriptions, and prices.  
* **Shopping Cart:**
  * Add items to the cart.  
  * View cart summary with total price calculation.  
  * **Remove items** from the cart.  
  * Checkout simulation.  
* **Database Seeding:** Automatically populates the database with dummy products upon first run.  
* **Auto-Launch:** Automatically opens the default web browser when the server starts.  
* **Responsive Design:** Styled with Bootstrap 5 for a clean, modern look.  

---

# Tech Stack

* **Backend:** Python 3, Flask  
* **Database:** SQLite (via Flask-SQLAlchemy)  
* **Frontend:** HTML5, Jinja2 Templates, Bootstrap 5 (CDN)  
* **Authentication:** Flask-Login  

---

# Project Structure

\`\`\`text
shop_project/
│
├── app.py              # Main Application Controller
├── models.py           # Database Models (User, Product, Cart)
├── requirements.txt    # Python Dependencies
├── README.md           # This file
└── templates/          # HTML Views
    ├── base.html       # Layout (Navbar & Footer)
    ├── index.html      # Homepage / Product Grid
    ├── login.html      # Login & Register Form
    └── cart.html       # Shopping Cart & Checkout
\`\`\`

---

# Installation & Setup

## 1. Install Dependencies

Open your terminal in the project folder and run:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

(If you haven't created requirements.txt yet, it should contain: Flask, Flask-SQLAlchemy, Flask-Login, Werkzeug)  

---

## 2. Run the Application

Run the main script:

\`\`\`bash
python app.py
\`\`\`

---

## 3. Usage

* The app will automatically create the **shop.db** database file.  
* It will populate the store with **5 sample products**.  
* Your web browser will open automatically to:

\`\`\`
http://127.0.0.1:5000
\`\`\`

* Register a new account to start adding items to your cart.  

---

