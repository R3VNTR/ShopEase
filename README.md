# ShopEase
ShopEase: Your one-stop online destination for effortless shopping, offering a wide range of products at unbeatable prices with fast and reliable delivery.

## Installation Guide

Follow these steps to set up and run this Django project locally.

### Prerequisites

- Python 3.12
- pip 

### Step 1: Clone the Repository
git clone https://github.com/R3VNTR/ShopEase.git

cd ShopEase

### Step 2: Set Up a Virtual Environment
python3 -m venv venv    or     python -m venv venv


source venv/bin/activate  

On Windows use `source venv\Scripts\activate`

### Step 3: Install Dependencies
pip install -r requirements.txt

## Step 4: Create the .env File
cd ShopEase

touch .env

Check .env.example for understand the structure and fill .env file

### Step 5: Set Up the Database
python manage.py migrate

### Step 6: Create a Superuser
python manage.py createsuperuser

### Step 7: Run the Development Server
python manage.py runserver


# Admin Tasks:

Add Categories: Admins must add categories at http://127.0.0.1:8000/admin/.

Update User Roles: After a user has registered, the admin can update the user to a seller by navigating to the "User Profiles" section, selecting the user, and checking the "Is Seller" box.

Seller Actions: Once a user is set as a seller, they can go to their profile and add new products. Users who are not sellers can only buy products.

# User Profile Management:

Profile Updates: Users can update their profile information, except for the "Is Seller" box, which can only be modified by an admin.


# Tasks
    Setup and Configuration
        DONE - Create Virtual Machine (VM)
        DONE - Install and set up the environment
        DONE - Initialize database, create superuser, and run initial tests

    Application Development

        DONE - Create core app for base pages
            DONE - Implement front page to list newest products
            DONE - Implement about us
        DONE - Develop user profiles app (Handle vendors, buyers, )
            DONE - Add UserProfile model
            DONE - Create My account view for filtering products, pending orders and user profile update
            DONE - Implement vendor detail page to showcase vendor-specific products and information
        DONE - Create store app for Product, Category management and Search handling
            DONE - Add product model 
            DONE - Add category model 
        DONE - Create order app for Buyers order handling
            DONE - Add Order model 
            DONE - Add Order_item model 
        DONE - Create cart app for cart function handling
        DONE - Create conversation('covertion') app for conversation function between sellers and buyers
            DONE - Add Conversation model 
            DONE - Add ConversationMessage model 

    User Authentication

        DONE - Implement sign-up functionality
        DONE - Develop log-in and log-out functionality

    Product and Order Management

        DONE - Implement add-to-cart functionality
        DONE - Manage orders from the 'My Account' page
        DONE - Develop cart view for users to review selected products
        DONE - Create checkout process, including payment and shipping details

    Administrative Features

        DONE - Develop admin pages for Products, Orders, User profiles management

    Payment Integration

        DONE - Integrate payment gateway (Stripe) for processing transactions

    Deployment
             - Deploy project to production
