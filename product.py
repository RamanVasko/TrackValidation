"""
Product schemas for API validation and serialization
"""

from pydantic import BaseModel, validator
from typing import Optional
from datetime import date
from decimal import Decimal


class ProductBase(BaseModel):
    """Base product schema"""
    name: str
    category_id: Optional[int] = None
    barcode: Optional[str] = None
    shop_name: Optional[str] = None
    purchase_date: Optional[date] = None
    expiration_date: date
    amount: Optional[Decimal] = None
    unit: Optional[str] = None
    notes: Optional[str] = None
    image_url: Optional[str] = None


class ProductCreate(ProductBase):
    """Schema for product creation"""
    
    @validator('expiration_date')
    def expiration_date_must_be_future(cls, v):
        from datetime import date
        if v <= date.today():
            raise ValueError('Expiration date must be in the future')
        return v
    
    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Amount must be positive')
        return v


class ProductUpdate(BaseModel):
    """Schema for product updates"""
    name: Optional[str] = None
    category_id: Optional[int] = None
    barcode: Optional[str] = None
    shop_name: Optional[str] = None
    purchase_date: Optional[date] = None
    expiration_date: Optional[date] = None
    amount: Optional[Decimal] = None
    unit: Optional[str] = None
    notes: Optional[str] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = None


class ProductResponse(ProductBase):
    """Schema for product response"""
    id: int
    user_id: int
    is_active: bool
    days_until_expiration: int
    is_expired: bool
    is_near_expiration: bool
    created_at: str
    updated_at: Optional[str] = None
    
    class Config:
        from_attributes = True


class BarcodeScanRequest(BaseModel):
    """Schema for barcode scan request"""
    barcode: str


class BarcodeScanResponse(BaseModel):
    """Schema for barcode scan response"""
    success: bool
    message: str
    product_data: Optional[dict] = None