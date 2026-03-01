<div align="center">

# 🚗 Jinete Riders

### Modern Ride Booking Platform

[![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com/)

[Live Demo](https://jinete-riders.herokuapp.com/) · [API Documentation](https://documenter.getpostman.com/view/14121536/UV5f6t9J) · [Report Bug](https://github.com/yourusername/jinete-riders/issues)

</div>

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 About The Project

**Jinete Riders** is a comprehensive ride-booking platform designed for seamless urban transportation. Built with Django REST Framework, it provides a robust backend API for connecting passengers with drivers, managing rides, and processing secure payments.

The platform features separate portals for passengers and drivers, real-time ride matching, integrated payment processing via Razorpay, and automated email notifications through SendGrid.

### Why Jinete Riders?

- **Scalable Architecture**: Built on Django with RESTful API design principles
- **Secure Authentication**: JWT-based authentication with token management
- **Payment Integration**: Secure payment processing with Razorpay
- **Email Automation**: Password reset and notifications via SendGrid
- **Production Ready**: Deployed on Heroku with PostgreSQL database
- **Well Documented**: Comprehensive API documentation via Postman

---

## ✨ Key Features

### For Passengers
- ✅ User registration and authentication
- ✅ Profile management with ratings
- ✅ Book rides with source and destination
- ✅ Real-time ride status tracking
- ✅ Rate drivers after ride completion
- ✅ Secure payment processing
- ✅ Password reset via email

### For Drivers
- ✅ Driver registration with vehicle details
- ✅ Profile management including license information
- ✅ Accept or reject ride requests
- ✅ Update ride status in real-time
- ✅ Rate passengers after ride completion
- ✅ View earnings and ride history

### System Features
- ✅ JWT token-based authentication
- ✅ Role-based access control (Passenger/Driver)
- ✅ Automated email notifications
- ✅ Payment order creation and verification
- ✅ Rating system for both passengers and drivers
- ✅ RESTful API architecture
- ✅ CORS support for frontend integration

---

## 🛠️ Tech Stack

### Backend Framework
- **Django 3.1.14** - High-level Python web framework
- **Django REST Framework 3.12.4** - Powerful toolkit for building Web APIs

### Database
- **PostgreSQL** - Production database
- **SQLite** - Development database
- **psycopg2 2.8.6** - PostgreSQL adapter for Python

### Authentication & Security
- **PyJWT 2.3.0** - JSON Web Token implementation
- **bcrypt 3.2.0** - Password hashing
- **django-cors-headers 3.10.0** - CORS handling

### Third-Party Services
- **Razorpay 1.2.0** - Payment gateway integration
- **SendGrid 6.9.7** - Email delivery service

### Deployment & Production
- **Gunicorn 20.1.0** - WSGI HTTP Server
- **WhiteNoise 5.3.0** - Static file serving
- **django-heroku 0.3.1** - Heroku configuration
- **dj-database-url 0.5.0** - Database URL parsing

### Development Tools
- **python-decouple 3.5** - Environment variable management
- **autopep8 1.5.7** - Code formatting

---

## 📁 Project Structure

```
jinete-riders/
├── api/                          # Main API application
│   ├── driver/                   # Driver management module
│   │   ├── models.py            # Driver & Token models
│   │   ├── views.py             # Driver endpoints
│   │   ├── serializers.py       # Data serialization
│   │   └── urls.py              # Driver routes
│   ├── passenger/               # Passenger management module
│   │   ├── models.py            # Passenger & Token models
│   │   ├── views.py             # Passenger endpoints
│   │   ├── serializers.py       # Data serialization
│   │   └── urls.py              # Passenger routes
│   ├── ride/                    # Ride management module
│   │   ├── models.py            # Ride model
│   │   ├── views_driver.py      # Driver ride operations
│   │   ├── views_passenger.py   # Passenger ride operations
│   │   └── urls.py              # Ride routes
│   ├── order/                   # Payment & order module
│   │   ├── models.py            # Order model
│   │   ├── views.py             # Payment endpoints
│   │   └── urls.py              # Order routes
│   ├── middleware/              # Custom middleware
│   │   └── auth_strategy.py     # Authentication middleware
│   └── utils/                   # Utility modules
│       ├── mailer.py            # Email functionality
│       ├── payment_status_constants.py
│       └── ride_type_constants.py
├── jinete/                      # Project configuration
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Root URL configuration
│   └── wsgi.py                  # WSGI configuration
├── templates/                   # HTML templates
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── Procfile                     # Heroku deployment config
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **PostgreSQL** - [Download PostgreSQL](https://www.postgresql.org/download/) (for production)
- **Git** - [Download Git](https://git-scm.com/downloads)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/jinete-riders.git
   cd jinete-riders
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   touch .env
   ```
   
   See [Environment Variables](#environment-variables) section for required variables.

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - API Base: `http://localhost:8000/api/`
   - Admin Panel: `http://localhost:8000/admin/`

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add the following variables:

```env
# Django Configuration
SECRET_KEY=your-django-secret-key-here
ENVIRONMENT=dev  # 'dev' for development, 'production' for production

# JWT Authentication
ACCESS_SECRET_TOKEN=your-jwt-secret-token-here

# Password Encryption
BCRYPT_SALT=your-bcrypt-salt-value-here

# SendGrid Email Configuration
SENDGRID_API_KEY=your-sendgrid-api-key
PASSWORD_RESET_EMAIL_TEMPLATE_ID=your-sendgrid-template-id
FROM_EMAIL=noreply@yourdomain.com

# Database (Production)
DATABASE_URL=postgresql://user:password@localhost:5432/jinete_db

# Razorpay Payment Gateway
RAZOR_KEY_ID=your-razorpay-key-id
RAZOR_KEY_SECRET=your-razorpay-secret-key
```

### Environment Variable Details

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Django secret key for cryptographic signing | ✅ Yes |
| `ENVIRONMENT` | Environment mode (`dev` or `production`) | ✅ Yes |
| `ACCESS_SECRET_TOKEN` | Secret key for JWT token generation | ✅ Yes |
| `BCRYPT_SALT` | Salt value for password encryption | ✅ Yes |
| `SENDGRID_API_KEY` | SendGrid API key for email services | ✅ Yes |
| `PASSWORD_RESET_EMAIL_TEMPLATE_ID` | SendGrid template ID for password reset emails | ✅ Yes |
| `FROM_EMAIL` | Sender email address for notifications | ✅ Yes |
| `DATABASE_URL` | PostgreSQL database connection URL | ✅ Yes (Production) |
| `RAZOR_KEY_ID` | Razorpay API key ID | ✅ Yes |
| `RAZOR_KEY_SECRET` | Razorpay API secret key | ✅ Yes |

### Generating Secret Keys

```python
# Generate Django SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Generate ACCESS_SECRET_TOKEN
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## 📖 Usage

### Running the Development Server

```bash
# Standard development server
python manage.py runserver

# Run on a specific port
python manage.py runserver 8080

# Run on all network interfaces
python manage.py runserver 0.0.0.0:8000
```

### Database Operations

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (⚠️ deletes all data)
python manage.py flush

# Create database backup
python manage.py dumpdata > backup.json

# Load database backup
python manage.py loaddata backup.json
```

### Admin Operations

```bash
# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run Django shell
python manage.py shell
```

---

## 🔌 API Endpoints

### Authentication

Both passengers and drivers have separate authentication endpoints.

#### Passenger Endpoints
- `POST /api/passenger/register/` - Register new passenger
- `POST /api/passenger/login/` - Passenger login
- `POST /api/passenger/logout/` - Passenger logout
- `POST /api/passenger/forgot-password/` - Request password reset
- `GET /api/passenger/profile/` - Get passenger profile
- `PUT /api/passenger/profile/` - Update passenger profile

#### Driver Endpoints
- `POST /api/driver/register/` - Register new driver
- `POST /api/driver/login/` - Driver login
- `POST /api/driver/logout/` - Driver logout
- `POST /api/driver/forgot-password/` - Request password reset
- `GET /api/driver/profile/` - Get driver profile
- `PUT /api/driver/profile/` - Update driver profile

### Ride Management

#### Passenger Ride Operations
- `POST /api/ride/create/` - Create new ride request
- `GET /api/ride/passenger/rides/` - Get all passenger rides
- `GET /api/ride/passenger/:id/` - Get specific ride details
- `POST /api/ride/passenger/:id/rate/` - Rate driver after ride
- `DELETE /api/ride/passenger/:id/cancel/` - Cancel ride

#### Driver Ride Operations
- `GET /api/ride/driver/available/` - Get available ride requests
- `POST /api/ride/driver/:id/accept/` - Accept ride request
- `POST /api/ride/driver/:id/reject/` - Reject ride request
- `PUT /api/ride/driver/:id/status/` - Update ride status
- `GET /api/ride/driver/rides/` - Get all driver rides
- `POST /api/ride/driver/:id/rate/` - Rate passenger after ride

### Payment & Orders

- `POST /api/order/create/` - Create payment order
- `POST /api/order/verify/` - Verify payment signature
- `GET /api/order/:id/` - Get order details

### Complete API Documentation

For detailed API documentation including request/response schemas, authentication headers, and example requests, visit:

**[Postman API Documentation](https://documenter.getpostman.com/view/14121536/UV5f6t9J)**

---

## 🗄️ Database Schema

### Core Models

#### Passenger Model
```python
- id (AutoField)
- name (CharField)
- email (CharField, Unique)
- phone (CharField)
- password (CharField, Hashed)
- city (CharField)
- country (CharField)
- profile_image (CharField, Optional)
- rating (FloatField, 0-5)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

#### Driver Model
```python
- id (AutoField)
- name (CharField)
- email (CharField, Unique)
- phone (CharField)
- password (CharField, Hashed)
- city (CharField)
- country (CharField)
- profile_image (CharField, Optional)
- rating (FloatField, 0-5)
- car_name (CharField)
- car_number (CharField)
- car_image (CharField)
- driving_license_no (CharField)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

#### Ride Model
```python
- id (AutoField)
- driver (ForeignKey → Driver, Nullable)
- passenger (ForeignKey → Passenger, Nullable)
- source (CharField)
- destination (CharField)
- total_cost (IntegerField)
- estimated_time (IntegerField, minutes)
- driver_rating (FloatField, 0-5)
- passenger_rating (FloatField, 0-5)
- ride_status (IntegerField, Choices)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

#### Order Model
```python
- id (AutoField)
- ride (ForeignKey → Ride, Nullable)
- order_id (CharField)
- payment_id (CharField, Optional)
- signature (CharField, Optional)
- price (FloatField)
- payment_status (CharField, Choices)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### Entity Relationships

```
Passenger 1──────* Token
Driver 1─────────* Token
Passenger 1──────* Ride
Driver 1─────────* Ride
Ride 1───────────1 Order
```

---

## 🚢 Deployment

### Heroku Deployment

This project is configured for Heroku deployment with the following files:

- `Procfile` - Defines process types and commands
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version (optional)

#### Deploy to Heroku

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Windows (use installer from heroku.com)
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Add PostgreSQL addon**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

5. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set ACCESS_SECRET_TOKEN=your-jwt-token
   heroku config:set SENDGRID_API_KEY=your-sendgrid-key
   # ... set all other environment variables
   ```

6. **Deploy the application**
   ```bash
   git push heroku main
   ```

7. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   ```

8. **Create superuser**
   ```bash
   heroku run python manage.py createsuperuser
   ```

### Docker Deployment (Optional)

<details>
<summary>Click to expand Docker instructions</summary>

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "jinete.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Build and run:

```bash
docker build -t jinete-riders .
docker run -p 8000:8000 --env-file .env jinete-riders
```

</details>

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test api.passenger
python manage.py test api.driver
python manage.py test api.ride
python manage.py test api.order

# Run with verbosity
python manage.py test --verbosity=2

# Run with coverage (install coverage first: pip install coverage)
coverage run --source='.' manage.py test
coverage report
coverage html
```

### Test Structure

Place tests in the `tests.py` file within each app:
- `api/passenger/tests.py` - Passenger module tests
- `api/driver/tests.py` - Driver module tests
- `api/ride/tests.py` - Ride module tests
- `api/order/tests.py` - Order module tests

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Code Style Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Write unit tests for new features
- Update documentation for API changes

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Contact

**Project Maintainer**: Your Name

- 📧 Email: your.email@example.com
- 🌐 Portfolio: [yourportfolio.com](https://yourportfolio.com)
- 💼 LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- 🐙 GitHub: [@yourusername](https://github.com/yourusername)

**Project Link**: [https://github.com/yourusername/jinete-riders](https://github.com/yourusername/jinete-riders)

**Live Demo**: [https://jinete-riders.herokuapp.com/](https://jinete-riders.herokuapp.com/)

---

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
- [Django REST Framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building Web APIs
- [Razorpay](https://razorpay.com/) - Payment gateway integration
- [SendGrid](https://sendgrid.com/) - Email delivery service
- [Heroku](https://www.heroku.com/) - Cloud platform for deployment
- [PostgreSQL](https://www.postgresql.org/) - Advanced open source database

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

Made with ❤️ using Django

</div>
