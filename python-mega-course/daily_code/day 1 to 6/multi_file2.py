file = open('../text_files/a.txt', 'r')
file_content_a = file.read()
file.close()

file = open('../text_files/b.txt', 'r')
file_content_b = file.read()
file.close()

file = open('../text_files/c.txt', 'r')
file_content_c = file.read()
file.close()

print(file_content_a)
print(file_content_b)
print(file_content_c)