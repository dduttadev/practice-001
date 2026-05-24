# main.py
from models import User, Course
from pydantic import ValidationError

def main():
    print("--- Task 5: Creating Valid Instances ---")
    user1 = User(id=1, name="Alice", email="alice@example.com")
    user2 = User(id=2, name="Bob", email="bob@example.com", is_active=False) 

    course1 = Course(id=101, title="Python Basics", description="Learn Python from scratch.")
    course2 = Course(id=102, title="Advanced Git", description="Master branching.", max_students=15)

    print(f"User 1 created successfully: {user1.name}")
    print(f"Course 1 created successfully: {course1.title}\n")

    print("--- Task 6: Testing Invalid Data / ValidationError ---")
    try:
        invalid_user = User(
            id=3, 
            name="Charlie", 
            email=[1, 2, 3]     # this is an invalid input
        )
    except ValidationError as e:
        print("Success! Pydantic caught the bad data. Here is the error layout:\n")
        print(e)
    print("\n")

    print("--- Task 7: Printing Dicts with model_dump() ---")
    print("User 1 Dictionary:", user1.model_dump())
    print("User 1 Dictionary:", user1)

if __name__ == "__main__":
    main()