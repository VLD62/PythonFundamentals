if __name__ == '__main__':
    words_list = list(map(lambda x:x.lower(),input().split(" ")))
    words_count = {}
    for i in range(0,len(words_list)):
           if words_list[i] in words_count:
               words_count[words_list[i]] += 1
           else:
               words_count[words_list[i]] = 1
    words_count  = {key:value for key,value in words_count.items() if value % 2 == 1}
    print(", ".join(words_count))
