from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modal import Base, User

engine = create_engine('sqlite:///users.db', connect_args={"check_same_thread": False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def is_username_taken(username):
    """
   Returns True if username is already taken,
   False otherwise.
   """
    user = session.query(
        User).filter_by(
        username=username).first()
    return user is not None

def add_user(id_num, full_name, username, password, site_administrator, facility_administrator, email, alt_email):
    user_object = User(
        id_num=id_num,
        full_name=full_name,
        username=username,
        password=password,
        site_administrator=site_administrator,
        facility_administrator=facility_administrator,
        email=email,
        alt_email=alt_email
    )
    session.add(user_object)
    session.commit()

def authenticate(username, password):
    """
    Returns true if there exists that username
    AND the password is correct; otherwise false.
    """
    user = session.query(
        User).filter_by(
        username=username).first()

    if user is not None:
        correct_password = user.password
        return correct_password == password

    return False

def get_admin_from_database(username):
    """
    Returns user object if there exists that username; otherwise None.
    """
    User = get_user_from_database(username)
    if User.site_administrator == 1:
        return True

def get_user_from_database(username):
    """
    Returns user object if there exists that username; otherwise None.
    """
    return session.query(User).filter_by(username=username).first()

def query_all():
    """ Returns all the users in the database"""

    users = session.query(User).all()
    return users

def query_by_full_name(full_name):
    """ Finds first user in the database, by full name"""
    users = session.query(User).filter_by(full_name=full_name).first()
    return users

def update_password(username, new_password):
    """ Updates users password with new password in the database"""
    user_object = session.query(User).filter_by(username=username).first()
    user_object.password = new_password
    session.commit()

def delete_user(full_name):
    """ Delete user from the database"""
    session.query(User).filter_by(full_name=full_name).delete()
    session.commit()


#----------------------------------------------------------------------------------
#The are to add to the database and check the user info.

# print(query_all())
# add_user(123456, 'Resident A', 'Resident.A', 'Password', True, True, None, None)

# print(get_admin_from_database('Resident.A'))
