# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 # вычисление функции F
#                 # вывод (x, y, z, w), если F=1
# F = (x or y) and not (y==z) and not (w)
# if F:  # то же самое, что "if F == True:"
#   print(x, y, z, w)
# print(f'пример 1')
# for x in 0, 1:
#      for y in 0, 1:
#          for z in 0, 1:
#             for w in 0, 1:
#                 F = (x or y) and not (y == z) and not (w)
#                 if F == 1
#                     print(x, y, z, w, F)
# print(f'пример 2')
# for x in 0, 1:
#      for y in 0, 1:
#          for z in 0, 1:
#             for w in 0, 1:
#                 F = (x or y) and not (y == z) and not (w)
#
#                 print(x, y, z, w, F)
# for a in 0, 1:
#      for b in 0, 1:
#           for c in 0, 1:
#               F = not (a or b) and c
#
#               print(a, b, c, F)
# for x in 0, 1:
#    for y in 0, 1:
#       for z in 0, 1:
#           f = not x or not y <= z
#
#           print(x, y, z, f)
# for s1 in 0, 1:
#    for s2 in 0, 1:
#       for s3 in 0, 1:
#           f = s1 and not s2 or s3
#           if f:
#            print (s1, s2, s3, f)
for x in 0, 1:
   for y in 0, 1:
      for z in 0, 1:
          f = not x == y or z
            print(x, y, z, f)