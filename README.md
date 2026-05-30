# Product Search API

## Overview

A Django REST Framework backend application that provides product search, filtering, inventory management, and order processing functionality.

The project includes advanced product search capabilities, store inventory management, Redis caching, Celery task integration, Docker support, and automated tests.

---

## Features

### Product Search

* Keyword search
* Category filtering
* Minimum price filtering
* Maximum price filtering
* Store-based filtering
* In-stock filtering
* Sorting by price and title
* Pagination support

### Product Suggestions

* Auto-suggestion endpoint for product names

### Inventory Management

* Store inventory tracking
* Product quantity management

### Order Management

* Create orders
* Inventory validation
* Automatic stock deduction
* Order status management

### Performance Features

* Redis caching
* Celery asynchronous task processing

### DevOps

* Docker support
* Docker Compose support

### Testing

* Automated unit tests

---

## Tech Stack

* Python 3
* Django
* Django REST Framework
* SQLite
* Redis
* Celery
* Docker

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd aforro-backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

---

## Docker Setup

Build and run:

```bash
docker-compose up --build
```

---

## Running Tests

```bash
python manage.py test
```

---

## API Endpoints

### Search Products

```http
GET /api/search/products/
```

Examples:

```http
/api/search/products/?q=iphone

/api/search/products/?category=Electronics

/api/search/products/?min_price=1000

/api/search/products/?max_price=60000

/api/search/products/?store=1

/api/search/products/?in_stock=true

/api/search/products/?sort=price

/api/search/products/?sort=-price
```

### Product Suggestions

```http
GET /api/search/suggest/?q=iph
```

### Store Inventory

```http
GET /api/stores/<store_id>/
```

### Create Order

```http
POST /api/orders/
```

### Store Orders

```http
GET /api/orders/store/<store_id>/
```

---

## Redis Cache

Redis is configured for caching frequently accessed data.

---

## Celery Tasks

Celery is configured for asynchronous task execution.

Example task:

* process_order(order_id)

Run worker:

```bash
celery -A config worker --loglevel=info
```

---

## Scalability Considerations

* Pagination for large datasets
* Redis caching for performance
* Celery background processing
* Modular application architecture
* Dockerized deployment support


## Screenshots

Project screenshots demonstrating:

- Django Admin Panel
- Product & Category Management
- Store & Inventory Management
- Product Search API
- Order Processing API

are available in the `/screenshots` folder.
