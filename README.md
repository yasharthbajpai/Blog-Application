# Blog Application

A modern, secure blog application built with FastAPI, featuring JWT authentication and SQLAlchemy ORM.

## Features

- 🔐 JWT Authentication
- 👥 User Management
- 📝 Blog Post Management
- 🔒 Secure Password Hashing
- 🗄️ SQLite Database (can be configured for other databases)
- 📚 API Documentation with Swagger UI

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication
- Python-Jose
- Passlib (bcrypt)
- Uvicorn

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blog.git
cd blog
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///./blog.db
```

## Running the Application

1. Start the development server:
```bash
uvicorn main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token
- `POST /auth/logout` - Logout (client-side token removal)

### Users
- `GET /user/{id}` - Get a specific user
- `GET /user/` - Get all users
- `DELETE /user/{id}` - Delete a user

### Blogs
- `POST /blog/` - Create a new blog
- `GET /blog/{id}` - Get a specific blog
- `GET /blog/` - Get all blogs
- `PUT /blog/{id}` - Update a blog (only by owner)
- `DELETE /blog/{id}` - Delete a blog (only by owner)

## Security Features

- JWT token-based authentication
- Password hashing with bcrypt
- Protected routes
- User-specific blog operations
- Input validation with Pydantic

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the Creative Commons Zero v1.0 Universal License - see the [LICENSE](LICENSE) file for details.

## Author

Created by Yasharth Bajpai

## Acknowledgments

- FastAPI documentation
- SQLAlchemy documentation
- JWT.io for token information 