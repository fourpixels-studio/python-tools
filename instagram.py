import instaloader

def scrape_instagram_page(username, num_posts=30):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Fetch the profile object of the specified username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Download the first 'num_posts' posts from the profile
        posts = profile.get_posts()
        count = 0
        for post in posts:
            loader.download_post(post, target=username)
            count += 1
            if count >= num_posts:
                break
        print(f"Successfully scraped the first {num_posts} posts from {username}!")
    except Exception as e:
        print(f"Error occurred: {e}")

# Replace 'instagram_username' with the actual username you want to scrape
scrape_instagram_page('username', num_posts=30)
