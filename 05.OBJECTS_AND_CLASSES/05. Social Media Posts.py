class Post:
    def __init__(self, name, like=0, dislike=0, comments=None):
        self.name = name
        self.like = like
        self.dislike = dislike
        self.comments = comments


if __name__ == '__main__':
    commands = input().split()
    posts = []

    while not " ".join(commands) == 'drop the media':

        if commands[0] == 'post':
            new_post = Post(name=commands[1], comments=[])
            posts.append(new_post)
        else:
            for post in posts:
               if post.name == commands[1]:
                    if commands[0] == 'like':
                        post.like += 1
                    if commands[0] == 'dislike':
                        post.dislike += 1
                    if commands[0] == 'comment' and post.name == commands[1]:
                        post.comments.append(commands[2] + ": " + " ".join(commands[3:]))

        commands = input().split()

    for post in posts:
        print(
            f'Post: {post.name} | Likes: {post.like} | Dislikes: {post.dislike}')
        print('Comments:')
        if len(post.comments) > 0:
            for commentator in post.comments:
                print('*  ' + commentator)
        else:
            print('None')
