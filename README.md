# A.P. TECHNOCARE

**Industrial Supplier & Service Provider Website**

A.P. TECHNOCARE is a Django-based business website and administration
system for an industrial supplier and service provider. It includes a
product catalog, business enquiry management, contact messages,
quotations, and a customized Django admin dashboard powered by Jazzmin.

## Features

### Product catalog

-   Product, category and brand management
-   Product applications and specifications
-   Product images and documents
-   Product pricing visibility and availability management
-   Featured and active product management
-   SEO-related catalog fields

### Enquiries and quotations

-   Customer enquiries and enquiry items
-   Enquiry status tracking and staff assignment
-   Contact message management
-   Quotations and quotation line items
-   Quotation status, totals, tax and validity information

### Administration

-   Django admin customized with Jazzmin
-   Business dashboard with catalog, enquiry and quotation statistics
-   Recent enquiries and today's activity
-   Quick links to common administration pages

### Other components

-   Split Django settings, including `config.settings.development`
-   Static and media file configuration
-   Django REST Framework, django-filter and django-htmx in the project
    configuration

## Technology stack

-   Python 3.12
-   Django (development environment reported as 6.1.1)
-   Jazzmin
-   Django REST Framework
-   django-filter
-   django-htmx
-   WhiteNoise
-   SQLite as the default development database

Check the dependency files and settings for exact package versions and
deployment configuration.

## Project structure

``` text
A.P. TECHNOCARE/
├── apps/
│   ├── catalog/
│   ├── core/
│   ├── enquiries/
│   ├── content/
│   ├── seo/
│   └── analytics/
├── config/
│   └── settings/
│       ├── base.py
│       └── development.py
├── templates/
│   └── admin/
│       └── index.html
├── manage.py
└── README.md
```

This is an overview of the main application areas; additional files and
folders may exist.

## Getting started

### 1. Clone the repository

Replace `YOUR_GITHUB_USERNAME` with the GitHub account that owns the
repository.

``` bash
git clone https://github.com/YOUR_GITHUB_USERNAME/A.P.-TECHNOCARE.git
cd A.P.-TECHNOCARE
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

``` powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

``` bat
.venv\Scripts\activate.bat
```

**macOS / Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If the repository contains `requirements.txt`, run:

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If dependencies are managed using another file or tool, follow that
project's instructions.

### 4. Configure environment variables

The project uses `django-environ`. Review `config/settings/base.py` and
configure the environment variables required by the project.

For local development: - Use a private development `SECRET_KEY`. - Keep
`DEBUG=True` only in local development settings. - Do not commit `.env`
files, passwords, API keys or production secrets. - Configure database
and other environment-specific values as required by the settings.

Never put production credentials in a public repository.

### 5. Apply database migrations

``` bash
python manage.py migrate --settings=config.settings.development
```

### 6. Create an administrator account

``` bash
python manage.py createsuperuser --settings=config.settings.development
```

Follow the prompts to create the admin user.

### 7. Run the development server

``` bash
python manage.py runserver --settings=config.settings.development
```

Open:

-   Website: http://127.0.0.1:8000/
-   Django admin: http://127.0.0.1:8000/admin/

The admin dashboard requires a user with appropriate admin access.

## Useful development commands

Run Django's system check:

``` bash
python manage.py check --settings=config.settings.development
```

Create migrations after model changes:

``` bash
python manage.py makemigrations --settings=config.settings.development
```

Apply migrations:

``` bash
python manage.py migrate --settings=config.settings.development
```

Collect static files when preparing for deployment:

``` bash
python manage.py collectstatic --settings=config.settings.development
```

Use production-specific settings for deployment. Do not deploy with
development settings or `DEBUG=True`.

## Security notes

-   Never commit `.env`, secret keys, passwords, tokens or private
    customer information.
-   Keep local databases and private uploaded media out of Git unless
    there is a deliberate, secure reason to version them.
-   Use a strong, environment-provided `SECRET_KEY` in production.
-   Set `DEBUG=False` in production.
-   Configure `ALLOWED_HOSTS`, HTTPS, database credentials, static files
    and media storage for the deployment environment.
-   Review staff and superuser permissions before giving employees admin
    access.
-   Back up production data regularly.

## Contributing

1.  Create a branch for your change.
2.  Make the change and run the Django system check.
3.  Test the affected functionality.
4.  Commit with a descriptive message.
5.  Push the branch and open a pull request.

## License

No license has been specified yet. Unless a license is added to this
repository, treat the project as proprietary and all rights reserved.

------------------------------------------------------------------------

**A.P. TECHNOCARE**\
*Lets Grow Together*
