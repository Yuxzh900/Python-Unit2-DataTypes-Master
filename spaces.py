# def Spaces(N, Y, T):
#     x = 0
#     for i in range(N):
#         if Y[i] == "C" and T[i] == "C":
#             x = x + 1
#     return x

# print(Spaces(5, "CC..C", "CCC.."))







# def wiz(n, start, duels):
#     #who owns the wand
#     #find how to see how wins the duels
#     #find how to make the wand change to the correct owners
#     #count the number of wand changes
#     owner = start
#     numberofowners = 1
#     # check singe battle
#     # check first character
#     # check if wand changes hand
#     for i in range(n):
#         if duels[i][1] == owner:
#             owner = duels[i][0]
#             numberofowners += 1
#     print(owner)
#     print(numberofowners)
# wiz(3, "A", ["BA", "CB", "DA" ])


def en_or_fr(text):
    s = 0
    t = 0
    text = text.lower()
    for i in range(len(text)):
        if text[i] == "s":
        s += 1
    print(s)
en_or_fr("Hello My name is what is your name?")