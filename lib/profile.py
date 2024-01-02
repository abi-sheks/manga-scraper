from db.models import *

def get_profiles():
    database.connect(reuse_if_open=True)
    profiles = Profile.select()
    database.close()
    return profiles

def get_profile(uname : str):
    database.connect(reuse_if_open=True)
    try:
        reqd_profile = Profile.get(Profile.username==uname)
    except Exception as e:
        raise Exception(f"The required profile could not be found : {str(e)}")
    database.close()
    return reqd_profile

def create_profile(uname : str):
    database.connect(reuse_if_open=True)
    profiles = Profile.select()
    profile_usernames = [profile.username for profile in profiles]
    if uname in profile_usernames:
        raise Exception("Profile already exists")
    new_profile = Profile.create(username=uname)
    print("Created successfully!")
    database.close()
    return new_profile