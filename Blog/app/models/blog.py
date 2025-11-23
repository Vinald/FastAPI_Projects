from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.cpre.database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    creator  = relationship("User", back_populates="blogs")
