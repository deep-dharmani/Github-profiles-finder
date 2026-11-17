 # 🔍 GitHub Profile Finder API

A backend application built with **Python and FastAPI** that allows users to search for GitHub profiles using a username and retrieve profile information through API requests.

This project demonstrates REST API development, request handling, data validation, and integration with GitHub.
link:http://127.0.0.1:8000/docs
## ✨ Features

- 🔎 **GitHub User Search:** Search for GitHub users using their usernames.
- ⚡ **FastAPI Backend:** Built using FastAPI for API development.
- 🌐 **GitHub API Integration:** Retrieve public GitHub profile information.
- 📦 **JSON Responses:** Return structured data in JSON format.
- 🛡️ **Data Validation:** Use Pydantic for request validation.
- ⚠️ **Error Handling:** Handle invalid usernames and unsuccessful requests.
- 📚 **Interactive API Documentation:** Explore API endpoints using Swagger UI.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| Pydantic | Data validation |
| Uvicorn | ASGI server |
| GitHub REST API | GitHub profile data |

## 📂 Project Structure

```text
Github-profiles-finder/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/deep-dharmani/Github-profiles-finder.git
```

### 2. Navigate to the Project

```bash
cd Github-profiles-finder
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

## 📖 API Documentation

After starting the server, open:

**Swagger UI:**
```text
http://127.0.0.1:8000/docs
```

**ReDoc:**
```text
http://127.0.0.1:8000/redoc
```

You can explore and test available API endpoints through the interactive documentation.

## 🔄 How It Works

1. The user provides a GitHub username.
2. FastAPI receives the API request.
3. The application processes the username.
4. GitHub API is used to retrieve public profile information.
5. The application returns the response in JSON format.

## 🎯 Project Goals

This project is part of my Python backend development journey.

Through this project, I am practicing:

- Building REST APIs with FastAPI.
- Understanding HTTP methods.
- Working with Pydantic models.
- Handling API requests and responses.
- Integrating external APIs.
- Managing virtual environments.
- Handling errors in backend applications.

## 👨‍💻 Developer

**Deep Dharmani**

GitHub: [@deep-dharmani](https://github.com/deep-dharmani)

---

⭐ If you find this project interesting, consider giving it a star!

**Built with Python & FastAPI 🐍**
