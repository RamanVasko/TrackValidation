"""
Category model for the Food Expiration Tracker application
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models import Base


class Category(Base):
    """Category model"""
    
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Self-referential relationship for nested categories
    parent = relationship("Category", remote_side=[id], backref="children")
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "parent_id": self.parent_id,
            "children": [child.to_dict() for child in self.children],
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }