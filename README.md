# Django E-commerce API

## Project Overview
This Django project is a backend API for an e-commerce application. It provides endpoints for managing products, categories, cart items, reviews, user authentication, orders, and payment integration using Stripe.

## Features
- User authentication and management
- Product and category listing
- Cart functionality (add, update, delete items)
- Wishlist functionality (add, delete, check existence)
- Product search
- Order processing with Stripe checkout

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd project_directory
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env`:
   ```sh
   STRIPE_SECRET_KEY=your_stripe_secret_key
   WEBHOOK_SECRET=your_webhook_secret
   ```
5. Apply migrations and run the development server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

## API Endpoints

### Product Endpoints

#### Get all products
**Endpoint:** `GET /product_list`

- **Response:**
  - Returns a list of all products.

---

#### Get Product Details
**Endpoint:** `GET /products/<slug:slug>`

- **Parameters:**
  - `slug`: The unique identifier for a product.
- **Response:**
  - JSON object containing product details.

---

#### Get All Categories
**Endpoint:** `GET /category_list`

- **Response:**
  - Returns a list of all product categories.

---

#### Get Category Details
**Endpoint:** `GET /category/<slug:slug>`

- **Response:**
  - JSON object containing category details.

## Cart Management

#### Add Item to Cart
**Endpoint:** `POST /add_to_cart/`

- **Request Body:**
  ```json
  {
    "cart_code": "string",
    "product_id": <int>
  }
- **Response:**
  - Success message and updated cart item details.

#### Update Cart Item Quantity
**Endpoint:** `PUT /update_cartitem_quantity/`

- **Payload:**
  ```json
  {
    "product_id": <int>,
    "quantity": <int>
  }
  ```
- **Response:**
  - JSON with updated cart item details.

#### Delete Item from Cart
**Endpoint:** `DELETE /delete_cartitem/<int:pk>/`

- **Response:**
  - Success message if deletion is successful.

---

## Wishlist Management

#### Add/Remove Item from Wishlist
**Endpoint:** `POST /add_wishlist/`

- **Payload:**
  ```json
  {
    "product_id": <int>,
    "email": "user@example.com"
  }
  ```
- **Response:**
  - If added successfully: `201 Created`
  - If deleted: `204 No Content`

#### Check if Product is in Wishlist
**Endpoint:** `GET /product_in_wishlist`

- **Query Parameters:**
  - `email`: User's email
  - `product_id`: ID of the product to check
- **Response:**
  ```json
  {
    "exists": true/false
  }
  ```

---

## User Management

#### Create User
**Endpoint:** `POST /create_user/`

- **Payload:**
  ```json
  {
    "username": "string",
    "email": "user@example.com",
    "first_name": "string"
  }
  ```
- **Response:**
  - JSON object with user details

#### Check Existing User
**Endpoint:** `GET /existing_user?email=<email>`

- **Response:**
  ```json
  {
    "exists": true/false
  }
  ```

---

## Checkout & Orders

#### Create Checkout Session
**Endpoint:** `POST /create_checkout_session`

- **Payload:**
  ```json
  {
    "cart_code": "string",
    "email": "user@example.com"
  }
  ```
- **Response:**
  - Redirects to Stripe Checkout session URL.

#### Get Orders
**Endpoint:** `GET /get_orders`

- **Query Parameters:**
  - `email`: (string) Email of the customer
- **Response:**
  - List of order details for the user

---

## Running the Project
1. **Apply Migrations:**
   ```sh
   python manage.py migrate
   ```
2. **Create a Superuser (For Admin Access):**
   ```sh
   python manage.py createsuperuser
   ```
3. **Run Development Server:**
   ```sh
   python manage.py runserver
   ```

This will start the Django development server, and you can test the API via tools like Postman or your browser.

