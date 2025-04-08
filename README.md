# Quora-Inspired Q&A Web App (Django)

This is a simple web application inspired by Quora, built using Django and Django Forms.  
It allows users to register, log in, post questions, view and answer others' questions, like answers, and log out.

---

## Features

- User Registration (Signup)
- User Authentication (Login/Logout)
- Post new questions
- View a paginated list of all questions
- View question details along with answers
- Submit answers to questions
- Like answers posted by others
- Pagination for questions list
- Basic styling for a clean UI

---

## Tech Stack

- **Backend:** Django 4.x
- **Frontend:** Django Templates (HTML/CSS with basic styling)
- **Database:** SQLite (default Django database)

---

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/quora-clone-django.git
   cd quora-clone-django
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access the app**

   Visit `http://127.0.0.1:8000/` in your browser.

---

## Usage

- **Signup** for a new account.
- **Login** with your credentials.
- On the **home page**, view all questions.
- **Post** a new question.
- **Click** on any question to view its details and answers.
- **Submit** your answer.
- **Like** answers you find helpful.
- **Logout** anytime from the navigation bar.

---

## Project Structure

```bash
quora_clone/
├── manage.py
├── quora_clone/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── core/                 # Main app
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── signup.html
│   │       ├── question_detail.html
│   │       └── ...
│   ├── static/
│   │   └── core/
│   │       └── styles.css
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
└── requirements.txt
```

---

## Notes

- Django's built-in authentication system is used (no JWT or API authentication needed).
- Basic session-based authentication is handled securely by Django.
- CSRF protection is enabled by default.

---
