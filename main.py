import redditapi as ra
import sentiment as se

reddit = ra.create_connection()
while True:
    subreddit = ra.get_subreddit(reddit)
    posts = ra.get_posts(subreddit)
    print("Finished getting posts")
    results = se.analyze_posts(posts)
    print("Finished analyzing posts")
    df = se.sentiment_to_df(results)
    print("Got sentiment dataframe.")
    se.sentiment(df)
    se.plot_sentiment(df)
    u_response = input('Would you like to continue? Type yes to continue or anything else to quit: ').lower()
    if u_response == 'yes':
        continue
    else:
        print("See you another day!")
        break
