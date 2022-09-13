# Library Management System

## Installation steps

1. Ensure you have python3 installed

2. Clone the repository
3. create a virtual environment using `virtualenv venv`
4. Activate the virtual environment by running `source venv/bin/activate`

- On Windows use `source venv\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

6. Migrate existing db tables by running `python manage.py migrate`

7. Run the django development server using `python manage.py runserver`


# Users
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

## Project Overview
### ```User Registration```
Login page | Signup page
:-------------------------:|:-------------------------:|
![](https://user-images.githubusercontent.com/66358041/189936047-9074e32b-fa75-4850-baa5-9a8f9c54f68c.png) | ![](https://user-images.githubusercontent.com/66358041/189936511-ab1d8dd3-7db3-4b79-9c9a-f9465ee59532.png)

### ```View book record```
![chrome_7JSFsOVETR](https://user-images.githubusercontent.com/66358041/189936691-518d4555-a78e-4cba-8b8e-8d71752d9d69.png)

### ```Add book```
![chrome_8okDjfLS7R](https://user-images.githubusercontent.com/66358041/189937068-e5aa1de8-eca4-49a4-9814-c39a9bf8adb8.png)

### ```Edit book```
Edit page| Record edited
:-------------------------:|:-------------------------:|
![chrome_ObueI4BAom](https://user-images.githubusercontent.com/66358041/189937693-6fdbcbfd-070b-4127-bd87-aa94d533b693.png) | ![chrome_L6CHHTIM0n](https://user-images.githubusercontent.com/66358041/189937747-4a62e392-0142-4990-93e1-90596059f8d4.png)

### ```Delete book```
Delete page| Record deleted
:-------------------------:|:-------------------------:|
![](https://user-images.githubusercontent.com/66358041/189937974-4fdfec27-6a57-4531-a852-70be838f3de0.png) | ![](https://user-images.githubusercontent.com/66358041/189937983-0347c92b-9a62-428c-89bc-ff867cd985af.png)


### ```Search book```
![chrome_f4vjAeIEp3](https://user-images.githubusercontent.com/66358041/189938189-1ad00c7a-d286-4fdb-86b6-97893de9e4d4.png)

### ```Search result```
![chrome_Bcood2V6Ed](https://user-images.githubusercontent.com/66358041/189938197-a50cb8b4-c7a5-453c-9d40-a7e4a2b03bdf.png)

### ```Only admin can access 'create', 'update' and 'delete' book record```
![chrome_UuO5JEuj5P](https://user-images.githubusercontent.com/66358041/189938630-9a366870-6ab8-4f4d-af21-fff1ae754320.png)



