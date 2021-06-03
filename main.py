import instaloader
bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, '_mr._.vector_')
bot.login(user="username",passwd="password")
followers = [follower.username for follower in profile.get_followers()]
followings = [following.username for following in profile.get_followees()]
print(followers)
print(followings)