import os
from pathlib import Path, PosixPath
from typing import List, Optional
from pydantic import BaseModel

from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()
db_name: str = 'test_users_sqlalchemy'
db_folder: PosixPath = Path(__file__).parent.parent
os.makedirs(f'{db_folder}/db', exist_ok=True)
db_file_path: PosixPath = db_folder.joinpath(f"db/{db_name}.db")

DATABASE_URL = f"sqlite:///{db_file_path}"
#DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel): # Validate input data before saving them in the db
    name: str
    email: str

class UserResponse(BaseModel): # Validate data before sending them
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel): # Validate input data before updating them in the db
    name: Optional[str] = None
    email: Optional[str] = None

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    new_user: User = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> List[User]:
    users: List[User] = db.query(User).offset(offset=skip).limit(limit=limit).all()
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
def read_users(user_id: int = 0, db: Session = Depends(get_db)) -> User:
    user: User = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=UserUpdate)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)) -> User:
    db_user: User = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name if user.name is not None else db_user.name
    db_user.email = user.email if user.email is not None else db_user.email
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, db: Session = Depends(get_db)) -> User:
    user: User = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user