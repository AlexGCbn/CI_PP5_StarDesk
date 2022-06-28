# CI_PP5_StarDesk
StarDesk is a computer hardware/components E-Commerce store, built as my 5th Portfolio Project for Code Institute's Full Stack Web Development Diploma, focused on E-Commerce. 

- There are two types of users, admins and regular users.
- Test accounts can be given on demand.
<br>

** View the live website [here](https://stardesk.herokuapp.com/)**
<br><br>
![Website hero image](/docs/readme-hero.png)

# Table of contents
- [Project Overview](#project-overview)
- [UX](#ux)
    * [Strategy](#strategy)
        + [Primary Goals](#primary-goal)
    * [Structure](#structure)
        + [Website pages](#website-pages)
        + [Code Structure](#code-structure)
        + [Database](#database)
            - [Database diagram](#database-diagram)
            - [Models](#models)
    * [Scope](#scope)
        + [User Stories](#user-stories)
    * [Design](#design)
        + [Colours](#colours)
        + [Fonts](#fonts)
- [Features](#features)
    * [Feature 1 - Homepage and deals](#feature-1)
    * [Feature 2 - Navbar](#feature-2)
    * [Feature 3 - Footer](#feature-3)
    * [Feature 4 - Messages](#feature-4)
    * [Feature 5 - Bag](#feature-5)
    * [Feature 6 - Products](#feature-6)
    * [Feature 7 - Product categories](#feature-7)
    * [Feature 8 - Product details](#feature-8)
    * [Feature 9 - Product admin](#feature-9)
    * [Feature 10 - Newsletter](#feature-10)
    * [Feature 11 - Search bar](#feature-11)
    * [Feature 12 - Product sorting](#feature-12)
    * [Feature 13 - Profile info](#feature-13)
    * [Feature 14 - Order History](#feature-14)
- [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and other resources](#libraries-and-other-resources)
- [Testing](#testing)
- [Deployment](#deployment)
  * [Local Deployment](#local-deployment)
  * [Heroku and Postgres Database](#heroku-and-postgres-database)
- [Credits](#credits)

# Project Overview
- This project is a website for the Portfolio Project 5, part of the Code Institute Diploma in Software Development (E-commerce Applications)
- The website is deployed using Heroku at the following URL: [Hike-a-Thon](https://stardesk.herokuapp.com/)
- The GitHub repository contains all the source code, Issues, Project (kanban board) and assets. It can be found [here.](https://github.com/AlexGCbn/CI_PP5_StarDesk)
- The website is fully responsive for all media sizes

# UX
## Strategy
### Primary Goals

The primary goals of the website admins are:
- To add, edit and delete products.
- To add product deals.
- To be able to see and manage user reviews.

The primary goals of the website users are: 
- To register for an account on the website. 
- To sign in and sign out of the website. 
- To view a list of all products.
- To view a list of all products of chosen category.
- To be able to search for a product.
- To add, update and remove products from their bag.
- To be able to complete their purchase.
- To be able to save their information for future checkouts.
- To see their order history.

## Structure
### Website pages
- The website is structured into 17 pages.
- All pages extend the same base, so they have the same look.
- Pages are described below.

Page            |Description
:-------------         |:------------- 
Home     |The homepage consists of a welcome message and cards for product deals
All products     |Contains all products and sorting functionality
Product categories (7)     |Each product category has a page, 7 total
Product details     |Contains details of chosen product, along with reviews and admin controls      
Bag     |Contains all bag items
Checkout     |Visitors can checkout to complete their purchase
Checkout Success     |Visitors can view their completed purchase details
Register     |Users can sign up for an account
Login     |Users can sign in with their accounts
Logout     |Users can sign out of their accounts
My Profile     |Users see their saved information and order history

### Code Structure
- The project contains 6 apps.
    * Bag app, to handle the products in the bag
    * Checkout app, to handle all checkouts and webhooks
    * Home app, to contain homepage and deals functionality
    * Products app, to contain all product models and pages
    * Profiles app, for users to save their info and view their orders
    * Reviews app, for users to add product reviews
- The project is accompanied by:
    * templates
    * README (This file)
    * TESTING (Documentation about testing)
    * Procfile (To run the deployed application)
    * Requirements.txt (Contains all necesary libraries required)
    * Robots.txt (Required for search engine optimisation)
    * Sitemap.xml (Required for search engine optimisation)
- The project was built with the help of the Django Blog app.

### Database
- The project uses a relational database (PostgreSQL)
- Data is handled by the application with Django

#### Database diagram
The database diagram can be seen below:<br>
![Database diagram image](/docs/db_schema.png)

#### Models
##### User
- The User model contains information about each user that registers
- It is part of the Django allauth library
- The following fields are used for this project: username, email, password

##### UserProfile
- The UserProfile model is used to store the user's information, so they can checkout more easily
- It has most of the necessary checkout fields with the "profile_" prefix added
- Fields: full_name, phone_number, country, city, postcode, street_address1, street_address2

##### Product
- The Product model has submodels for each product category
- The main model contains all shared fields and the submodels contain unique ones
- Shared fields: model, manufacturer, image, description, price, rating
- Submodels have unique fields that can be used to connect them, in case project is developed to check whether components match with each other

##### ProductCategoryReview
- Used to add reviews to products
- Model/submodel could be used here, too, yet there weren't many fields
- There are 7 total ProductCategoryReview models, one for each type of product. "ProductCategory" should be replaced with the product model.
- Fields: product, user, score, comment

##### DealProduct
- Used by admins to add product deals
- Has main DealProduct model and 7 submodels, one for each product model.
- Contains the following fields: product, price_new, deal_ends

##### Order
- Used to create the orders on the website
- Is directly linked to the User, while having the OrderLineItems linked to it
- Fields: user, email, full_name, phone_number, country, city, postcode, street_address1, street_address2, date, delivery_cost, order_total, grand_total, original_bag, stripe_pid
- Calculates the delivery_cost, order_total and grand_total in its functions

##### OrderLineItem
- Used to create order lineitems
- Has main OrderLineItem model and 7 submodels, one for each product model
- Related directly to Order
- Total price is updated when it is created

## Scope
The User Stories are described below
### User Stories

Potential Customer
1. As a **potential customer** I can **see a home page** so that **I get information about the website/store**
2. As a **potential customer** I can **get to the products page** so that **I find all available products**
3. As a **potential customer** I can **get to an offers page** so that **I can find deals on the products**
4. As a **potential customer** I can **get redirected to the login page if I visit a logged-in-only page** so that **I can log in or sign up**
5. As a **potential customer** I can **find a sign up button on the navigation** so that **I can sign up**
6. As a **potential customer** I can **find a sign up button on the sign in page** so that **I can directly go to the sign up page**
7. As a **potential customer** I can **sign up for an account** so that **can access all that the website offers**
8. As a **potential customer** I can **find a sign in button on the navigation** so that **I can sign in easily**
9. As a **potential customer** I can **add items to my order without signing in** so that **I can make an order as a guest**
10. As a **potential customer** I can **complete an order without signing in** so that **I can make an order as a guest**
11. As a **potential customer** I can **add items to my order while signed in** so that **I can make an order as a user**
12. As a **potential customer** I can **complete an order while signed in** so that **I can make an order as a user**
13. As a **potential customer** I can **find a social media link** so that **I can visit the store's social media account**
14. As a **potential customer** I can **visit a product's details page** so that **I can learn more about it or add it to my bag**
15. As a **potential customer** I can **see my bag** so that **products added in it are visible**
16. As a **potential customer** I can **see confirmation or error messages** so that **I know whether an action was successful or failed**
17. As a **potential customer** I can **get an email for the order confirmation** so that **I have a copy of my order**

Recurring customer
18. As a **recurring customer** I can **use my profile information in an order** so that **I can complete my order faster**
19. As a **recurring customer** I can **see my order history** so that **I know what I have ordered in the past**
20. As a **recurring customer** I can **edit my profile** so that **my information is up to date**

Admin / Website owner
21. As a **website owner** I can **access an "add product" page** so that **I can easily add new products**
22. As a **website owner** I can **access an "edit product" page** so that **I can update its information**
23. As a **website owner** I can **delete a product** so that **it gets removed from the catalog**
24. As a **website owner** I can **access the admin panel** so that **I have control of my page's data**

## Design

### Colours
The colour palette was taken from [Color Hunt](https://colorhunt.co/palette/06283d1363df47b5ffdff6ff)<br>
![Colour palette used](/docs/colour_palette.png)

### Fonts
The fonts used are from the Google Fonts library, and are the following:
Rubik for the logo
Ubuntu for the website's text

# Features

### Feature 1 - Homepage and deals
- The homepage contains a welcome statement, a hero image and the deals section
- Deals section is updated automatically as deals are added or when they end
- Each deal has a card and provides necessary information

#### User stories covered:
1, 3

![Homepage image](/docs/features/pages/home_top.png.png)
![Homepage image](/docs/features/pages/home_bottom.png.png)
![DEals image](/docs/features/deals.png)

### Feature 2 - Navbar
- The navbar contains links to all products and their categories
- It is fully responsive, as it changes between static and sticky based on screen size (a refresh might be needed)
- Products and categories are tucked inside a dropdown hamburger menu
- Also contains search bar feature, user controls and bag button

#### User stories covered:
2, 5, 8, 15

![Navbar image](/docs/features/products_menu_1.png)

### Feature 3 - Footer
- Footer contains a site map with links
- Always stays on the bottom of the page
- Also contains newsletter feature and social links
- Facebook button directs to store Facebook page, rest are mock

#### User stories covered:
2, 13

![Footer image](/docs/features/footer.png)

### Feature 4 - Messages
- Django messages are used with Bootstrap toasts
- Messages are displayed on successful or unsuccessful user actions

#### User stories covered:
16

![Success message image](/docs/features/messages_success.png)

### Feature 5 - Bag
- Visitors can add products to their bag so they can prepare for checkout
- There is a bag button in the navbar which shows the grand total
- Users can update or remove items from their bag page directly

#### User stories covered:
9, 11, 15

![Bag button image](/docs/features/bag_button.png)
![Bag button image](/docs/features/pages/bag.png)

### Feature 6 - Products
- All products displayed here
- Sorting menu on the left of the page (or top for mobile)
- Go-to-top button on the bottom right of the page
- Pagination to display maximum of 10 products

#### User stories covered:
2, 9, 11

![Products image](/docs/features/pages/all_products.png)

### Feature 7 - Product categories
- Choosing a product category (with or without sorting) leads to that category's products page
- Same as the all products page, there is a sorting menu and a go-to-top button, along with pagination if there are enough products

#### User stories covered:
2, 9, 11

![Product categories image](/docs/features/pages/products_cases.png)

### Feature 8 - Product Details
- All specific product details on page
- Visitors can adjust the quantity and add as many products as they want to their bag (max. 99)
- Users can review the product
- User reviews visible on the bottom of the page

#### User stories covered:
14

![Product details image](/docs/features/pages/product_details_top.png)
![Product details bottom image](/docs/features/pages/product_details_bottom.png)

### Feature 9 - Review trip
- Users can review trips they have registered for and are completed
- They need to complete the form with at least some data
- The score they provide is added to the total score average
- They can edit the review later or delete it

#### User stories covered:
10

![Trip review guide image](/docs/features/new_review_1.png)
![Trip score image](/docs/features/score_before_review.png)
![Trip review guide image](/docs/features/new_review_2.png)
![Trip review guide image](/docs/features/new_review_3.png)
![Trip score image](/docs/features/score_after_review.png)
![Trip review edit guide image](/docs/features/edit_review_1.png)
![Trip review edit guide image](/docs/features/edit_review_2.png)
![Trip review edit guide image](/docs/features/edit_review_3.png)
![Trip delete review image](/docs/features/delete_review_1.png)
![Trip delete review image](/docs/features/delete_review_2.png)

### Feature 10 - Registered trips (Dashboard)
- Users can view all the trips they have registered for
- Completed trips have a checkmark
- All trip names are links to the trip details
- If the user deregisters from one trip, it is removed

#### User stories covered:
5, 9

![Trip history image](/docs/features/registered_trips_1.png)
![Trip Deregister image](/docs/features/trip_deregister.png)
![Trip history image](/docs/features/registered_trips_2.png)

### Feature 11 - Request trip
- Users can make a trip request
- The trip request will be added to their request history
- The admin can approve it and they will see an 'X' for not approved (default) or a checkmark if approved

#### User stories covered:
11

![Trip request image](/docs/features/request_1.png)
![Trip request image](/docs/features/request_2.png)

### Feature 12 - Admin panel Request page
- Admin can see trip requests
- They have the option to approve any they want

#### User stories covered:
14

![Admin trip request image](/docs/features/admin_approve_request_1.png)
![Admin trip request image](/docs/features/admin_approve_request_2.png)
![Admin trip request image](/docs/features/admin_approve_request_3.png)
![Admin trip request image](/docs/features/admin_approve_request_4.png)

### Feature 13 - Admin panel Trips page
- Admin can see trip objects and add new ones
- They need to add necessary data to trips
- They can choose which users to pre-populate 'registered_users' with

#### User stories covered:
13, 15

![Admin new trip image](/docs/features/admin_add_trip_1.png)
![Admin new trip image](/docs/features/admin_add_trip_2.png)
![Admin new trip image](/docs/features/admin_add_trip_3.png)
![Admin new trip image](/docs/features/admin_add_trip_4.png)
![Admin new trip image](/docs/features/admin_add_trip_5.png)

### Feature 14 - Footer
- Footer contains basic contact information
- Is always located at the bottom of the page and does not overlap with content

#### User stories covered:
4

![Footer image](/docs/features/footer.png)

# Technologies used
## Languages
The languages used are:
- HTML
- CSS
- JavaScript (only what is created by Django - No personal code)
- Python

## Libraries and other resources
The project is based on Django, but contains the following resources, too:
- Bootstrap 5
- PostgreSQL
- Balsamiq
- Coverage
- HTML Markup Validation
- CSS Validation Service
- PEP8 Validation
- Quick Database Diagrams
- Crispy Forms
- FontAwesome
- Google Fonts
- Github
- Heroku

# Testing
All conducted testing can be found on the separate file, [TESTING.md](TESTING.md)

# Deployment
## Note
The project uses Cloudinary for static files hosting and it is needed for deployment and development.
## Local Deployment
You can clone this repository and run it locally with the following steps:
1. Login to GitHub (https://wwww.github.com)
2. Select the repository AlexGCbn/CI_PP4_Hike-a-thon
3. Click the Code button and copy the HTTPS url, for example: https://github.com/AlexGCbn/CI_PP4_Hike-a-thon.git
4. In your IDE, open a terminal and run the git clone command, for example:
    ```git clone https://github.com/AlexGCbn/CI_PP4_Hike-a-thon.git```
5. The repository will now be cloned in your workspace
6. Create an env.py file(This file should be included in .gitignore, so it will not be commited) in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<code>import os</code>
<br><code>os.environ['SECRET_KEY'] = 'ADDED_BY_YOU'</code>
<br><code>os.environ['DATABASE_URL'] = 'ADDED_BY_YOU'</code>
<br><code>os.environ['CLOUDINARY_URL'] = 'ADDED_BY_YOU'</code>
<br>

7. Install the relevant packages as per the requirements.txt file
8. In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqllite database
9. Ensure debug is set to true in the settings.py file for local development
10. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in settings.py
11. Run "python3 manage.py showmigrations" to check the status of the migrations
12. Run "python3 manage.py migrate" to migrate the database
13. Run "python3 manage.py createsuperuser" to create a super/admin user
14. Start the application by running <code>python3 manage.py runserver</code>
15. Open the application in a web browser with the URL: http://127.0.0.1:8000/

## Heroku
This project can be deployed to Heroku with the following steps:
1. Create an account on [Heroku](https://www.heroku.com/)
2. Create an app, give it a name for example hike-a-thon, and select a region
3. Under resources search for postgres, and add a Postgres database to the app
4. Note the DATABASE_URL, this needs to be set as an environment variable in Heroku and your local environment variables
5. Create a Procfile with the text: web: gunicorn hike_a_thon.wsgi
6. Make sure you add your environment variables (env.py) to Heroku's Config Vars
7. In the settings.py ensure the connection is to the Heroku postgres database
8. Ensure debug is set to false in the settings.py file
9. Add 'localhost/127.0.0.1', and 'hike-a-thon.herokuapp.com' to the ALLOWED_HOSTS variable in settings.py
10. Run "python3 manage.py showmigrations" to check the status of the migrations
11. Run "python3 manage.py migrate" to migrate the database
12. Run "python3 manage.py createsuperuser" to create a super/admin user
13. Connect the app to GitHub, and enable automatic deploys from main
14. Click deploy to deploy your application to Heroku for the first time

# Credits
The app was created by relying on Code Institute's Django Blog walkthrough app, so a big thanks for that! 
<br>I would also like to thank my mentor, Mo Shami, for his continued support and encouragement through my course! 