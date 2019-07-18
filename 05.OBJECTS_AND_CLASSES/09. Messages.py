class User:

    def __init__(self, Username, ReceivedMessages):
        self.Username = Username
        self.ReceivedMessages = ReceivedMessages


class Message:

    def __init__(self, Content, Sender):
        self.Content  = Content
        self.Sender  =  Sender


def Max_num(a,b):
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':

        input_string = input().split(' ')
        users_list = {}
        message_list_1 = []
        message_list_2 = []

        while not input_string[0] == 'exit':
            if input_string[0] == 'register':
                newUser = User(input_string[1], [])
                users_list[input_string[1]] = newUser
            else:
                for key, user in users_list.items():
                    if user.Username == input_string[2]:
                        newMessage = Message(input_string[3], input_string[0])
                        user.ReceivedMessages.append(newMessage)

            input_string = input().split(' ')

        final_usernames = input().split(' ')

        for key,user in users_list.items():
            if user.Username == final_usernames[1]:
                for messages in user.ReceivedMessages:
                    if messages.Sender == final_usernames[0]:
                        message_list_1.append(f'{messages.Sender}: {messages.Content}')

        for key,user in users_list.items():
            if user.Username == final_usernames[0]:
                for messages in user.ReceivedMessages:
                    if messages.Sender == final_usernames[1]:
                        message_list_2.append(f'{messages.Content} :{messages.Sender}')

        if len(message_list_1) > 0 or len(message_list_2) > 0:
            for i in range(0,Max_num(len(message_list_1),len(message_list_2))):
                if i < len(message_list_1):
                    print(message_list_1[i])
                if i < len(message_list_2):
                    print(message_list_2[i])
        else:
            print('No messages')
