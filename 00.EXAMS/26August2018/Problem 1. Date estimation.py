from datetime import date

if __name__ == "__main__":
    input_date = list(map(int,input().split("-")))
    ref_date = date(2018,8,25)
    exam_date = date(2018,8,26)
    date_time_obj =date(input_date[0],input_date[1],input_date[2])
    
    if exam_date > date_time_obj:
        print('Passed')
    elif exam_date == date_time_obj:
        print('Today date')
    else:
        print(f'{(date_time_obj - ref_date).days} days left')