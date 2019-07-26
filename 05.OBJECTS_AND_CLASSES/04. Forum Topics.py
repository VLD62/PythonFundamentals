class Topic:
    def __init__(self,name,tags=[]):
        self.name = name
        self.tags = tags

def remove_duplicate_topics(arr):
    return sorted(set(arr), key=lambda x: arr.index(x))

if __name__ == '__main__':

    input_list = input().split(" -> ")
    topics = []
    while not input_list[0] == 'filter':
        new_topic = Topic(name=input_list[0],tags=input_list[1].split(', '))
        if new_topic.name not in [old_topic.name for old_topic in topics]:
            topics.append(new_topic)
        else:
            for old_topic in topics:
                if old_topic.name == new_topic.name:
                    old_topic.tags.extend(new_topic.tags)
        input_list = input().split(" -> ")

    for topic in topics:
        topic.tags = remove_duplicate_topics(topic.tags)

    cmd_list = input().split(', ')

    for topic in topics:
        if all(item in topic.tags  for item in cmd_list):
            new_topics = ['#' + i for i in topic.tags]
            print(f'{topic.name} | {", ".join(new_topics)}')