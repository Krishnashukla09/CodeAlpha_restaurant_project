# 🍽️ Restaurant Management System

A mini full-stack application to manage restaurant menu items, orders, and customer details — built using Flask and MySQL with a clean Bootstrap interface.

---

## 🚀 Features

- 📝 Add, update, and delete food items
- 🧾 Create and manage customer orders
- 📊 View order history with total amount
- 🔍 Search and filter menu items
- 📁 Data stored persistently in MySQL

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Tools:** VS Code, Git, Postman

---


## 📂 Folder Structure

restaurant-management/
├── app.py
├── templates/
│ ├── index.html
│ ├── menu.html
│ └── orders.html
├── static/
│ └── styles.css (if any)
├── db_config.sql
└── README.md


---

## 💻 How to Run Locally

1. Clone the repository:

git clone https://github.com/Krishnashukla09/Restaurant-Management.git
cd Restaurant-Management

2. Install required Python packages:

pip install flask

3. Set up your MySQL database:

Import db_config.sql

4. Update database credentials in app.py

5. Run the app:

python app.py

6. Access in browser:

http://localhost:5000


🔮 Future Scope
👨‍🍳 Add admin authentication

🧾 Auto-generate bill PDFs

🧮 Inventory management module

☁️ Deploy to cloud using Render or Railway
