import instaloader

class InstaloaderService:
    def __init__(self, used_account, used_password):
        self.hello = "Hello instaloader!"
        self.loader = instaloader.Instaloader()
        # self.loader.login(used_account, used_password)
        self.loader.load_session_from_file(used_account)

    def print_hello(self):
        print(self.hello)

    def make_verification(self, target_account):
        loader = self.loader

        profile = instaloader.Profile.from_username(loader.context,target_account)

        followers = [follower.username for follower in profile.get_followers()]

        followings = [followee.username for followee in profile.get_followees()]

        non_mutuals = followings.copy()

        for person in followings:
            if person in followers:
                non_mutuals.remove(person)

        print(*non_mutuals, sep='\n')

    def get_followers_list(self, target_account):
        loader = instaloader.Instaloader()

        # loader.load_session_from_file(used_account)

        profile = instaloader.Profile.from_username(loader.context, target_account)

        followers = [follower.username for follower in profile.get_followers()]

        return followers
    
    def get_profile_data(self, target_account):
        loader = self.loader

        try: 
            profile = instaloader.Profile.from_username(loader.context, target_account)
        except Exception as ex:
            excpetion_string = str(ex)
            print(excpetion_string)
            if ("does not exist" in excpetion_string):
                return "Deleted", []

        status = "False"
        following_list = []

        if profile.is_private:
            status = "Private"
        elif profile.followees > 2000:
            status = "Invalid"
        # elif profile.followees > 500:
        #     status = "False"
        else:
            try:
                following_list = [followee.username for followee in profile.get_followees()]
                status = "True"
            except Exception as ex:
                excpetion_string = str(ex)
                print(excpetion_string)
                if ("error code 401" in excpetion_string):
                    from service.TimeService import TimeService
                    TimeService.notifica_erro(excpetion_string)
                    exit()
        
        return status, following_list

    def recreate_session(self, used_account, used_password):
        self.loader.login(used_account, used_password)
