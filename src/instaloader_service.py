import instaloader
import pandas as pd

loader = instaloader.Instaloader()

loader.load_session_from_file("ladien.cup")

profile = instaloader.Profile.from_username(loader.context,'dani.apc')

followers = [follower.username for follower in profile.get_followers()]

followings = [followee.username for followee in profile.get_followees()]

non_mutuals = followings.copy()

for person in followings:
    if person in followers:
        non_mutuals.remove(person)

print(*non_mutuals, sep='\n')