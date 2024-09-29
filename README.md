# Madni Inter College

Welcome to the Madni Inter College website project! This Django application provides a complete backend support system for managing various aspects of the college's online presence. From managing content to handling admissions, this app is designed to streamline the college's operations.

## Features

- Complete backend support for managing website content
- Ability to add and update sections such as:
  - About section
  - Image gallery
  - Faculty section
  - Director's message
  - FAQs
  - Student's corner
  - Initiatives
  - Challenges
- Admission form for prospective students
- Career section to explore career opportunities at the college
- Notice board to display important announcements
- Holiday calendar to keep track of college holidays

## Requirements

To run this project, you need to have the following packages installed:

- Django==5.0.7
- django-jazzmin (for enhanced admin interface)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Prakhar2706/Madni_Int_College.git
   cd Madni_Int_College

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

   ```bash
   pip install Django==5.0.7
   pip install -U django-jazzmin

4. Create migrations for your models:

   ```bash
   python manage.py makemigrations

5. Apply migrations:

   ```bash
   python manage.py migrate

6. Create a superuser (optional, for admin access):

   ```bash
   python manage.py createsuperuser

7. Run the development server:

   ```bash
   python manage.py runserver

8. Open your web browser and go to http://127.0.0.1:8000/ to access the Madni Inter College website.

9. For admin access:

   ```bash
   http://127.0.0.1:8000/admin

## Usage

- Log in to the admin panel to manage the website content.
- Add or update information in the various sections of the website.
- Use the admission form to collect applications from prospective students.
- Check the career section for available opportunities.
- Post notices and maintain the holiday calendar.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
