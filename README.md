# Freelance Services 

# Aim
The goal of this site is to enable freelancers to be able to sell thier services online. This will be done by presenting the freelancers previous work, a list of services that they provide and giving the customer the oppurtunity to buy the services. 

[Deployed Project](https://shop.ethancundick.com)

## User Stories

### Customer
- A customer to the site must be able to see a list of services that the Freelancer provides. 
- A customer to the site must be able to add a "service" to a basket. 
- A customer to the site must be able to purchase a service.  
- A customer must be able to register
- A customer must be able to log in 
- A customer must be able to reset thier password
- A customer must be able to change thier password
- A customer must be able to edit thier profile
- Payment - secure payment method using Stripe integration

### Freelancer
- The freelancer must be able to see orders from the admin panel 
- Freelancer must be able to add, edit and delete services they offer through the admin panel
- Freelancer must be able add,edit and delete items on the homepage

## Features 
- Login - allows user to login
- Sign Up - sign up new users
- Profile - edit, update, change the password
- Site admin - Create, edit, delete Services
- SIte admin - Create, edit, delete items on the homepage, allowing freelancer to edit their own site.

## Future Features
- Previous_Work
- Sign in with just email

## Django Design

### Django Apps
- Home
    - Used to display index page with homepage object values. 
- Services
    - A list of services that are offered, values taken from services object.
- Basket
    - Used to store items in pre-purchase
- Checkout 
    - Used to take payment
- Accounts
    - Used for all user authentication tasks. 
- Freelance_Services
    - Initial django project handles urls

### Django Models/Database Design
- Services 
    - Name
    - Description
    - Price
- Order
    - full_name
    - phone_number
    - country 
    - postcode 
    - town_or_city
    - street_address1
    - street_address2 
    - date 

- Homepage
    - title 
    - name 
    - headline 
    - subheadline
    - about
    - first_skill_name 
    - first_skill_description
    - second_skill_name 
    - second_skill_description
    - third_skill_name 
    - third_skill_description 

## Technologies Used
- HTML5
- CSS3
- JavaScript
- Python
    - Back end language
- Django 2.2
    - Python Framework
- Google Cloud MYSQL
    - Google hosted MySQL database
- Google Cloud App engine
    - Google Cloud Serverless web application hosting
- Bootstrap Framework
    - Front End Framework
- VSCode
    - IDE for development
- Chrome Dev Tools



## Deployment

To deploy my app I used Google Cloud Platforms App Engine, to do this in the Google Cloud admin console I selected App Engine which took me to the App Engine dashboard. From the App Engine dashboard I selected Create Project  and named it " ci-django-freelance-services". 

I then downloaded the Google Cloud SDK, this allowed me to use the CLI to create and deploy my app, after this I enabled APIs to be used on my project this allowed my app to communicate with Google Cloud SQL. 

Next I ran the below: 

	gcloud auth application-default login
	gcloud services enable sqladmin

This creates credentials that allow you to use the Cloud SQL Admin API, and then enables the API.

Next I created a Cloud SQL Instance using:
 
	gcloud sql instances describe [INSTANCE_NAME]

This created a MySQL 5.7  database  instance for me to use. 

In my settings.py I added the lines: 

	if os.getenv('GAE_APPLICATION', None):
	    # Running on production App Engine, so connect to Google Cloud SQL using
	    # the unix socket at /cloudsql/<your-cloudsql-connection string>
	    host = os.getenv('GCSQL_HOST')
	    DATABASES = {
	        'default': {
	            'ENGINE': 'django.db.backends.mysql',
	            'HOST': '/cloudsql/{}'.format(host),
	            'NAME': os.getenv('GCSQL_DBNAME'),
	            'USER': os.getenv('GCSQL_USER'),
	            'PASSWORD': os.getenv('GCSQL_PASSWORD'),
	        }
	    }

This told my django installation to connect to the Cloud SQL Instance. 

I added the app.yaml in the root directory of my project, this tells google app engine how to deploy me application 

	  runtime: python37
	  handlers:
	  # This configures Google App Engine to serve the files in the app's static
	  # directory.
	  - url: /static
	    static_dir: static/
	  
	  # This handler routes all requests not caught above to your main app. It is
	  # required when static routes are defined, but can be omitted (along with
	  # the entire handlers section) when there are no static files defined.
	  - url: /.*
	    script: auto    
	  
	  env_variables:
	    GCSQL_USER : 
	    GCSQL_PASSWORD : 
	    GCSQL_HOST : 
	    GCSQL_DBNAME : 
	    SECRET_KEY : '

I also needed  to create a main.py file which contains the below: 

	from freelance_services.wsgi import application
	# App Engine by default looks for a main.py file at the root of the app
	# directory with a WSGI-compatible object called app.
	# This file imports the WSGI-compatible object of your Django app,
	# application from mysite/wsgi.py and renames it app so it is discoverable by
	# App Engine without additional configuration.
	# Alternatively, you can add a custom entrypoint field in your app.yaml:
	# entrypoint: gunicorn -b :$PORT mysite.wsgi
	app = application
	
To ensure the required packages are installed Google App Engine checks for a requirements.txt file and will install any pip packages within it. To create this file I used: 

	pip freeze > requirements.txt
	
This takes all of my installed pip packages within my virtual environment and inserts them into my requirements file.

Finally I ran:

    gcloud app deploy

## Manual Testing

### Customer
Requirement: A customer to the site must be able to see a list of services that the Freelancer provides. 
- Tested by browsing to the services page on mobile, tablet and desktop and ensuring services are viewable.

Requirement: A customer to the site must be able to add a "service" to a basket. 
- Tested by logging in and click add to basket on the service page then browsing to basket to see that its there. 

Requirement: A customer to the site must be able to purchase a service.  
- Tested by going to checkout and filling out the required form and seeing the payment go through on stripe. 

Requirement: A customer must be able to register
- Tested by clicking on the register link, filling out the form and then getting logged in.  

Requirement: A customer must be able to log in 
- Tested by clicking on the login button entering a username and password and viewing pages that are for logged in users only. 

Requirement: A customer must be able to reset thier password
- Tested by browsing to sign in page and clicking the reset password link 

Requirement: A customer must be able to change thier password
- Tested by going to the "My Profile" page clicking reset password and filling out the form, then log in with the new password. 

Requirement: A customer must be able to edit thier profile
- Tested by going to the "My Profile" page and changing the values of the form listed. 

Requirement: Payment - secure payment method using Stripe integration
- Tested by going adding a service to a basket, going to checkout and filling out the form and then clicking submit payment then logging into stripe and seeing the payment in the dashboard, 

### Freelancer
Requirement: The freelancer must be able to see orders from the admin panel 
- Tested by logging into the admin panel and clicking orders after completing a payment on the front end.

Requirement:Freelancer must be able to add, edit and delete services they offer through the admin panel
- Tested by adding services on the backend and then browsing to the services page on the front end. 

Requirement: Freelancer must be able to edit the home page. 
- Tested by logging into the admin panel going to homepage and editing the value and seeing it update on the front end.

### Disclaimer
This is for educational use.