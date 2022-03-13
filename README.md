# G A L L E R I A   

An Independent project for Moringa Core Django module, Feb 28th, 2022.

## Author  
  
[Venesa Okuna](https://github.com/VenesaOkuna) 

## Description

Galleria is a photo gallery web application to showcase a collection of pictures. 

- Users get can view photos uploaded by admin. 
- Users can see photos based on the location, by clicking on the listed locations in the menu. 
- They can also copy the link to a photo to paste at their discretion. 
- And finally also search for photos based on the categories.

## Features
- The home page allows users to see various images:
- User can see all images per location they were taken
- Users can also search for images based categories
- Admin can upload images from a django dashboard


## Site Snipets
Here is the Design

<p> Landing</p>

![Landing](https://raw.github.com/VenesaOkuna/Galleria/master/static/images/landing.png)


<p> Locations</p>

![Landing](https://raw.github.com/VenesaOkuna/Galleria/master/static/images/locations.png)


<p> Gallery</p>

![Landing](https://raw.github.com/VenesaOkuna/Galleria/master/static/images/albumgallery.png)


<p> Image Details Modal</p>

![Landing](https://raw.github.com/VenesaOkuna/Galleria/master/static/images/detailsmodal.png)


<p> Footer</p>

![Landing](https://raw.github.com/VenesaOkuna/Galleria/master/static/images/footer.png)


<p> Admin</p>

![Landing](https://raw.github.com/VenesaOkuna/Galleria/master/static/images/admin.png)




## View Live Site here
View the complete site [here](mygalleriaapp.herokuapp.com/)


## Technologies Used
    - Python 3.8
    - Django MVC framework
    - HTML and Bootstrap
    - JavaScript
    - Postgressql
    - Heroku

## Specifications
To view the BDD check the [specs file](specs.md).

### Prerequisite
The Galleria project requires a prerequisite understanding of the following:
- Django Framework
- Python3.8
- Postgres
- Python virtualenv

## Setup and installation

#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE gallery;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'gallery'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.8 manage.py makemigrations gallery
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000

## Known bugs
No known bugs so far. If found drop me an email.


## Contributors
    - Venesa Okuna

### Contact Information
vanessaatieno5@gmail.com | venesaatieno5@gmail.com
