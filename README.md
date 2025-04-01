# FastAPI Blog Application

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

1. Copy the `.env.example` to `.env` and update the values:
   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your secret key and database configuration.

## Running the Application

1. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the API documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Project Structure

```
blog-api/
│
├── main.py                  # Entry point of the application
│
├── routers/                 # API route handlers organized by resource
│   ├── __init__.py          # Makes the directory a Python package
│   ├── blog.py              # Blog-related endpoints
│   ├── user.py              # User management endpoints
│   └── login.py             # Authentication endpoints (register, login, logout)
│
├── models.py                # SQLAlchemy ORM models (User, Blog)
│
├── schemas.py               # Pydantic models for request/response validation
│
├── database.py              # Database connection and session management
│
├── requirements.txt         # Project dependencies
│
├── .env.example             # Example environment variables template
│
├── .env                     # Environment variables (not versioned)
│
├── .gitignore               # Git ignore file
│
├── LICENSE                  # Project license (CC0 v1.0)
│
├── README.md                # Project documentation
│
├── TABLEPLUS_GUIDE.md       # Guide for database management with TablePlus
│
└── test_tableplus.py        # Test script for API functionality
```

### Component Details

#### Core Components

- **main.py**: Application entry point. Initializes FastAPI, includes routers, and sets up middleware.

- **models.py**: Defines SQLAlchemy ORM models:
  - `User`: Represents application users with authentication details
  - `Blog`: Represents blog posts linked to users

- **schemas.py**: Defines Pydantic models for:
  - Request validation (ensuring correct data format for API inputs)
  - Response serialization (standardizing API outputs)
  - Data transformation between API and database layers

- **database.py**: Sets up SQLAlchemy engine, session management, and database connection.

#### Routers (API Endpoints)

- **routers/blog.py**: CRUD operations for blog posts:
  - Create: `POST /blog/`
  - Read: `GET /blog/` and `GET /blog/{id}`
  - Update: `PUT /blog/{id}`
  - Delete: `DELETE /blog/{id}`

- **routers/user.py**: User management endpoints:
  - Read: `GET /user/` and `GET /user/{id}`
  - Delete: `DELETE /user/{id}`

- **routers/login.py**: Authentication endpoints:
  - Register: `POST /auth/register`
  - Login: `POST /auth/login`
  - Logout: `POST /auth/logout`

#### Configuration and Documentation

- **.env.example**: Template showing required environment variables
- **.env**: Actual environment variables with sensitive configuration
- **README.md**: Project documentation (this file)
- **TABLEPLUS_GUIDE.md**: Instructions for database management

#### Testing and Development

- **test_tableplus.py**: Test script for API functionality:
  - User registration and authentication
  - Blog post creation and retrieval

## API Flow Diagram

```
┌────────────┐      ┌────────────┐      ┌────────────┐
│   Client   │◄────►│  FastAPI   │◄────►│ SQLAlchemy │◄────►┌─────────┐
│  (Browser/ │      │  (Routers) │      │    ORM     │      │ SQLite  │
│  App/etc.) │      │            │      │            │      │ Database│
└────────────┘      └────────────┘      └────────────┘      └─────────┘
       ▲                   ▲
       │                   │
       │                   │
       │            ┌────────────┐
       └────────────┤    JWT     │
                    │  Security  │
                    └────────────┘
```

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
