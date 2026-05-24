# models.py
from pydantic import BaseModel, Field

# Task 3: Define the User model
class User(BaseModel):
    id: int
    name: str
    email: str
    # Setting a default value means this field is optional when creating a user
    is_active: bool = True 

# Task 4: Define the Course model
class Course(BaseModel):
    id: int
    title: str
    description: str
    # Default value set to 30 as requested
    max_students: int = 30