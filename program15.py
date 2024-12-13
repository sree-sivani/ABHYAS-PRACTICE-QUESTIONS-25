sen = input()

strip_sen=sen.strip()


words = strip_sen.split()

l_word = words[-1]

length = len(l_word)

print(length-1)
