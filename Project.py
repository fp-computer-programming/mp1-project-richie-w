# Creator RW 10/28/22

#Nouns w1 w19 w20 w21
#Verbs w2
#Adjectives w3 w4 w5 w8 w13 w16 
#Places w6 w11
#Plural nouns w7 w9
#Body part w10
#Number w12 w17
#Food w14
#Body motion w15
#Language w18

#inputs for madlib answers ; creating variables

w1 = input("Noun")
w2 = input("verb")
w3 = input("Adjective")
w4 = input("Adjective")
w5 = input("Adjective")
w6 = input("Place")
w7 = input("Plural noun")
w8 = input("Adjective")
w9 = input("Plural noun")
w10 = input("Body part")
w11 = input("Place")
w12 = input("Number")
w13 = input("Adjective")
w14 = input("Food")
w15 = input("Body motion")
w16 = input("Adjective")
w17 = input("Number")
w18 = input("Language")
w19 = input("Noun")
w20 = input("Noun")
w21= input("Noun")

# Completed Madlib with inputs and variables included

Madlib = """The rainfalls in the """+w1+""" as the Jesuits are very """+w2+""" because the natives are told to be """+w3+""".
They walk upon the """+w4+""" pathway which leads to a """+w5+"""  """+w6+""".
There, they meet the natives who hold """+w7+""".
The Jesuits remain """+w8+""" as they give the natives a bucket of """+w9+""" as a peace offering.
The natives accept the offer, then grab one of the Jesuits """+w10+""" and lead them to """+w11+"""
.There, they meet """+w12+""" other natives who look """+w13+""".
The Jesuits begin to hand out their gifts as the natives give back a/an """+w14+"""to repay the Jesuits for their kindness.
The Jesuits thank them by """+w15+""" and the natives copy them. 
The Jesuits then attempt to communicate with the """+w16+""" natives.
After """+w17+""" years, some of the natives have learned """+w18+""" so they could read the """+w19+""" and talk to the Jesuits. 
Throughout the years, the natives and Jesuits had made a village with a large """+w20+""" in front of their """+w21+""" """

#Preventing w1 from equaling other inputs
if w1 == w19 or w1 == w20 or w1 == w21:
    print("Use a different input")

#Preventing w3 from equaling different inputs
if w3 == w4 or w3 == w5 or w3 == w8 or w3 == w13 or w3 == w16:
    print("Use a different input")

#Preventing w4 from equaling other inputs
if w4 == w3 or w4 == w5 or w4 == w8 or w4 == w13 or w4 == w16:
    print("Use a different input")

#Preventing w5 from equaling other inputs
if w5 == w3 or w5 == w4 or w5 == w8 or w5 == w13 or w5 == w16:
    print("Use a different input")

#Preventing w6 from equaling other inputs
if w6 == w11:
    print("Use a different input")

#Preventing w7 from equaling other inputs
if w7 == w9:
    print("Use a different input")

#Preventing w8 from equaling other inputs
if w8 == w3 or w8 == w4 or w8 == w5 or w8 == w13 or w8 == w16:
    print("Use a different input")

#Preventing w9 from equaling other inputs
if w9 == w7:
    print("Use a different input")

#Preventing w11 from equaling other inputs
if w11 == w6:
    print("Use a different input")

#Preventing w12 from equaling other inputs
if w12 == w17:
    print("Use a different input")

#Preventing w13 from equaling other inputs
if w13 == w3 or w13 == w4 or w13 == w5 or w13 == w8 or w13 == w16:
    print("Use a different input")

#Preventing w16 from equaling other inputs
if w16 == w3 or w16 == w4 or w16 == w5 or w16 == w8 or w16 == w13:
    print("Use a different input")

#Preventing w17 from equaling other inputs
if w17 == w12:
    print("Use a different input")

#Preventing w19 from equaling other inputs
if w19 == w1 or w19 == w20 or w19 == w21:
    print ("Use a different input")

#Preventing w20 from equaling other inputs
if w20 == w1 or w20 == w19 or w20 == w21:
    print("Use a different input")

#Preventing w21 from equaling other inputs
if w21 == w1 or w21 == w19 or w21 == w20:
    print("Use a different input")

else: 
    print(Madlib)


