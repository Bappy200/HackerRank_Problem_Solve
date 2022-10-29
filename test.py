# for i in range(10):
#     for j in range(10):
#         if i == j:
#             print(i)
#             break
#     print("hello")
letter = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'.split(", ")
print(letter)
ec = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c = ec.index('z')
copy_letter = letter.copy()
copy_letter.pop()
print(copy_letter)
print(letter)
print(c)
num = [1, 3, 4, 5, 67, 78, 667, 56]
letter_double = [2 * i for i in letter]
print(letter_double)
x = 12.3456789
print('The value of x is %.2f' %x)
st = "This will split all words into a list".upper().split("I")
print(st)

text = ['Python']

# join elements of text with space
text.append(12)
print(text)