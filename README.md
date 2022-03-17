
## Blogit
### Author
Jacob Maina

### Description
This is a flask application that allows writers to post blogs, edit and delite blogs. It also allows users who have signed up to comment on the blogs that has been posted by a writer. It also allows a person to subscribed to recieve email everytime a new blog is posted by a writer.

### User Story
1. A user can view the most recent posts.
2. View and comment the blog posts on the site.
3. A user should an email alert when a new post is made by joining a subscription.
4. Register to be allowed to log in to the application
5. A user sees random quotes on the site
6. A writer can create a blog from the application and update or delete blogs I have created.

### Technology used
1. Python3.9
2. Flask
3. Heroku CLI
4. git CLI
5. Markdown
6. HTML
7. CSS
8. Bootstrap
9. GitHub

## Behaviour Driven Development (BDD)

| Behaviour   | Input      | Output |
| ------------- | ------------- | -------- |
| user loads the application         | On page load        | users see various posts/blogs posted by bloggers |
| user clicks on register button         | on click        | subscription page is loaded and user enters details for subscription  |
| writer cllicks on sign up         | On page load    | sign up page is loaded and user can sign up to be a blogger |
| writer clicks on crete blog        | on page load        | user is able to create blog on when the page loads  |
| writes clicks on edit post       | edit page is loaded        | user is able to update the blog  |
| writer clicks on delete post       | on page load        | the post is deleted  |
| writer clicks on profile       | on page load         | the comment is deleted  |

## Prerequisites
Python3.6 and above

## Setup/Installation Requirements
1. git clone https://github.com/jacobrugano/blogworld.git.

2. Note:You will need to git installed in your machine. You can install using the following command: $ sudo apt-get install git.
3. After cloning, use command cd Blog-Post.git and open using your code editor.
4. Create a vitual environment using the following command python3 -m venv --without-pip virtual
5. Activate the virtual environment using the following command . virtual/bin/activate
6. Run this command to interact with the application $python3.9 app.py server
7. Run tests units using the this command $python --version(examplepython3.9 app.py`)

### Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

### Contact Information
If you have any question or contributions, please email me at [jacobrugano@gmail.com]

### License
MIT License:
Copyright (c) 2022 Jacob Rugano