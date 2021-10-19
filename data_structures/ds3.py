# nums = [3,6,4,3,2,6,6,5,9,7]
#
# print(sum(nums))
#
#
# nums.pop()
# print(nums)



# languages = ['Java', 'Python', 'JavaScript']
# versions = [14, 3, 6]

# result = zip(*languages, versions)
# print(list(result))


sequence = "ababcbabc"
words = ["ab", "babc", "bca"]


def max_k_occurences(sequence,word):
    k = 1
    while word*k in sequence:
        print(word*k)
        k += 1
    return k-1

l = []
for i in words:
    l.append(max_k_occurences(sequence, i))
print(l)