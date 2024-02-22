from sqlalchemy.orm import Session

from models import User


def create_user(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session) -> User:
    return db.query(User).all()
