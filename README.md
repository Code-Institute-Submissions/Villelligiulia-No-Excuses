# ~~NO-EXCUSES~~
No Excuses app is a Django application, which runs in the Code Institute moke terminal on Heroku.
It is a responsive ToDo List app, that allows the user to keep track of all kind of activities in an easy and nice way, as also performing other tasks such as update, delete and toggle.
It is an app that aims to be usefull to the user, helping the user to manage at his best all his tasks from any kind of device.

[Here](https://no-excuses.herokuapp.com/) is a live view on the project. 
(foto del prgetto)

## How it works
To use the app, if not already in posses of an account will have to register one which will allow to use it.
No excuses its an easy and intuitive app which allow the user once logged in to perform various actions.

## Features
The app consists of different features:
- SignIn and SignUp
   - To allow the access to the tasks the user will have to login to the app providing his/her registered user name and password, if the user is not registered will have then the chance to create an account providing a username a password and optional email address. 

![Login feature](/static/images/signin-no-excuses.jpg)
![Sign up feature](/static/images/signup-no-excuses.jpg)

### No Excuses main page
   - Once Logged in the app will welcome the recognized user and be able to use the features of the app.and be able to:
     - See all of his/her tasks ordered by date.
     - Click on the Update and Delete link which will lead respectivelty to different pages for the intended action.
     - Toggle the Task from Done to UnDone by clicking the Toggle link. If the task is unmaarked and displayed under the "To Do" section, the task will be then marked and copied in the "Tasks Completed" section.
     - Get permanently rid of the selected task by clicking the Delete button at be redirected to the Delete page and permorf the intended action.
     - Click the Add Task link and redirected to the Add task page to perfmorm the intended action.
     - Search for a particular task by typing the name of the task into the search bar and retreieve it. If the user will click the search button without inserting a value or inserting an incorrect value will be notified by the app about those actions.
     -  Logout from the app.

![No Excuses toggle task](/static/images/toggle-task-no-excuses.jpg)
![No Excuses empty search](/static/images/invalid-search-noexcuses.jpg)
![No Excuses wrong search](/static/images/no-tasks-found.jpg)

### No Excuses Update Task
- After clicking the "Update" link beside the task from the main page, the user will be redirected to the Update page and be able to:
  - Write a title for a task.
  - Add a description for a task. To do so the user will be provided with a full Summernote editor so that will be able to chose the preferred style to save his/her task.
  - Check a box and mark the task as Done.
  - Submit with a botton the update action and be redirect to the main page where the tasks list will be now updated.
  - Go back to the main page without performing any update.

![No Excuses Update page]




