from sqlalchemy import select, func
from sqlalchemy.orm import Session 

from app.models import (
    User,
    Post,
    Comment,
    Like,
    Tag,
    PostTag,
    Follow
)


#================================User

def create_user(session: Session, name: str, email: str, password: str, bio: str, avatar: str)->User:
    
    user = User(name=name, email=email, password=password, bio=bio, avatar=avatar)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return user




def get_user_by_id(session: Session, user_id):
    
    return session.get(User, user_id)


def get_users(session: Session):
    
    stmt = select(User)
    return list(session.scalars(stmt))


def update_user_name(session: Session, user_id: int, new_name: str):
    
    user = session.get(User, user_id)
    
    if user is None:
        return None
    
    user.name = new_name
    session.commit()
    session.refresh(user)
    
    return user
    

def delete_user(session: Session, user_id):
    
    user = session.get(User, user_id)
    
    if user is None:
        return False
    
    session.delete(user)
    session.commit()
    return True


#======================================Post


def create_post(session: Session, user: User, title: str, content: str, is_active: bool):
    
    post = Post(user=user, title=title, content=content, is_active=is_active)
    
    session.add(post)
    session.commit()
    session.refresh(post)
    
    return post 
    


def get_post_by_id(session: Session, post_id: int):
    
    return session.get(Post, post_id)


def get_posts(session: Session):
    
    stmt = select(Post)
    return list(session.scalars(stmt))


def update_post_title(session: Session, new_title: str, post_id: int):
    
    post = session.get(Post, post_id)
    
    if post is None:
        return None
    
    post.title = new_title
    session.commit()
    session.refresh(post)
    
    return post 


def delete_post(session: Session, post_id: int):
    
    post = session.get(Post, post_id)
    
    if post is None:
        return False
    
    session.delete(post)
    session.commit()
    
    return True


#==============================Comment


def create_comment(session: Session, user: User, post: Post, text):
    
    text = Comment(user=user, post=post, text = text)
    
    session.add(text)
    session.commit()
    session.refresh(text)
    
    return text


def get_comment_by_id(session: Session, comment_id: int):
    
    return session.get(Comment, comment_id)


def update_comment(session: Session, new_text, comment_id):
    
    comment = session.get(Comment, comment_id)
    
    if comment is None:
        return None
    
    comment.text = new_text
    session.commit()
    session.refresh(comment)
    
    return comment


def delete_comment(session: Session, comment_id: int):
    
    comment = session.get(Comment, comment_id)
    
    if comment is None:
        return False
    
    session.delete(comment)
    session.commit()
    
    return True 


#============================Like


def create_like(session: Session, user: User, post: Post):
    
    like = Like(user=user, post=post)
    
    session.add(like)
    session.commit()
    session.refresh(like)
    
    return like


def delete_like(session: Session, like_id: int):
    
    like = session.get(Like, like_id)
    
    if like is None:
        return False
    session.delete(like)
    session.commit()
    return True 

#===============Tag

def create_tag(session: Session, name: str):
    
    tag = Tag(name=name)
    
    session.add(tag)
    session.commit()
    session.refresh(tag)
    
    return tag


def get_tag_by_id(session: Session, tag_id):
    
    return session.get(Tag, tag_id)


def get_tags(session: Session):
    
    stmt = select(Tag)
    return list(session.scalars(stmt))


#=============PostTag


def create_post_tag(session: Session, tag_id: int, post_id: int):
    
    post_tag = PostTag(tag_id = tag_id, post_id = post_id)
    
    session.add(post_tag)
    session.commit()
    session.refresh(post_tag)
    
    return post_tag


def delete_post_tag(session: Session, tag_id: int, post_id: int):
    
    post_tag = session.get(PostTag, (tag_id, post_id))
    
    if post_tag is None:
        return False
    
    session.delete(post_tag)
    session.commit()
    
    return True


#====================Follow

def create_follow(session: Session, follower_id: int, following_id: int):
    
    follow = Follow(follower_id=follower_id, following_id=following_id)
    
    session.add(follow)
    session.commit()
    session.refresh(follow)
    
    return follow



def delete_follow(session: Session, follower_id: int, following_id: int):
    
    follow = session.get(Follow, (follower_id, following_id))
    
    if follow is None:
        return False
    
    session.delete(follow)
    session.commit()
    
    return True


