# Using TablePlus with FastAPI Blog Application

This guide explains how to use TablePlus to manage and view your blog application's database.

## Prerequisites

1. Install TablePlus from [https://tableplus.com/](https://tableplus.com/)
2. Make sure your FastAPI application is running
3. Have your database file ready (blog.db)

## Connecting to SQLite Database

1. Open TablePlus
2. Click "Create a new connection"
3. Select "SQLite" from the connection types
4. Configure the connection:
   - Name: Blog App
   - File: Select your `blog.db` file from the project directory
   - Click "Connect"

## Database Structure

Your database contains two main tables:

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    email VARCHAR,
    password VARCHAR
);
```

### Blogs Table
```sql
CREATE TABLE blogs (
    id INTEGER PRIMARY KEY,
    title VARCHAR,
    body VARCHAR,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## Common Queries

### View All Users
```sql
SELECT id, name, email FROM users;
```

### View All Blogs with User Names
```sql
SELECT b.id, b.title, b.body, u.name as author
FROM blogs b
JOIN users u ON b.user_id = u.id;
```

### View Blogs by User
```sql
SELECT b.*, u.name as author
FROM blogs b
JOIN users u ON b.user_id = u.id
WHERE u.id = 1;
```

## Testing the Database

1. First, run the test script:
```bash
python test_tableplus.py
```

2. In TablePlus, you can verify the data:
   - Check the users table for the test user
   - Check the blogs table for the test blog post

## Security Notes

1. Never modify the password field directly in the database
2. Always use the API endpoints for user management
3. The password field contains hashed values, not plain text

## Troubleshooting

1. If you can't connect to the database:
   - Make sure the application is not running
   - Check if the database file exists
   - Verify file permissions

2. If you see no data:
   - Run the test script first
   - Check if the application is running
   - Verify the database path

## Best Practices

1. Always backup your database before making changes
2. Use the API endpoints for data modification
3. Use TablePlus mainly for viewing and debugging
4. Keep your database file in version control (if using SQLite) 