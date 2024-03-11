from . import db
from .models import User

def load_usernames_bulk(filepath):
    # Clear the User table
    User.query.delete()
    db.session.commit()
    
    users = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            if len(parts) >= 2:  # Ensure there's at least a first name and a last name
                firstname = parts[0]  # First part is the first name
                lastname = ' '.join(parts[1:])  # Join the remaining parts as the last name
                users.append({'firstname': firstname, 'lastname': lastname})
                
                # Insert in batches of 1000 (or another suitable batch size)
                if len(users) >= 1000:
                    db.session.bulk_insert_mappings(User, users)
                    db.session.commit()
                    users = []
            else:
                print(f"Invalid line format, skipping: {line.strip()}")

    # Insert any remaining users
    if users:
        db.session.bulk_insert_mappings(User, users)
        db.session.commit()
