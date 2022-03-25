#  Inventory 

This is a web app made by using django-python framework.

In this web app user can search for a books by entering the name of the book and from there they will get the link of the book and after getting the link if they want to store the book in the database they can store it by pressing inventory button present at the homescreen and pasting the url of the book.
At the backend only necessary thing is the id of that particular book.

** Features **
* User can add a book or also copy of a existing book to the bookstore.

  * remove or delete the book from the bookstore.

  * can also remove or delete the book from the bookstore.
  
  * A search box which shows the books with the help of Google Book Api for the given query.
  
  * Searched books have text on their bottom, weather it is already exist in bookstore or not.
  
 ** Assumptions **
 
  *Added some books with popular keywords to the inventory using Google book API with a script(base_script.py)
  
  * Delete and Edit options are only for the books that are in the inventory.
  
 ** Installation and Running the server **
 * Create a virtual environment using python -m venv env {here env is the name of our virtual environment}
 * git clone https://github.com/krishnakanttripathi988/krishna-book-store.git
 
** Install Requirements **
  * change the directory to the root of bookinventory(where manage.py is present)
  * pip install -r requirements.txt
  * python manage.py makemigrations
  * python manage.py migrate
** Running the server **
 * python manage.py runserver {make sure you have installed postgresql and the user and password in the settings.py is okay}
 your app will be running on localhost:8000
    
 [Live app on heroku](https://krishna-bookinventory.herokuapp.com/inventory/)
  

 
  
