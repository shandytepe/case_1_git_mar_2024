blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, 
              {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, 
              {'Comments': 4, 'Shares': 2}, 
              {'Photos': 8, 'Comments': 1, 'Shares': 1}, 
              {'Photos': 3, 'Likes': 19, 'Comments': 3}]

# fitur baru

total_likes = 0

try:
    for post in blog_posts:
        if 'Likes' not in post.keys():
            post['Likes'] = 0
            total_likes = total_likes + post['Likes']

except:
    pass

print(total_likes)