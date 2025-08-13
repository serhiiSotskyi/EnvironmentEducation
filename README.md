# Environment Education Platform 🌱

A fully functional educational web platform built using Django as part of my first-year university project. It allows users to learn about environmental topics through content and interactive quizzes, while admins can manage everything from the backend. It includes user authentication, content submission, and quiz result tracking.

---

## ✨ Features

- 🔓 **User system**: Register, log in, and access personalised dashboard
- 📚 **Educational content**: Admins can post and edit articles and media
- 🧠 **Interactive quizzes**: Admins can create, edit, and remove quizzes
- 📊 **Progress tracking**: Users can view their quiz history and scores
- 🛠️ **Admin dashboard**: Full Django admin interface for content and quiz management
- 🧪 Built entirely from scratch using Django (no templates or generators)

---

## ⚙️ Tech Stack

- Django (Python)
- SQLite (default Django DB)
- HTML & CSS (vanilla)
- Bootstrap (light usage for styling)

---

## 🖥️ How to Run Locally

1. **Clone the repo**:
   ```bash
   git clone https://github.com/serhiiSotskyi/EnvironmentEducation.git
   cd EnvironmentEducation
   ```

2. **Apply migrations and create a superuser**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

4. **Access the site**:
   - [http://127.0.0.1:8000/](http://127.0.0.1:8000/) – Main website
   - [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) – Admin panel

---

## 📸 Notes

- Quizzes, user progress tracking, and custom content management were implemented entirely from scratch during my first year at university.

---

## 🔮 Future Plans

- Deploy the site publicly (e.g. Render, Railway, or Heroku)
- Add AI-powered content suggestions or quiz generation
- Include downloadable progress reports and badges for users

---

## 📄 License

MIT – free to use, fork, or extend.

---
