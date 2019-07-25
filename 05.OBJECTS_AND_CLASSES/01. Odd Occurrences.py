class Element:
    def __init__(self, name, appearance_count):
        self.name = name
        self.count = appearance_count


if __name__ == "__main__":

    List_Of_String = [x.lower() for x in input().split()]
    Element_List = []

    for idx in range(len(List_Of_String)):
        single_element = Element(name=List_Of_String[idx], appearance_count=1)
        for idx2 in range(len(List_Of_String)):
            if not idx == idx2 and List_Of_String[idx] == List_Of_String[idx2]:
                single_element.count += 1
        if single_element.count % 2 == 1 and single_element.name not in [element.name for element in Element_List]:
            Element_List.append(single_element)

    Element_List = [x.name for x in Element_List]
    print(", ".join(Element_List))
