# LiquidRound Django Application

**Bringing liquidity to the crowd** - A modern Django 5.2.5 application for crowdfunding and investment platforms.

## 🚀 Major Upgrade Completed (September 2025)

This application has been successfully upgraded from Django 1.9.1 (2016) to Django 5.2.5 (latest) with modern best practices and styling.

### ✅ Upgrade Highlights

- **Django 5.2.5**: Latest stable version with all security updates
- **Tailwind CSS 4.x**: Modern, responsive UI framework
- **SQLite Database**: Easy development and deployment
- **Python 3.11**: Modern Python with latest features
- **WhiteNoise**: Efficient static file serving
- **Modern Dependencies**: All packages updated to latest versions

## 📋 Requirements

- Python 3.11+
- Node.js 20+ (for Tailwind CSS)
- Git

## 🛠 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kaljuvee/liquidround-django.git
cd liquidround-django
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
cd liquidround
pip install -r requirements.txt
```

### 4. Install Node.js Dependencies (for Tailwind CSS)

```bash
cd ..  # Back to project root
npm install
```

### 5. Build Tailwind CSS

```bash
npm run build-css-prod
```

### 6. Setup Database

```bash
cd liquidround
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see the application!

## 🌐 Deployment

### Local Development

The application is configured for local development with SQLite database and Django's development server.

### Render.com Deployment

The application is ready for deployment on Render.com:

1. **Create a new Web Service** on Render.com
2. **Connect your GitHub repository**
3. **Configure build settings**:
   - **Build Command**: `cd liquidround && pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `cd liquidround && python manage.py runserver 0.0.0.0:$PORT`
   - **Environment**: Python 3.11

4. **Set Environment Variables**:
   ```
   DJANGO_SETTINGS_MODULE=core.settings.production
   DEBUG=False
   SECRET_KEY=your-secret-key-here
   ```

5. **Deploy**: Render will automatically build and deploy your application

### Production Settings

For production deployment, create `liquidround/core/settings/production.py`:

```python
from .base import *
import os

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['your-domain.com', 'your-app.onrender.com']

# Database for production (if using PostgreSQL)
# DATABASES = {
#     'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
# }

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## 📁 Project Structure

```
liquidround-django/
├── liquidround/                 # Main Django project
│   ├── core/                   # Project settings and configuration
│   │   ├── settings/          # Environment-specific settings
│   │   └── static/css/        # Tailwind CSS files
│   ├── accounts/              # User accounts and profiles
│   ├── companies/             # Company management
│   ├── listings/              # Investment listings
│   ├── msgs/                  # Messaging system
│   ├── news/                  # News and updates
│   ├── statpages/             # Static pages
│   ├── admindeck/             # Admin dashboard
│   ├── templates/             # HTML templates
│   ├── manage.py              # Django management script
│   └── requirements.txt       # Python dependencies
├── package.json               # Node.js dependencies
├── tailwind.config.js         # Tailwind CSS configuration
└── README.md                  # This file
```

## 🎨 Frontend Technologies

- **Tailwind CSS 4.x**: Utility-first CSS framework
- **Responsive Design**: Mobile-first approach
- **Custom Components**: LiquidRound-specific styling
- **Modern JavaScript**: ES6+ features

## 🔧 Development

### Running Tests

```bash
cd liquidround
python manage.py test
```

### Creating Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files

```bash
python manage.py collectstatic
```

### Building CSS (Development)

```bash
npm run build-css-dev
```

### Building CSS (Production)

```bash
npm run build-css-prod
```

## 📦 Dependencies

### Python Packages (requirements.txt)

- **Django 5.2.5**: Web framework
- **Pillow**: Image processing
- **django-imagekit**: Image optimization
- **django-cors-headers**: CORS handling
- **whitenoise**: Static file serving
- **python-decouple**: Environment configuration

### Node.js Packages

- **tailwindcss**: CSS framework
- **@tailwindcss/forms**: Form styling
- **@tailwindcss/typography**: Typography plugin

## 🔒 Security Features

- **Django 5.2.5 Security**: Latest security patches
- **CSRF Protection**: Built-in CSRF middleware
- **SQL Injection Protection**: Django ORM
- **XSS Protection**: Template auto-escaping
- **Secure Headers**: Security middleware

## 🐛 Troubleshooting

### Common Issues

1. **Static files not loading**: Run `python manage.py collectstatic`
2. **CSS not updating**: Rebuild Tailwind with `npm run build-css-dev`
3. **Database errors**: Run `python manage.py migrate`
4. **Import errors**: Check virtual environment activation

### Getting Help

- Check Django 5.2.5 documentation
- Review Tailwind CSS documentation
- Check GitHub issues for this repository

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review the upgrade notes

---

**Last Updated**: September 2025  
**Django Version**: 5.2.5  
**Python Version**: 3.11+  
**Status**: ✅ Production Ready

