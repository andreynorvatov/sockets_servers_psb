# def likes(names):
#     names_count = len(names)
#     if names_count == 0:
#         return "no one likes this"
#     elif names_count == 1:
#         return ''.join([names[0], " likes this"])
#     elif names_count == 2:
#         return ''.join([names[0], " and ", names[1],  " like this"])
#     elif names_count == 3:
#         return ''.join([names[0], ", ", names[1], " and ", names[2],  " like this"])
#     else:
#         return ''.join([names[0], ", ", names[1], " and ", str(len(names[2:])),  " others like this"])
#
#
# print(likes([]))
# print(likes(['Peter']))
# print(likes(['Jacob', 'Alex']))
# print(likes(['Max', 'John', 'Mark']))
# print(likes(['Alex', 'Jacob', 'Mark', 'Max']))

# def order(sentence):
#     if len(sentence) == 0:
#         return ''
#
#     res_dict = {}
#     for word in sentence.split(' '):
#         for letter in word:
#             if letter.isdigit():
#                 res_dict[int(letter)] = word
#
#     sorted_res_dict = sorted(res_dict.items())
#     sorted_list = ' '.join([i[1] for i in sorted_res_dict])
#
#     return sorted_list

# def order2(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
#
# print(order(""))


# def persistence(n):
#     l = [i for i in str(n)]
#     res = 1
#     cnt = 0
#     while len(l) > 1:
#         for i in l:
#             res *= int(i)
#         l = [i for i in str(res)]
#         cnt += 1
#         res = 1
#     return cnt
#
# import operator
# def persistence2(n):
#     i = 0
#     while n>=10:
#         n=reduce(operator.mul,[int(x) for x in str(n)],1)
#         i+=1
#     return i
#
# print(persistence(39))
