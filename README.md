Project Name: Project Details Collections Form (SPA)

You can access the application through this link: http://127.0.0.1:8000/

Project Overview:

This project focuses on developing a Single-Page Application (SPA) using Django. Its core objective is to capture project details and save this data within a database. The technology stack employed for this project includes Python, HTML, CSS, JavaScript, and MySQL.

To initiate the project, you'll start by running the manage.py file using the command 'python3 manage.py runserver', which will generate a link accessible on the server side. This link provides access to the form where users can input essential project details. Upon filling out the form and clicking the 'Save' button, the information gets stored in the database.

Following a page refresh, the stored project details, such as the project title and the name of the person associated with the project, will be displayed below. The page also features options for editing, deleting, and reordering entries. The 'Edit' button enables the modification of existing content, the 'Delete' button removes the form content identified by its object ID number, and the 'Reorder' option recreates the form content with a new object ID.

An important initial step involves creating an admin superuser using the command 'python3 manage.py createsuperuser'.

Additionally, the project requires Django packages to be installed. Use the 'requirements.txt' file to install all the necessary packages. To create the Django project and run it, follow the commands listed in the 'commands.txt' file.
