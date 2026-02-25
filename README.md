# Food Expiration Tracker

A comprehensive mobile application for tracking food products and managing expiration dates with automated notifications.

## Features

### Core Functionality
- ✅ **Product Management**: Add, edit, and delete food products
- ✅ **Barcode Scanning**: Scan barcodes to automatically add product information
- ✅ **Expiration Tracking**: Track expiration dates and receive timely notifications
- ✅ **Categories**: Organize products into customizable categories
- ✅ **Manual Entry**: Add products manually with full control over details

### Notification System
- ✅ **Email Notifications**: Receive email alerts 3 days before expiration
- ✅ **Push Notifications**: Get mobile push notifications for expiring products
- ✅ **Customizable Settings**: Configure notification preferences per user
- ✅ **Automated Scheduler**: Background service sends notifications automatically

### Product Details
- ✅ **Product Name**: Name of the food item
- ✅ **Shop Information**: Where and when the product was purchased
- ✅ **Expiration Date**: Track when the product expires
- ✅ **Quantity Tracking**: Amount in kg, liters, pieces, etc.
- ✅ **Photo Upload**: Add images of products
- ✅ **Notes**: Additional information about the product

## Tech Stack

### Backend (FastAPI)
- **Framework**: FastAPI with async support
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens with refresh mechanism
- **Notifications**: Email (SMTP) and Push (Firebase)
- **API Documentation**: Automatic OpenAPI/Swagger docs

### Frontend (React Native)
- **Framework**: React Native with Expo
- **State Management**: Redux Toolkit
- **Navigation**: React Navigation
- **UI Components**: Native base components
- **Barcode Scanning**: react-native-camera integration

## Project Structure

```
food-tracker/
├── backend/                    # FastAPI backend application
│   ├── app/
│   │   ├── main.py            # Application entry point
│   │   ├── config.py          # Configuration settings
│   │   ├── models/            # Database models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── api/               # API endpoints
│   │   ├── services/          # Business logic
│   │   ├── utils/             # Utility functions
│   │   └── database/          # Database configuration
│   ├── requirements.txt       # Python dependencies
│   └── alembic/               # Database migrations
├── frontend/                   # React Native mobile app
│   ├── src/
│   │   ├── screens/           # App screens/components
│   │   ├── components/        # Reusable components
│   │   ├── store/             # Redux store and slices
│   │   ├── services/          # API services
│   │   └── utils/             # Utility functions
│   ├── App.tsx                # App entry point
│   └── package.json           # Node.js dependencies
├── docs/                      # Documentation
│   ├── ARCHITECTURE.md        # System architecture
│   ├── API.md                 # API documentation
│   └── DEPLOYMENT.md          # Deployment guide
└── README.md                  # This file
```

## Installation

### Backend Setup

1. **Install Python dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the backend directory:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/food_tracker
   SECRET_KEY=your-secret-key-change-in-production
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   EMAIL_FROM=noreply@foodtracker.com
   ```

3. **Run database migrations:**
   ```bash
   alembic upgrade head
   ```

4. **Start the server:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Install Node.js dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm start
   ```

3. **Run on device/simulator:**
   ```bash
   # For iOS
   npm run ios
   
   # For Android
   npm run android
   ```

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Token refresh
- `GET /api/v1/auth/me` - Get current user
- `PUT /api/v1/auth/me` - Update user profile

### Products
- `GET /api/v1/products` - Get all products
- `GET /api/v1/products/{id}` - Get specific product
- `POST /api/v1/products` - Create new product
- `PUT /api/v1/products/{id}` - Update product
- `DELETE /api/v1/products/{id}` - Delete product
- `GET /api/v1/products/expiring` - Get expiring products
- `POST /api/v1/products/scan` - Scan barcode

### Categories
- `GET /api/v1/categories` - Get all categories
- `POST /api/v1/categories` - Create category

### Notifications
- `GET /api/v1/notifications` - Get user notifications
- `POST /api/v1/notifications/test` - Test notifications
- `GET /api/v1/settings` - Get user settings
- `PUT /api/v1/settings` - Update user settings

## Database Schema

The application uses PostgreSQL with the following main tables:

- **users**: User accounts and authentication
- **products**: Food product information
- **categories**: Product categorization
- **notifications**: Sent notification records
- **user_settings**: User notification preferences

## Notification System

The application includes an automated notification system that:

1. **Runs hourly** to check for expiring products
2. **Sends email notifications** 3 days before expiration
3. **Sends push notifications** for mobile users
4. **Respects user preferences** for notification types
5. **Logs all notifications** for tracking and debugging

## Development

### Code Style
- Backend: Follow PEP 8 with Black formatter
- Frontend: Use ESLint and Prettier for consistent formatting
- Use type hints throughout the codebase

### Testing
- Backend: Use pytest with pytest-asyncio
- Frontend: Use Jest with React Native Testing Library
- API: Test with Postman or curl

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Deployment

### Backend Deployment
- Use Docker containers for production
- Deploy to cloud platforms (AWS, GCP, Azure)
- Use environment-specific configuration
- Set up monitoring and logging

### Frontend Deployment
- Build production APK/IPA files
- Deploy to app stores
- Use CI/CD for automated builds

## Security

- JWT authentication with secure tokens
- Password hashing with bcrypt
- Input validation and sanitization
- HTTPS enforcement in production
- Rate limiting on API endpoints

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue on GitHub
- Join our Discord community
- Email us at support@foodtracker.com

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.