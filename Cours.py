#TableauEtBoucle
#tonton = [
#    [0,1],
#    [0,2],
#    [0,3],
#    [0,4]
#]

#for i in tonton:
#    print(i)


#for i in tonton:
#    print(i[1])
#

#     *
#    ***
#   *****
#  *******
# *********

# space = " "
# star = "*"

# myTree = [
#     [4,1],
#     [3,3],
#     [2,5],
#     [1,7],
#     [0,9]
# ]

# for i in myTree:
#     a = i[0] * space
#     b = i[1] * star
#     print(a,b)

star = "*"
space = " "

def draw_line(nb_star, nb_space, eq_space=0):

    line = ""
    line += (nb_space + eq_space) * space
    line += nb_star * star
    line += (nb_space + eq_space) * space
    print(line)


def lg_max_calcul(lg_max):
    first_line_stars = 1
    x = first_line_stars
    lg_max = x + 8

lg_max_calcul(13)
word = "bananana"
i = word.find("na")

# def 

# def myTree(nbligne = 5, nbetage= 5):

#     nbspace = nbligne - 1
#     nbstar = 1

#     space = " "
#     star = "*"
#     i=1

#     while nbetage != 0:

#         while nbspace != -1:
#             a = nbspace * space
#             b = nbstar * (star)
#             print(a,b)
#             nbspace -=1
#             nbstar += 2
#         i+=2
#         nbspace = nbligne
#         nbstar = i
#         nbetage -=1

#     return nbligne, nbetage

# myTree()
