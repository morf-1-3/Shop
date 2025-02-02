# 🛒 Electronics Store (Django)

An online electronics store built with Django, featuring product filtering, order placement, and user authentication. The store integrates **Nova Poshta API** for delivery selection and **WayForPay API** for online payments.

🔗 **Live Demo:** [morf.pythonanywhere.com](https://morf.pythonanywhere.com/)

---

## 🚀 Features
- 🔍 **Product Filtering** – Easily search and filter products.
- 🛒 **Shopping Cart** – Add products to the cart and place orders.
- 🔑 **User Authentication** – Register, log in, and manage orders.
- 🚚 **Nova Poshta API** – Select a delivery branch for shipping.
- 💳 **WayForPay Integration** – Secure online payments.

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository
```sh
git clone https://github.com/morf-1-3/Shop

```

### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Apply database migrations
```sh
python manage.py migrate
```

### 4️⃣ Run the server
```sh
python manage.py runserver
```

Or visit the **live version** at: [morf.pythonanywhere.com](https://morf.pythonanywhere.com/)

---

## 📂 Project Structure
```
📦 electronics-store
├── 📂 catalog        # Product catalog & filtering
├── 📂 cart           # Shopping cart functionality
├── 📂 orders         # Order processing, Nova Poshta & WayForPay API integrations
│   ├── 📂 services   # External API integrations
├── 📂 users          # User authentication & profiles
├── 📂 shopinfo       # Store management (admin tools, settings)
├── manage.py        # Django project management
└── requirements.txt  # Dependencies
```

---

## 📌 Tech Stack
- **Backend:** Django, Django ORM
- **Database:** SQLite / PostgreSQL
- **APIs:** Nova Poshta, WayForPay
- **Hosting:** PythonAnywhere

---

## 🎯 Future Improvements
✅ Implement a REST API for third-party integrations.  
✅ Add user reviews & ratings for products.  
✅ Improve UI with modern frontend framework (React or Vue).

---

## 📩 Contact
🔗 GitHub: [morf-1-3](https://github.com/morf-1-3))  
📧 Email: foliakhov.developer@gmail.com


