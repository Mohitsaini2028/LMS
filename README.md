Income Expenses API

## Installation steps

1. Ensure you have python3 installed

2. Clone the repository
3. create a virtual environment using `virtualenv venv`
4. Activate the virtual environment by running `source venv/bin/activate`

- On Windows use `source venv\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

6. Migrate existing db tables by running `python manage.py migrate`

7. Run the django development server using `python manage.py runserver`


# Library Management System
## ![](https://via.placeholder.com/15/f03c15/f03c15.png)   ``ADMIN functionalities``
<li> Add a book</li>
<li> Update a entry of a book</li>
<li> Delete a book</li>
<li> Get all books</li>


## ![](https://via.placeholder.com/15/c5f015/c5f015.png) ``Student functionalities``
<li> Get all books</li>
<li> Search books by title</li>

## Urls
  <li><b> /login </b> :- Handle the data received from login form and authentication of user.</li>
  <li><b> /signup </b> :- Render the signup form template.</li>
  <li><b> /signupHandle </b> :- Handle the data received from form and user account creation task.</li>
  <li><b> /logout </b> :- Handle user logout request.</li>
  <li><b> /new-book </b> :- Render the Add new book template.</li>
  <li><b> /add-book </b> :- Add a new to existing database as well as reflect the changes in the UI.</li>
  <li><b> /delete-book </b> :- Delete particular book in the database.</li>
  <li><b> /edit-book </b> :- Render edit book form template.</li>
  <li><b> /edit </b> :- Edit a particular book record.</li>
  <li><b> /search-book </b> :- Render search page.</li>
  <li><b> /search </b> :- Find book by user request and displaying the output to the user.</li>

https://sourcecodehero.com/library-management-system-project-in-django-with-source-code/
