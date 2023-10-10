import instaloader

class InstaloaderService:
    def __init__(self):
        self.hello = "Hello instaloader!"

    def print_hello(self):
        print(self.hello)

    def make_verification(self, used_account, target_account):
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

    def get_followers_list(self, used_account, target_account):
        loader = instaloader.Instaloader()

        loader.load_session_from_file(used_account)

        profile = instaloader.Profile.from_username(loader.context, target_account)

        followers = [follower.username for follower in profile.get_followers()]

        return followers