"""
Notification utilities for sending email and push notifications
"""

import smtplib
import asyncio
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from typing import List, Optional
import logging

from app.config import settings
from app.models.notification import Notification
from app.models.user_settings import UserSettings
from app.models.product import Product
from app.database.session import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

logger = logging.getLogger(__name__)


async def send_email_notification(
    to_email: str, 
    subject: str, 
    body: str
) -> bool:
    """Send email notification"""
    try:
        msg = MIMEMultipart()
        msg['From'] = settings.EMAIL_FROM
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html'))
        
        server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
        server.starttls()
        server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(settings.EMAIL_FROM, to_email, text)
        server.quit()
        
        logger.info(f"Email sent successfully to {to_email}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send email to {to_email}: {str(e)}")
        return False


async def send_push_notification(
    user_id: int, 
    title: str, 
    body: str,
    tokens: List[str]
) -> bool:
    """Send push notification via Firebase"""
    try:
        # This would integrate with Firebase Cloud Messaging
        # For now, we'll log the notification
        logger.info(f"Push notification sent to user {user_id}: {title}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send push notification to user {user_id}: {str(e)}")
        return False


async def create_notification_record(
    db: AsyncSession,
    user_id: int,
    product_id: Optional[int],
    notification_type: str,
    message: str
) -> Notification:
    """Create notification record in database"""
    notification = Notification(
        user_id=user_id,
        product_id=product_id,
        notification_type=notification_type,
        message=message,
        sent_at=datetime.utcnow(),
        is_sent=True
    )
    
    db.add(notification)
    await db.commit()
    await db.refresh(notification)
    
    return notification


async def send_expiration_notifications():
    """Send notifications for products expiring within the configured days"""
    async with get_async_session() as db:
        try:
            # Get current date and target date range
            today = datetime.utcnow().date()
            target_date = today + timedelta(days=settings.NOTIFICATION_DAYS_BEFORE)
            
            # Find products expiring within the notification window
            result = await db.execute(
                select(Product, User, UserSettings)
                .join(User, Product.user_id == User.id)
                .join(UserSettings, User.id == UserSettings.user_id)
                .where(
                    Product.expiration_date >= today,
                    Product.expiration_date <= target_date,
                    Product.is_active == True,
                    User.is_active == True
                )
            )
            
            notifications_to_send = result.all()
            
            for product, user, user_settings in notifications_to_send:
                # Skip if user has disabled notifications
                if not user_settings.email_enabled and not user_settings.push_enabled:
                    continue
                
                # Create notification message
                days_until = (product.expiration_date - today).days
                message = f"Reminder: {product.name} expires in {days_until} days"
                
                # Send email notification
                if user_settings.email_enabled and user.email:
                    email_body = create_email_template(product, days_until)
                    email_sent = await send_email_notification(
                        user.email, 
                        "Food Expiration Reminder", 
                        email_body
                    )
                    
                    if email_sent:
                        await create_notification_record(
                            db, user.id, product.id, "email", message
                        )
                
                # Send push notification
                if user_settings.push_enabled:
                    push_sent = await send_push_notification(
                        user.id, 
                        "Expiration Reminder", 
                        message,
                        []  # Would get from user device tokens
                    )
                    
                    if push_sent:
                        await create_notification_record(
                            db, user.id, product.id, "push", message
                        )
                
                # Send combined notification
                if user_settings.email_enabled and user_settings.push_enabled:
                    await create_notification_record(
                        db, user.id, product.id, "both", message
                    )
            
            logger.info(f"Processed {len(notifications_to_send)} expiration notifications")
            
        except Exception as e:
            logger.error(f"Error sending expiration notifications: {str(e)}")


def create_email_template(product: Product, days_until: int) -> str:
    """Create HTML email template for expiration notification"""
    return f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background-color: #f44336; color: white; padding: 20px; text-align: center; }}
            .content {{ background-color: #f9f9f9; padding: 20px; border-radius: 5px; }}
            .product-info {{ background-color: white; padding: 15px; margin: 15px 0; border-radius: 5px; }}
            .footer {{ text-align: center; color: #666; font-size: 12px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Food Expiration Alert</h1>
            </div>
            <div class="content">
                <p>Hello,</p>
                <p>This is a reminder that one of your food items is approaching its expiration date:</p>
                
                <div class="product-info">
                    <h3>{product.name}</h3>
                    <p><strong>Expires in:</strong> {days_until} days</p>
                    <p><strong>Expiration Date:</strong> {product.expiration_date}</p>
                    {f'<p><strong>Shop:</strong> {product.shop_name}</p>' if product.shop_name else ''}
                    {f'<p><strong>Amount:</strong> {product.amount} {product.unit}</p>' if product.amount and product.unit else ''}
                </div>
                
                <p>Please check your food items and consider using them soon or disposing of them properly.</p>
            </div>
            <div class="footer">
                <p>This is an automated message from your Food Expiration Tracker app.</p>
            </div>
        </div>
    </body>
    </html>
    """


def start_notification_scheduler():
    """Start the notification scheduler"""
    async def notification_task():
        while True:
            try:
                await send_expiration_notifications()
                # Run every hour
                await asyncio.sleep(3600)
            except Exception as e:
                logger.error(f"Error in notification scheduler: {str(e)}")
                await asyncio.sleep(3600)
    
    # Start the scheduler in the background
    asyncio.create_task(notification_task())
    logger.info("Notification scheduler started")