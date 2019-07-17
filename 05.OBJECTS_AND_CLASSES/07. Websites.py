class Website:

    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        self.queries = queries


if __name__ == '__main__':

        input_string = input()
        website_list = []
        while not input_string == 'end':
            data_list = input_string.split(' | ')
            if len(data_list) < 3:
                single_website = Website(host=data_list[0], domain=data_list[1])
            else:
                single_website = Website(host=data_list[0], domain=data_list[1], queries=data_list[2])
            website_list.append(single_website)
            input_string = input()

        for website in website_list:
            if website.queries:
                print(f"https://www.{website.host}.{website.domain}/query?=[{']&['.join(website.queries.split(','))}]")
            else:
                print(f'https://www.{website.host}.{website.domain}')