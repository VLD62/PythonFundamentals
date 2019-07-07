if __name__ == "__main__":

    posts_list = []
    ## Check split in comment
    data_list = input().split()

    while not data_list[0] == "drop":
        post_dict = {
            'Post': "none",
            'Likes': 0,
            'Dislikes': 0,
            'Comments': []
        }
        if data_list[0] == 'post':
            post_dict['Post'] = data_list[1]
            posts_list.append(post_dict)
        elif data_list[0] == 'like':
            for post in posts_list:
                 if post.get('Post') == data_list[1]:
                    post['Likes'] += 1

        elif data_list[0] == 'dislike':
            for post in posts_list:
                if post.get('Post') == data_list[1]:
                    post['Dislikes'] += 1

        elif data_list[0] == 'comment':
            for post in posts_list:
                if post.get('Post') == data_list[1]:
                    comment_dict = {}
                    comment_dict[data_list[2]] = ' '.join(data_list[3:])
                    post['Comments'].append(comment_dict)

        data_list = input().split(' ')

    for posts in posts_list:
        print(f"Post: {posts['Post']} | Likes: {posts['Likes']} | Dislikes: {posts['Dislikes']}")
        print("Comments:")
        if len(posts['Comments']) > 0:
            for comment in posts['Comments']:
                for k,v in comment.items():
                    print(f'*  {k}: {v}')
        else:
            print("None")


