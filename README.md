# ~~NO-EXCUSES~~
No Excuses app is a Django application, which runs in the Code Institute moke terminal on Heroku.
It is a responsive ToDo List app, that allows the user to keep track of all kind of activities in an easy and nice way, as also performing other tasks such as update, delete and toggle.
ITo use the app, if not already in posses of an account, the user  will have to register one which will allow to use it.
No excuses its an easy and intuitive app which allow the user once logged in to perform various actions.t is an app that aims to be usefull to the user, helping the u to manage at his best all his tasks from any kind of device.

![No Excuses responsive mockup](/static/images/responsive-noexcuses.jpg)

[Here](https://no-excuses.herokuapp.com/) is a live view on the project.


## Features

No Excuses app offers a range of features across its various pages, including Sign In and Sign Out functionality, a user-friendly main page for task management, intuitive Add/Update task pages for easy task modification, convenient task deletion, and a simple Logout option.
The landing page of the app is designed to provide users with a brief introduction and enticing message about the app's purpose and functionality. 
The page greets users with an engaging introduction, emphasizing the importance of staying organized and on top of their tasks. Also, also offers convenient options to log in or register for a new account.

![No Excuses Landing Page](/static/images/intro.jpg)

  ### SignIn and SignUp
 
- To provide access to the tasks, users are required to log in to the app by entering their registered username and password. If a user is not registered, they have the opportunity to create a new account by providing a username, password, and optional email address. Those authentication features are provided by "Django allauth package" allowing the user to easily perform those actions. The authentications pages have been then customized to align with the overall style of the application.

![Login feature](/static/images/signin-no-excuses.jpg)
![Sign up feature](/static/images/signup-no-excuses.jpg)

### No Excuses main page

-Once logged in, the app welcomes the user and enables them to perform the following actions:

  - View Tasks: Users can easily access all their tasks, which are conveniently ordered by date, providing a clear overview of their task list.
  - Update and Delete: By clicking the "Update" and "Delete" links, users can navigate to dedicated pages to modify or permanently remove tasks, respectively.
  - Toggle Task Completion: Users can mark tasks as complete or incomplete by clicking the "Toggle" link. When a task is marked as complete, it is moved from the "To Do" section to the "Tasks Completed" section, and vice versa.
  - Add Task: Users add new tasks by clicking the "Add Task" link, which redirects them to a page where they can enter the necessary information for the task.
  - Search Task: A search bar allows users to quickly find a particular task by entering its name. The app retrieves matching tasks based on the search query. In case of empty or incorrect search inputs, the app provides appropriate notifications.
  - Logout: Users can securely log out from the app, ensuring the privacy and security of their tasks and account.

![No Excuses toggle task](/static/images/tasks-list.jpg)
![No Excuses empty search](/static/images/invalid-search-noexcuses.jpg)
![No Excuses wrong search](/static/images/no-task-found.jpg)

### The Uppdate/Add task page
  When users click either the "Update" link next to a task or the "Add Task" link at the bottom of the page, they are redirected to a dedicated page where they can perform these actions. On this page, users are presented with the following options:

- Task Title: Users can enter a title for the task they are updating or adding.
- Task Description: The task description field provides users with a full-featured text editor. This allows them to customize the appearance and format of their task description according to their preferences.
- Done Checkbox: Users have the option to mark the task as "Done" by checking the corresponding checkbox. When this checkbox is selected, the task is automatically updated in the task list to reflect its completion status.
- Submit Button: After entering the necessary information, users can click the Submit button to save and update the task or add a new task, depending on the action performed. By providing these input fields and options, the app enables users to easily update or add new tasks with personalized titles and detailed descriptions. The flexibility of the full-featured text editor ensures that users can customize the formatting and style of their task descriptions as desired.

![Add/Update page](/static/images/add-update.jpg)
![Update task list](/static/images/taskview.jpg)

### The Delete Task Page
- By clinking the "Delete" link beside the task, the user is redirected to the Delete page, where will be asked if certain about removing the task chosen from the task list. The user qill be able to confirm this action or go back to the main page.

![Delete Task page](/static/images/delete-task-no-excuses.jpg)

### The Logout Page
- Fianlly the user will be able to safely leave the app by clicking the "Logout" link from the main page. Equally to the Sign In/Sign up features, the Logout is also provided by "Django allauth package", but the additional "Go back to your list" link feature has been added to the customization of the page to improve the overall UX by giving the user flexibilty and options for who may have accessed the logout page by mistake or wish to continue using the app, giving the user full control of the application.
  
![Signout page](/static/images/signout.jpg).

## Messages
The app incorporates informative messages for every action performed by the user. The messages have the purpose to keep the user informed reasing awareness over the changes anc actions taken in the app. Those will be displayed for: successfull login and logout, added/updated task, deleted task and the mentioned above invalid or wrong search.
- Successful login message
![Successful login message](/static/images/login-success.png)

- Successful logout message
![Successful logout message](/static/images/logout-message.png)

- Added task message 
![Added task message](/static/images/added-message.png)

- Updated task message
![Updated task message](/static/images/updated-message.jpg)

- Deleted task message
![Deleted task message](/static/images/del-message.png)


 # UX
 
 ## The Strategy plan
 
 No Excuses app is intended to be a friendly and intuitive ToDo application that is usefull to the user in tasks management. With a simple layout but efficient and intuitive the user can effortlessy have access to the task list, customize its details, quickly retrieve it with a search funcionality, add, update, mark it as complete, permanently delete it and and have exclusively access to it thanks to a user authentication system.

 ## Site Goals

 The application objective is to develop a responsive and intuiitive ToDo list application that engaaes with the user with clear and frequent messages. 

 ## Epics

 For the development of the project 8 Epics with 8 User Stories were created.  Details of the Agile Design Thinking approach can be found in the project Kanban board [here](https://github.com/users/Villelligiulia/projects/4/views/1)

   1. View task list.
   2. Select a task.
   3. Manage a task.
   4. Mark a task complete.
   5. Search task.
   6. Account Registration.
   7. Important task
   8. Set task due date and receive reminders.

## User Stories

For each Epic, one User Story has been developed for a total of 8 User Stories. Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have. Out of those Epics and respective User Stories 6 were completed and implemented of which 5 with "must have" label, assigned to "Task Management App Mvp" that provides  core functionlity and essential task management features , and 1 with "should have" label providing  an additional element and increasing the overall user experience.
Individual user stories were categorised according to whether they had to be implemented to produce a Minimum Viable Product , with priority for development to be given to those that were part of the MVP specification.


- ## Implemented User stories.

### Epic: View Task List#1

As User i can view the task list so that i can select and check the task i need to do

#### Acceptance Criteria: 

 - The user can access the task list page.
 - The task list displays all tasks with their titles.
 - The user can see an indication of completed tasks.
 
#### Implementation:

 - Create a route in Django for the task list page.
 - Retrieve all tasks from the database.
 - Clear access to the task list
- Clear task titles in the task list template.
- Clear separation between completed and uncompleted tasks.


### Epic: Select a task#2

As User i can click on a particular task so that i can see the details of that task

#### Acceptance Criteria:

 - The user can click on a task from the task list.
 - Clicking on a task redirects the user to the task details page.

#### Implementation:

- Create a  link for each task in the task list template.
- Create a designated task detail page
- Create the path from the link to the task details page to redirect the user.
- Retrieve the specific task details from the database.
- Display the task details in the task details page


### Epic: Manage tasks#3

As User i can read, add, update and delete tasks so that i can manage my tasks list

#### Acceptance Criteria:

 - The user can create new tasks.
 - The user can edit existing tasks.
 - The user can delete tasks.


 #### implementation: 
 - Add a link to perform add action.
 - Create designated add task page
 - Create a path to redirect the user to add task page.
- Create a form to register task info: title and description text field that comes with a full editor.
- Create a button to submit the action.
- Validate and save the new task to the database.
- Add a link to perform update action.
- Create a path to redirect the user to update task page.
- Pre-fill the form with already existing task detail for the user to update.
- Create a button to submit the action.
- Validate and update the task in the database.
- Create a link to perform delete action.
- Create a designated delete page.
- Create a path to redirect the user to delete page.
- Confirm the task deletion and remove it from the database.

### Epic: Mark a task as completed #4

As User i can mark a completed checkbox and strike a task off so that i know which tasks dont have to be done

#### Acceptance criteria:

- The user can mark a task as completed.
- Completed tasks are visually distinguished from active tasks.

 #### Implementation:

- In the task model add a checkbox to mark task as completed from the add/update page.
- Update the visual representation of the tasks reflecting 
checkbox behaviour
- Create a link to perform toggle action
 - Implement the functionality to toggle the completion status of tasks.
 - Update the visual representation of the tasks reflecting checkbox behaviour

### Epic: Account registration #7
As User i can register a new account so that i can be the only person that has access to the tasks list

#### Acceptance criteria:

- The user can register a new account.
- Account registration ensures unique access to the task list.

#### Implementation: 

- Clearly accessible link to login or register within main navigation bar
- Easy actions for the User in order to create an account
- Restrict access to the task list exclusively to the logged in user

### Epic: Search a task #5
As User i can search for a particular task so that i can be quicker in finding the task i'm interested into

#### Acceptance criteria:

 -The user can search for a task by its title.
 - Search results display matching tasks

#### Implementation: 
- Create an input text to insert the task title for the search.
- Create a search button to send request to retrieve the task searched.
- Retrieve correct task from tasklist
- Return matching task to task searched
- Handle possibile search senario such as invalid search or empty search.


## Feature Features
The remaining two User Stories provide additional features that will enhance the funcionality and user experience of the app. 


## Wireframe Design and Styling Approach
The wireframe for my project was intentionally designed to have a simple and straightforward style. I wanted to create a clean and minimalist layout that focused on functionality and ease of use. The wireframe served as a blueprint for the app's structure and guided the development process.
During the implementation phase, I made some minor adjustments to the positioning of certain elements for style purposes.

![wireframe landing page]  
![wireframe task list] 
![wireframe add/update] 
![wireframe delete] 
![wireframe ] 


## Database schema 
The database schema was implemented using [Lucidchart](https://www.lucidchart.com/pages/?gspk=eXVsaWFzYWRvdmExOTMz&gsxid=ORkF5zrs1X9l&pscd=try.lucid.co&sid=3CehEubVwGiRLxsMJlM84OGyCDf2RrOo7WSLQzR9opc8me&utm_campaign=partnerstack&utm_medium=affiliate-partner&utm_source=yuliasadova1933).

![Database scheme](/static/images/db-scheme.jpg)
For the purpose of the project, a custom modelcalled "Task" was created, based on the "Item" model of the "Hello Django" project, which has then been altered as per Project Portfolio requirements.
The User model is provided by Django's allauth package authentication system .
The relationship between the User model and the Task model is established through a foreign key relationship. In the Task model, the user field is a foreign key to the User model and by doing so each task is linked to a specific user.
The "Task" Model represents the structure of the task that the user creates and consists of the following fields:
- user: foreign key to the User model mentioned above.
- title : is a character field with a maximum length of 200 characters. It stores the title or name of the task.




The Task Model includes the following fields :

- title:
