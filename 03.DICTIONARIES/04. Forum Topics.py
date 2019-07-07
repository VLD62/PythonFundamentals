if __name__ == "__main__":
    topics_dict = {}
    tags_array = []
    data_list = input().split(' -> ')

    while not data_list[0] == "filter":

        if data_list[0] not in topics_dict.keys():
            topics_dict[data_list[0]] = data_list[1].split(', ')
        else:
            topics_dict[data_list[0]] += data_list[1].split(', ')

        data_list = input().split(' -> ')

    for k,v in  topics_dict.items():
        topics_dict[k] = list(dict.fromkeys(v))

    tags_array = input().split(', ')


    for k,v in topics_dict.items():
        temp_list = ['#' + el for el in v]
        if all(tags in v for tags in tags_array):
            print(f'{k} | {", ".join(temp_list)}')
