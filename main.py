import redditapi as ra
import sentiment as se


reddit = ra.create_connection()
while True:
    subreddit = ra.get_subreddit(reddit)
    posts = ra.get_posts(subreddit)
    results = se.analyze_posts(posts)
    df = se.sentiment_to_df(results)
    labeled_df = se.label_df(df)

    se.sentiment(labeled_df)
    se.plot_sentiment(labeled_df)
    print('Five Most Positive Titles:')

    print(se.get_most_positive(df))
    print()
    print('Five Most Negative Titles:')
    print(se.get_most_negative(df))

    u_response = input('Would you like to continue? Type yes to continue or anything else to quit: ').lower()
    if u_response == 'yes':
        continue
    else:
        print("See you another day!")
        break
