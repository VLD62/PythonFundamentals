def normalize_space(s):
    return ' '.join(s.split())

if __name__ == '__main__':
    int_list = input().split('|')
    int_list.reverse()
    print(normalize_space(' '.join(int_list)))  