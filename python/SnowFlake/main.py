from threading import Thread


def streamAndClassify():
    from tweppy_streamer import TwitterStreamer

    hash_tag_list = ["bo"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

def restApi():
    import rest
    from app import app
    if __name__ == "__main__":
         app.run()

print("  / ____| \ | |/ __ \ \        / /  ____| |        /\   | |/ /  ____|")
print(" | (___ |  \| | |  | \ \  /\  / /| |__  | |       /  \  | ' /| |__   ")
print("  \___ \| . ` | |  | |\ \/  \/ / |  __| | |      / /\ \ |  < |  __|  ")
print("  ____) | |\  | |__| | \  /\  /  | |    | |____ / ____ \| . \| |____ ")
print(" |_____/|_| \_|\____/   \/  \/   |_|    |______/_/    \_\_|\_\______|")
print(":: SnowFlake - The Twitter Prostitution Indentifier ::     <v.1.0>")
print(":: https://github.com/Alfinandika/SnowFlake ::")
Thread(target = streamAndClassify).start() 
Thread(target = restApi).start()

