from app.db import SessionLocal
from app.queries import (create_user, 
    create_post, 
    create_comment, 
    create_like, 
    create_tag, 
    create_post_tag, 
    create_follow,
    get_user_by_id,
    get_users,
    update_user_name,
    delete_user,
    update_post_title,
    update_comment,
    delete_post,
    get_post_by_id,
    get_posts,
    get_comments,
    get_comment_by_id,
    delete_comment
)



def main():
    
    with SessionLocal() as session:
        
        user = create_user(
            session,
            name="Teo",
            email = "teo@gmail.com",
            password = "qwerty123",
            bio = "programmer",
            avatar = ""
        )
        
        
        user1 = create_user(
            session,
            name = "Tony",
            email = "stark@gmail.com",
            password="ironman123",
            bio = "genius, playboy, billioniar",
            avatar="iron.jpg"
        )
        
        post = create_post(
            session,
            user = user,
            title = "birth of algorithm",
            content="algorithm is easy when you understand its meaning",
            is_active = True
        )
        
        
        comment = create_comment(
            session,
            user = user,
            post = post,
            text = "oh man you choose good name for post"
        )
        
        
        like = create_like(
            session,
            user=user,
            post = post
        )
        
        
        tag = create_tag(session, name = "#python")
        
        post_tag = create_post_tag(session, tag_id=tag.id, post_id=post.id)
        
        
        follow = create_follow(
            session,
            follower_id=user.id,
            following_id=user1.id
        )
        
        
        found = get_user_by_id(session, user.id)
        print(found)
        
        users = get_users(session)
        
        for u in users:
            print(u.id, u.name)
        
        updated = update_user_name(session, user.id, "haydar")
        print(updated)
        
        #deleted = delete_user(session, user1.id)
        
        
        found_post = get_post_by_id(session, post.id)
        print("post by id: ", found_post)
        
        posts = get_posts(session)
        
        for u in posts:
            print(u.id, u.title)
        
        
        update_title = update_post_title(session, "hackers", post.id)
        print("updated_post", update_title)
        

        #deleted_post = delete_post(session, post.id)
        
        comments = get_comments(session)
        
        for u in comments:
            print(u.id, u.text)
            
        comment_by_id = get_comment_by_id(session, comment.id)
        print(comment_by_id)
        
        
        update_com = update_comment(session, "you know if you have time see mentalist", comment.id)
        print(update_com)

        deleted_com = delete_comment(session, comment.id)
        
        print(delete_comment)
        
        

if __name__ == "__main__":
    main()
