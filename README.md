<!-- # Django E-commerce API

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
    "first_name": "string",
    "profile_picture_url": "string"
  }
  ```
- **Response:**
  - JSON object with user details

#### Check Existing User
**Endpoint:** `GET /existing_user/<str:email>`

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
 -->
---

<!-- ```markdown -->
# Django E-commerce API

## Project Overview
This Django project is a backend API for an e-commerce application. It provides endpoints for managing products, categories, cart items, reviews, user authentication, orders, and payment integration using Stripe.

🚀 **Live API Base URL:** [https://ytecommerceapi2025-production.up.railway.app](https://ytecommerceapi2025-production.up.railway.app)

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

---

# 🛍️ E-commerce API Documentation

This API supports a basic e-commerce platform with features like product listing, cart management, reviews, wishlist, checkout, and user management.

---

## 📦 Products

### `GET /product_list`
- **Description**: Get all featured products.
- **Response**:
```json
[
  {
    "id": 1,
    "name": "Product A",
    "price": 100,
    ...
  }
]
```

### `GET /products/<slug:slug>`
- **Description**: Get detailed info about a specific product.
- **Response**:
```json
{
  "id": 1,
  "name": "Product A",
  "description": "...",
  ...
}
```

---

## 🧩 Categories

### `GET /category_list`
- **Description**: Get all product categories.
- **Response**:
```json
[
  {
    "id": 1,
    "name": "Electronics",
    ...
  }
]
```

### `GET /categories/<slug:slug>`
- **Description**: Get details of a specific category.
- **Response**:
```json
{
  "id": 1,
  "name": "Electronics",
  ...
}
```

---

## 🛒 Cart

### `POST /add_to_cart/`
- **Payload**:
```json
{
  "cart_code": "abc123",
  "product_id": 5
}
```
- **Response**: Returns the updated cart.

### `PUT /update_cartitem_quantity/`
- **Payload**:
```json
{
  "item_id": 3,
  "quantity": 2
}
```
- **Response**:
```json
{
  "data": { ... },
  "message": "Cartitem updated successfully!"
}
```

### `GET /get_cart/<cart_code>`
- **Description**: Retrieve full cart details using `cart_code`.

### `GET /get_cart_stat?cart_code=abc123`
- **Description**: Get cart subtotal and item count.

### `DELETE /delete_cartitem/<int:pk>/`
- **Response**: 
```text
"Cartitem deleted successfully!"
```

### `GET /product_in_cart?cart_code=abc123&product_id=5`
- **Response**:
```json
{
  "product_in_cart": true
}
```

---

## 📝 Reviews

### `POST /add_review/`
- **Payload**:
```json
{
  "product_id": 5,
  "email": "user@example.com",
  "rating": 4,
  "review": "Great product!"
}
```
- **Response**: Review data or error if review already exists.

### `PUT /update_review/<int:pk>/`
- **Payload**:
```json
{
  "rating": 5,
  "review": "Updated review text"
}
```
- **Response**: Updated review object.

### `DELETE /delete_review/<int:pk>/`
- **Response**:
```text
"Review deleted successfully!"
```

---

## 💖 Wishlist

### `POST /add_to_wishlist/`
- **Payload**:
```json
{
  "email": "user@example.com",
  "product_id": 5
}
```
- **Response**: Wishlist item or `204` if already existed and now deleted.

### `GET /my_wishlists?email=user@example.com`
- **Response**: List of wishlisted items.

### `GET /product_in_wishlist?email=user@example.com&product_id=5`
- **Response**:
```json
{
  "product_in_wishlist": true
}
```

---

## 🔍 Search

### `GET /search?query=phone`
- **Response**: List of matching products.

---

## 💳 Checkout

### `POST /create_checkout_session/`
- **Payload**:
```json
{
  "cart_code": "abc123",
  "email": "user@example.com"
}
```
- **Response**:
```json
{
  "data": {
    "id": "cs_test_xxx",
    ...
  }
}
```

### `POST /webhook/`
- **Stripe webhook**: Handles payment events and fulfills order.
- **No payload from client**.

---

## 👤 User

### `POST /create_user/`
- **Payload**:
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "profile_picture_url": "https://example.com/image.jpg"
}
```
- **Response**: Created user data.

### `GET /existing_user/<email>`
- **Response**:
```json
{
  "exists": true
}
```

---

## 📦 Orders

### `GET /get_orders?email=user@example.com`
- **Response**: List of orders for the user.

---

## 🏠 Address

### `POST /add_address/`
- **Payload**:
```json
{
  "email": "user@example.com",
  "street": "123 Street",
  "state": "Lagos",
  "city": "Cityname",
  "phone": "123456789"
}
```
- **Response**: Created or updated address.

### `GET /get_address?email=user@example.com`
- **Response**:
```json
{
  "email": "user@example.com",
  "street": "123 Street",
  ...
}
```

---

---

# 🚀 Django SQLite → PostgreSQL Migration Workflow

**1. Install PostgreSQL driver:**
```bash
pip install psycopg2-binary
```

**2. Dump existing data from SQLite:**
```bash
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > data.json
```

**3. (Optional) Ensure `data.json` is UTF-8 encoded:**
- If you get a `UnicodeDecodeError` later:
  - Open `data.json` in VS Code.
  - Click the encoding at the bottom bar (or `File > Save with Encoding > UTF-8`).
  - Save the file again as **UTF-8**.

**4. Create PostgreSQL database and user.**

**5. Update `settings.py` to use PostgreSQL:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**6. Run database migrations:**
```bash
python manage.py migrate
```

**7. Load dumped data into PostgreSQL:**
```bash
python manage.py loaddata data.json
```

**8. Test your application thoroughly.**

---
