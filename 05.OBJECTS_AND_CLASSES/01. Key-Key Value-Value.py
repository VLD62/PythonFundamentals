class KeyValue:
    def __init__(self,key,values):
        self.key = key
        self.values = values

if __name__ == "__main__":
    key = input()
    value = input()
    N = int(input())
    Key_Value_List = []
    
    for i in range(0,N):
        input_list = input().split(" => ")
        new_key_value = KeyValue(key=input_list[0],values=input_list[1])
        Key_Value_List.append(new_key_value)
    
    for k_v in Key_Value_List:
        if key in k_v.key:
            kv_list = k_v.values.split(";")
            print(f'{k_v.key}:')
            for values in kv_list:
                if value in values:
                    print(f'-{values}')
                

