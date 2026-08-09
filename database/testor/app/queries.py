from sqlalchemy import select

from sqlalchemy.orm import Session

from app.models import User, Post



def create_user(session: Session, name: str, email: str)-> User:
    
    user = User(name = name, email = email)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return user 



def create_post(session: Session, user_id: int, title: str)-> Post:
    
    post = Post(user_id = user_id, title = title)
    
    session.add(post)
    session.commit()
    session.refresh(post)
    
    return post 



def get_user_by_id(session: Session, user_id: int)-> User | None:
    
    return session.get(User, user_id)



def get_users(session: Session)->list[User] | None:
    
    stmt = select(User)
    return list(session.scalars(stmt))



def update_user_name(session: Session, user_id: int, new_name: str)-> User | None:
    
    user = session.get(User, user_id)
    
    if user is None:
        return None
    
    user.name = new_name
    session.commit()
    session.refresh(user)
    
    return user



def delete_user(session: Session, user_id)->bool:
    
    user = session.get(User, user_id)
    
    if user is None:
        return False
    
    session.delete(user)
    session.commit()
    
    return True
