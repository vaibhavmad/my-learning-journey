
file = open('../text_files/members.txt', 'r')
member_list = file.readlines()
file.close()

new_name = input("Add a new member: ")
new_name = f"{new_name}\n"
member_list.append(new_name)
file = open('../text_files/members.txt', 'w')
file.writelines(member_list)

