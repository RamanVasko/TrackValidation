"""
Food Expiration Tracker API
FastAPI backend application for managing food products and expiration notifications
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api import auth, products, categories, notifications
from app.database.session import create_tables
from app.config import settings


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    app = FastAPI(
        title="Food Expiration Tracker API",
        description="API for managing food products and expiration notifications",
        version="1.0.0"
    )

    # Startup: Create database tables
    create_tables()

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Mount static files for product images
    app.mount("/static", StaticFiles(directory="static"), name="static")

    # Include API routers
    app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])
    app.include_router(products.router, prefix="/api/v1", tags=["Products"])
    app.include_router(categories.router, prefix="/api/v1", tags=["Categories"])
    app.include_router(notifications.router, prefix="/api/v1", tags=["Notifications"])

    @app.get("/")
    def root():
        return {"message": "Food Expiration Tracker API"}

    @app.get("/health")
    def health_check():
        return {"status": "healthy", "version": "1.0.0"}

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
