from lib.profile import get_profiles, create_profile, get_profile
from lib.manga import get_subbed_mangas, subscribe_to_manga, is_chapter_released
from lib.scraper import get_manga_list, display_manga_choices
from db.utils import init_database


try:

    # init database
    init_database()
        
    current_profile = None

    #"login" process
    print("Welcome. To continue, create a new profile or load an existing one from the following: ")
    profiles = get_profiles()
    for profile in profiles:
            print(f"{profile.username}")
    prof_choice = input("Press C to create a new profile, or P to pick a profile from the above: ")
    if prof_choice == "C":
            username_in = input("Enter the username: ")
            current_profile = create_profile(username_in)
    elif prof_choice == "P":
            username_in = input("Enter the username: ")
            current_profile = get_profile(username_in)
    else:
        raise Exception("Invalid command")
    print(f"Welcome, {current_profile.username}!")
    while(True):
        # user is "logged in" at this point
        command_choice = None
        print(f"S : Subscribe to a manga")
        print(f"L : List out your tracked mangas, and view changes")
        print(f"E : Exit")
        command_choice = input("> ")
        if(command_choice == "S"):
            manga_name = input("Enter the name of the manga you want to sub to : ")
            manga_list = get_manga_list(manga_name)
            print("Enter the index of the manga you would like to sub to : ")
            display_manga_choices(manga_list)
            chosen_manga_no = input("> ")
            manga_idx = int(chosen_manga_no)
            if manga_idx < 0 or manga_idx >= len(manga_list):
                raise Exception("Incorrect index.")
            subscribe_to_manga(manga_list[manga_idx], current_profile.username)
            print("Subbed!")
        elif(command_choice == "L"):
            manga_list = get_subbed_mangas(current_profile.username)
            print("Mangas you're subbed to : ")
            index = 0
            for manga in manga_list:
                print(f"{index} --> {manga.name}")
                index += 1
            should_change = input("Would you like to view changes? Y/N > ")
            if(should_change == "Y"):
                chosen_manga_no = input("Enter the index of the manga you want to view changes for : ")
                manga_idx = int(chosen_manga_no)
                release_status, latest_chap = is_chapter_released(manga_list[manga_idx])
                if(release_status):
                    print(f"There is a new release! {latest_chap} is out now")
                else:
                    print("No new releases. \n")
            else:
                pass
        elif(command_choice == "E"):
             print("byee")
             break
        else:
            raise Exception("Invalid command")   
except Exception as e:
    print(f"Exception : {str(e)}")
