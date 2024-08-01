# Flask File Sharing App

## Overview

This is a Flask application for secure file sharing with user authentication. Users can register, log in, upload files, and view or download their files. The app uses SQLAlchemy for database management and Flask-Login for user session management.

## Features

- **User Registration**: Users can create a new account with a username and email.
- **User Login/Logout**: Users can log in and out of their accounts.
- **File Upload**: Authenticated users can upload files to their account.
- **File Management**: Users can view a list of their uploaded files and download them.

## Technologies

- **Flask**: Web framework for Python
- **Flask-SQLAlchemy**: SQLAlchemy integration for Flask
- **Flask-Login**: User session management
- **SQLite**: Lightweight database
- **Werkzeug**: Security utilities

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repo-name
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Initialize the database:**

    ```bash
    python
    ```

    ```python
    from app import db
    db.create_all()
    ```

7. **Run the Flask app:**

    ```bash
    python app.py
    ```

    The app will start on `http://127.0.0.1:5000/`.

## Configuration

- **SECRET_KEY**: Set a secret key in `app/config.py` for session management.
- **SQLALCHEMY_DATABASE_URI**: Configure the database URI in `app/config.py`.

## Usage

- **Home Page**: Navigate to `/` or `/home` to view the home page.
- **Register**: Go to `/register` to create a new account.
- **Login**: Go to `/login` to log in to an existing account.
- **Upload Files**: Go to `/upload` to upload files.
- **View Files**: Go to `/files` to see and download your files.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Ganidu Hapuarachchi
