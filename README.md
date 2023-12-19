# Django Library Management System

This is a Library Management System built with Django. It allows users to add authors and books, and manage a library inventory. The system provides an easy-to-use interface for managing the library's resources.
## Setup

1. Clone the repository:
    ```
    git clone https://github.com/CalebCheptumo/Library-Management-System.git
    cd Library-Management-System
    ```

2. Set up your MySQL database and update the `DATABASES` setting in `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE' : 'django.db.backends.mysql',
            'NAME' : '<your-database-name>',
            'USER' : '<your-username>',
            'PASSWORD' : '<your-password>',
            'HOST' : '<your-host>',
            'PORT' : '<your-port>',
            'OPTIONS' : {
                'init_command' : "SET sql_mode = 'STRICT_TRANS_TABLES'"
            }
        }
    }
    ```

3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

4. Make the migrations:
    ```
    python manage.py makemigrations
    ```

5. Apply the migrations:
    ```
    python manage.py migrate
    ```

6. Create a superuser:
    ```
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username, email, and password for the superuser.

7. Run the server:
    ```
    python manage.py runserver
    ```

## Usage

1. Navigate to `http://127.0.0.1:8000/` in your browser to access the main library management system.
2. Log in at `http://127.0.0.1:8000/accounts/login/` with your superuser credentials.
3. Visit `http://127.0.0.1:8000/book_inventory/` to view the book inventory.
4. Add a new book at `http://127.0.0.1:8000/book_inventory/book_form/`.
5. Add a new author at `http://127.0.0.1:8000/book_inventory/author_form/`.

## Contributing

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.