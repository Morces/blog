# BLOG
## Description

- A personal blogging website where you can create and share your opinions and other users can read them. Additionally there is feature that displays random quotes to inspire users.

## BDD 
As a user, I would like to:
- View the blog posts on the site
- Comment on blog posts.
- View the most recent posts.
- Random quotes on the site.
- Sign in to the blog.
- Create a blog from the application.


## SetUp Instructions
- You need to have python3 installed together with a virtual environment and pip.
- Set up the virtual environment and activate it.
```bash
$ python3.6 -m venv virtual
$ source virtual/bin/activate

```
- Install all necessary dependencies.
$ git clone [Repo](https://github.com/Morces/blog.git)

- Navigate into the cloned project.

$ cd blog

Export manage.py file
- $ export FLASK_APP=manage.py

Export dubug mode
- $ export FLASK_DEBUG=1

Export secret keys
- $ export SECRET_KEY='WTF_CSRF_SECRET_KEY'

To run your application use command:
- flask run

## Live Link
[Live Link](https://morces.herokuapp.com/)

## Technologies Used
- Python (Flask)
- Jinja2
- HTML
- CSS
- Bootstrap

## License
MIT License

Copyright (c) 2022 MOSES KARANI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


