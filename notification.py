"""
Notification schemas for API validation and serialization
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NotificationBase(BaseModel):
    """Base notification schema"""
    user_id: int
    product_id: Optional[int] = None
    notification_type: str  # 'email', 'push', 'both'
    message: str


class NotificationCreate(NotificationBase):
    """Schema for notification creation"""
    pass


class NotificationResponse(NotificationBase):
    """Schema for notification response"""
    id: int
    sent_at: Optional[datetime] = None
    is_sent: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserSettingsBase(BaseModel):
    """Base user settings schema"""
    notification_days: int = 3
    email_enabled: bool = True
    push_enabled: bool = True


class UserSettingsCreate(UserSettingsBase):
    """Schema for user settings creation"""
    pass


class UserSettingsUpdate(BaseModel):
    """Schema for user settings updates"""
    notification_days: Optional[int] = None
    email_enabled: Optional[bool] = None
    push_enabled: Optional[bool] = None


class UserSettingsResponse(UserSettingsBase):
    """Schema for user settings response"""
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class NotificationTestRequest(BaseModel):
    """Schema for notification test request"""
    notification_type: str  # 'email', 'push', 'both'
    test_message: Optional[str] = "This is a test notification"


class NotificationTestResponse(BaseModel):
    """Schema for notification test response"""
    success: bool
    message: str
    sent_to: list[str]