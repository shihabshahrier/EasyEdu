# EasyEdu - University Management Platform

EasyEdu is an online platform designed to simplify university management, providing features for course advising, payment systems, and various tools for both teachers and students. With EasyEdu, teachers can upload course materials, quizzes, and manage evaluations, while students can access their gradesheets, evaluate courses, and perform self-advising. This project is built using Python Django and utilizes libraries like pandas, pillow, and the Stripe API.

## Key Features

- **Teacher Features:**
  - Upload course materials.
  - Create and manage quizzes.
  - Manage course evaluations.
  - Upload grades
  - Approve advising 


- **Student Features:**
  - Perform self-advising.
  - Take quiz and view course materials
  - Pay Semester Fee
  - Access gradesheets.
  - Evaluate courses.


- **Organization Admin Features:**
  - Upload student and teacher’s info in csv Format
  - Upload advising info and course info in csv format
  - post announcements 



## Technologies Used

- **Django**: A high-level Python web framework for building web applications.
- **HTML, CSS, Bootstrap**: Front-end technologies for creating a responsive and visually appealing user interface.
- **JavaScript (JS)**: Used to add interactivity to the website.
- **Pandas**: A Python library for data manipulation and analysis.
- **Pillow**: A Python Imaging Library that adds image processing capabilities to your Django application.
- **Stripe API**: Used for handling payment processing.

## Installation and Setup

Follow these steps to get EasyEdu up and running on your local machine:

1. Clone the repository:

   ```bash
   https://github.com/shihabshahrier/EasyEdu.git
   ```

2. Navigate to the project directory:

   ```bash
   cd EasyEdu
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Set up the database:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser (admin account):

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin account.

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

9. Open your web browser and access the development server at [http://localhost:8000/](http://localhost:8000/). You can log in with the superuser account created earlier to access admin features.

## Usage
- Organizations can sign up and log in and access the OrgAdmin dashboard to manage Student, Faculty, Course, Advising info.
- Teachers can log in and access the teacher dashboard to manage their courses, upload materials, create quizzes and upload grades.
- Students can log in and access the student dashboard to view couses, make payment for courses, access gradesheets, evaluate courses, and perform self-advising.
- The admin panel is accessible at [http://localhost:8000/admin/](http://localhost:8000/admin/) and can be used to manage users and course-related data.

## Contributing

Contributions are welcome! If you'd like to contribute to EasyEdu, please follow these guidelines:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your fork on GitHub.
6. Open a pull request to the main repository with a detailed explanation of your changes.


