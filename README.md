# URL Shortener

A Django-based URL shortener application that allows users to create shortened versions of long URLs.

## Features

- User authentication system (login, signup, logout)
- URL shortening functionality
- Password protection for shortened URLs
- reCAPTCHA integration for login and signup (configurable)
- View counter for shortened URLs
- User-specific URL management
- Random short URL generation
- Handling of duplicate short URLs
- Redirection to original URL

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/msabry1/url-shortener.git
   cd url-shortener
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Django project settings, including database configuration and secret key.

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

1. Navigate to the homepage to create shortened URLs.
2. Sign up or log in to manage your shortened URLs.
3. Enter a long URL to get a shortened version.
4. Optionally set a password for the shortened URL.
5. Share the shortened URL.

## Configuration

- reCAPTCHA: 
  - Set `RECAPTCHA_SITE_KEY` and `RECAPTCHA_SECRET_KEY` in your settings.
  - Configure `RECAPTCHA_LOGIN` and `RECAPTCHA_SIGNUP` to enable/disable reCAPTCHA for login and signup.
