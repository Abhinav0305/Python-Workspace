names_list=['abhinav','sachin','kamath','tonse','tejas','kanisk','ro']

for name_length in names_list:
    if len(name_length)>5 and ('n' in name_length or 'N' in name_length):
        print(len(name_length))
        print(name_length)


while len(names_list)>=1:
    print(names_list.pop())





