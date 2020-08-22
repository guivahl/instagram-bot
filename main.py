from instapy import InstaPy

import config
import constants

session = InstaPy(username=config.username, password=config.password)

session.login()

session.set_skip_users(
    skip_private=False,
    skip_no_profile_pic=True,
    no_profile_pic_percentage=100,
    skip_business=True,
    business_percentage=100
)

user_nonfollowers=session.pick_nonfollowers(username=config.username, live_match=True, store_locally=True)

filtered_user_nonfollowers=list(set(user_nonfollowers) - set(config.white_list))

session.follow_user_followers(
    config.users_to_follow,
    amount=5,
    randomize=False,
    sleep_delay=constants.ONE_MINUTE_TO_SECONDS
)

session.unfollow_users(
    amount=20,
    custom_list_enabled=True,
    custom_list=filtered_user_nonfollowers,
    style="RANDOM",
    unfollow_after=(3 * constants.ONE_DAY_TO_SECONDS),
    sleep_delay=constants.ONE_MINUTE_TO_SECONDS
)

session.end()