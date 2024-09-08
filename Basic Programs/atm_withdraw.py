# input section 
amount = int(input('Enter the amount ')) - 500

# logic section
num_2000 = amount // 2000  # 4000 // 2000 => 2
amount = amount - num_2000 * 2000
num_500 = amount // 500  # 4000 // 500 => 8




# Output Section 
print('Number of Two Thousand Notes', num_2000)
print('Number of Five Hundred Notes',num_500 + 1)
# print('Number of Two Hundred Notes', num_200)
# print('Number of One Hundred Notes', num_100 + 1)