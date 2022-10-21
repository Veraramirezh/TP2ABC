# creer par Henrique Vera
# octobre 21
#^program qui demande le nom et le truc de point ou wtv


#on va demander une question
print("Hello world")
Question = str(input(" quelle est votre nom"))


#on print la reponse du lecteur
print("bonjour",Question)

#on repose une autre question pour ensuite demander le noimbre de ranger
print("regarder ceci",Question)
nbrderanger = int(input("combien de ranger detoile voulez vous"))
for i in range(nbrderanger  + 1, 0, -1):
    print("*"* i)