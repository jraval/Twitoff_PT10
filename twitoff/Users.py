from twitoff.data_model import User, DB, Tweet

app_user = User(id=1, name='app_user')
user_8 = User(id=7, name="user_8")
user_9 = User(id=8, name="user_9")
user_10 = User(id=9, name="user_10")
user_11 = User(id=10, name="user_11")
user_12 = User(id=11, name="user_12")

user_list = [app_user, user_8, user_9, user_10, user_11, user_11, user_12]

t0 = Tweet(id=0, text='tweet test', user_id=1)
t1 = Tweet(id=1, text='another test', user_id=2)
t2 = Tweet(id=2, text='third tweet', user_id=3)
new_tweet = Tweet(id=3, text='tweet issues', user_id=4)

tweet_list = [t0, t1, t2, new_tweet]



