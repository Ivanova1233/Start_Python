# a, s, p = 1, 150, 200
# while True:
#     if a>10:
#         break
#     a += 2
#     p += a
#     s += p
# print(s)
# c, d = 750, 90
# while True:
#     if d>0:
#         break
#     d -= 10
#     c = c/2 + 50
# print(c)
# s = 1
# for n in range(1,6):
#     s *= n
# print(s)
# m, n = 12, 5
# while True:
#     if m == n:
#      break
#     elif m > n:
#         m -= 2 * n
#     else:
#         n -=3
# print(m)

print(f'Задакча 3 b множественные условия')
m, n = 12, 5
while m != n:
     if m>n:
         m -= 2 * n
     else:
         n -= 3
         print(f'переменная m = {m}')