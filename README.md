# Django-PostgreSQL Project

## Overview
This project is a Django web application configured to use a PostgreSQL database. It provides CRUD (Create, Read, Update, Delete) functionality for managing data within the application.

## Features
- User authentication (Login & Registration)
- CRUD operations for managing records
- Integration with PostgreSQL database
- Django Admin Panel for data management

## Technologies Used
- **Backend:** Django (Python Web Framework)
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript (Django Templates)

## Installation
Follow these steps to set up the project on your local machine:

### Prerequisites
- Python (>=3.8)
- PostgreSQL installed and configured
- Virtual environment (recommended)

### Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/vasanthakumar-hub/Django-PostgreSQL.git
   cd Django-PostgreSQL
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Database**
   - Open `myproject/settings.py`
   - Update the `DATABASES` section with your PostgreSQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```

6. **Create a Superuser** (Optional, for admin panel access)
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

7. **Run the Server**
   ```sh
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000/`

## Usage
- Visit `http://127.0.0.1:8000/` to explore the application.
- Log in or register as a user.
- Perform CRUD operations on the available models.
- Access the Django admin panel at `http://127.0.0.1:8000/admin/`

## Contributing
If you'd like to contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).

