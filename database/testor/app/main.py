from app.db import SessionLocal

from app.queries import (
    create_user,
    create_post,
    get_user_by_id,
    get_users,
    update_user_name,
    delete_user
)


def main():
    
    with SessionLocal() as session:
        
        user = create_user(session, "Scott", "mccall@gmail.com") #from crud c "clearly create"
        user1 = create_user(session, "Styles", "stilinski@gmail.com")
        user2 = create_user(session, "Derek", "hale2gmail.com")
        user3 = create_user(session, "Allison", "argent@gmail.com")
        user4 = create_user(session, "Mark", "newton@gmail.com")
        user5 = create_user(session, "peter", "halee@gmail.com")
        
        post = create_post(session, user.id, "teenwolf")

        found = get_user_by_id(session, user3.id) # from crud: r "clearly read"
        
        if found:
            print(f"found res: {found.id}, {found.name}")
        
        
        users = get_users(session)
        print("Users: ")
        
        if users:
            for u in users:
                print(u.id, u.name)
                
        
        updated = update_user_name(session, user4.id, "isaac")
        
        if updated:
            print(updated.id, updated.name)
        
        
        deleted = delete_user(session, user5.id)
        print(deleted) 

if __name__ == "__main__":
    main()
