# Django App

Demonstration of a very basic django app that fetches data from a remote api and displays it.

# Task Summary
Render data from an API using a language you have never used before, using tools you have never handled.

This task is designed to test your agnostic skills, understanding of the shared concepts of web servers, package managers, control flow, and REST that all web based languages and frameworks use. This will also test how you handle something completely outside of your skill set.

Mission:
   1) Use Python to perform a RESTful API request on https://jsonplaceholder.typicode.com/posts. Take the data and render it to the browser. Use bootstrap (http://getbootstrap.com/) to style the posts on the screen so you don't have to worry about frontend.
   3) Only render posts with the numbers 4,2 and 7 in the id.
   2) List everything you google
   3) List the problems you faced and how you solved them/ or what you did to avoid them.
   4) If you use a lib, copy/paste code or apply a technique, use a package or technology; please note them down and your justifications for using them.

## Installation

Clone this repo and install the dependencies in testsite/settings.py:
    $ pip install django-bootstrap3
    $ ./manage.py runserver

## Usage

Visit http://127.0.0.1:8000/ to view the posts.
