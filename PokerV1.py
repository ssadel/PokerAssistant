#PokerV1.py
#Sid Sadel
#this program will take 5-7 cards and determine what hand they make in texas holdem poker
from tkinter import *

global suits 
suits=['D', 'S', 'H', 'C']

global values
values = {"T":'10', "J":'11', "Q":'12', "K":'13', "A":'14'}


def nakedHand(hand):
    naked_hand=hand
    for index, value in enumerate(naked_hand): #gets rid of suit so just card value
        naked_hand[index]=value[0]
    for index, value in enumerate(naked_hand): #makes all values a number
        if value in values.keys():
            naked_hand[index]=values.get(value)
    for index, value in enumerate(naked_hand):
        naked_hand[index]=int(value)
    naked_hand.sort()
    return naked_hand

def suitHand(hand):
    suit_hand=hand
    for index, value in enumerate(suit_hand):
        value=str(value)
        suit_hand[index]=value[1]
    suit_hand.sort()
    return suit_hand


def royalFlush(naked_hand, suit_hand):
    flus=False
    land=False
    high_str8=False

    for index, value in enumerate(naked_hand):
        if naked_hand.count(value) >= 2:
            naked_hand.pop(index)

    amt=len(naked_hand)

    if amt==5:
        if naked_hand[4]==14 and naked_hand[1] - naked_hand[0] == 1 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1:
            high_str8=True
    elif amt==6:
        if naked_hand[4]==14 and naked_hand[1] - naked_hand[0] == 1 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1:
            high_str8=True
        elif naked_hand[5]==14 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1 and naked_hand[5] - naked_hand[4] == 1:
            high_str8=True
    elif amt==7:
        if naked_hand[4]==14 and naked_hand[1] - naked_hand[0] == 1 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1:
            high_str8=True
        elif naked_hand[5]==14 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1 and naked_hand[5] - naked_hand[4] == 1:
            high_str8=True
        elif naked_hand[6]==14 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1 and naked_hand[5] - naked_hand[4] == 1 and naked_hand[6] - naked_hand[5] == 1:
            high_str8=True

    for i in suits:
        if suit_hand.count(i)>=5:
            flus=True
    if flus == True and high_str8 == True:
        land=True
    return land

def straightFlush(naked_hand, suit_hand):
    land=False
    flus=False
    str8=False

    amt=len(naked_hand)
    for index, value in enumerate(naked_hand):
        if naked_hand.count(value) >= 2:
            naked_hand.pop(index)

    if amt==5:
        if naked_hand[1] - naked_hand[0] == 1 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1:
            str8=True
    elif amt==6:
        if naked_hand[1] - naked_hand[0] == 1 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1:
            str8=True
        elif naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1 and naked_hand[5] - naked_hand[4] == 1:
            str8=True
    elif amt==7:
        if naked_hand[1] - naked_hand[0] == 1 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1:
            str8=True
        elif naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1 and naked_hand[5] - naked_hand[4] == 1:
            str8=True
        elif naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1 and naked_hand[5] - naked_hand[4] == 1 and naked_hand[6] - naked_hand[5] == 1:
            str8=True

    for i in suits:
        if suit_hand.count(i)>=5:
            flus=True

    if flus == True and str8 == True:
        land=True
    return land

def fourOfAKind(naked_hand):
    land=False
    for i in range(2, 15):
        if naked_hand.count(i)==4:
            land=True
    return land

def fullHouse(naked_hand):
    land=False
    dos=False
    tres=False
    for i in naked_hand:
        if naked_hand.count(i)==2:
            dos=True
        elif naked_hand.count(i)==3:
            tres=True
    if dos == True and tres == True:
        land=True
    return land

def flush(suit_hand):
    land=False
    for i in suits:
        if suit_hand.count(i)>=5:
            land=True
    return land

def straight(naked_hand):
    land=False

    amt=len(naked_hand)
    for index, value in enumerate(naked_hand):
        if naked_hand.count(value) >= 2:
            naked_hand.pop(index)

    if amt==5:
        if naked_hand[1] - naked_hand[0] == 1 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1:
            land=True
    elif amt==6:
        if naked_hand[1] - naked_hand[0] == 1 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1:
            land=True
        elif naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1 and naked_hand[5] - naked_hand[4] == 1:
            land=True
    elif amt==7:
        if naked_hand[1] - naked_hand[0] == 1 and naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1:
            land=True
        elif naked_hand[2] - naked_hand[1] == 1 and naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1 and naked_hand[5] - naked_hand[4] == 1:
            land=True
        elif naked_hand[3] - naked_hand[2] == 1 and naked_hand[4] - naked_hand[3] == 1 and naked_hand[5] - naked_hand[4] == 1 and naked_hand[6] - naked_hand[5] == 1:
            land=True
    return land

def threeOfAKind(naked_hand):
    land=False
    for i in range(2, 15):
        if naked_hand.count(i)==3:
            land=True
    return land

def twoPair(naked_hand):
    land=False
    x=0
    for i in naked_hand:
        if naked_hand.count(i)==2:
            x+=1
    if x==4: #each number gets counted twice in 2 pair, hence 4
        land=True
    return land

def pair(naked_hand):
    land=False
    for i in range(2, 15):
        if naked_hand.count(i)==2:
            land=True
    return land

def highCard(naked_hand):
    land=False 
    a=max(naked_hand)
    return True

#---main---
root=Tk()
root.title("Poker Assistant")

#---declare---
welcome = Label(root, text="Welcome to Poker Assistant\nBy Sid Sadel\n\nPlease select 5-7 cards and press Enter!")
e = Entry(root)

def press_enter():
    new_window=Toplevel(root)
    new_window.title("Show Hands")
    welcome=Label(new_window, text="your hand is")
    welcome.pack()
    #strip and split, get into list, add switch and functions
    a=e.get()
    b=a[0:-3]
    lst=b.split(" | ")
    hand=[]
    for i in lst:
        new=i[0]+i[2]
        hand.append(new)

    #delete thus print later - - - - - - - - - -
    print(hand)

    #send list of hand to naked_hand (no suit list) and suit_hand (no value just suit)
    naked_hand=nakedHand(hand.copy())
    suit_hand=suitHand(hand.copy())
    #account for naked_hand changing in functions that check for str8 (gets rid of repition)
    naked_hand2=naked_hand.copy()
    naked_hand3=naked_hand.copy()

    hand_switch="a"
    #check all 10 hands from rf down to high card
    if royalFlush(naked_hand, suit_hand)==True:
        print("royale flush")
        hand_switch="Royale Flush"
    elif straightFlush(naked_hand, suit_hand)==True:
        print("straight flush")
        hand_switch="Straight Flush"
    elif fourOfAKind(naked_hand2)==True:
        print("four of a kind")
        hand_switch="Four of a Kind"
    elif fullHouse(naked_hand2)==True:
        print("full house")
        hand_switch="Full House"
    elif flush(suit_hand)==True:
        print("flush")
        hand_switch="Flush"
    elif straight(naked_hand2)==True:
        print("straight")
        hand_switch="Straight"
    elif threeOfAKind(naked_hand3)==True:
        print("three of a kind")
        hand_switch="Three of a Kind"
    elif twoPair(naked_hand3)==True:
        print("two pair")
        hand_switch="Two Pair"
    elif pair(naked_hand3)==True:
        print("pair")
        hand_switch="Pair"
    elif highCard(naked_hand3)==True:
        print("high card")
        hand_switch="High Card"
    else:
        print("sum went wrong")
        hand_switch="error"

    hand_label=Label(new_window, text=hand_switch)
    hand_label.pack()
    exit=Button(new_window, text="Return", command=new_window.destroy)
    exit.pack()

def click_card(n):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(n)+' | ')

def clear():
    e.delete(0, END)

#buttons
buttons_frame=LabelFrame(root, padx=5, pady=5)
enter = Button(buttons_frame, text="Enter", command=press_enter)
clear_button=Button(buttons_frame, text="Clear", command=clear)

hearts_frame = LabelFrame(root, padx=5, pady=5)
h2=Button(hearts_frame, text="2 H", command=lambda: click_card("2 H"))
h3=Button(hearts_frame, text="3 H", command=lambda: click_card("3 H"))
h4=Button(hearts_frame, text="4 H", command=lambda: click_card("4 H"))
h5=Button(hearts_frame, text="5 H", command=lambda: click_card("5 H"))
h6=Button(hearts_frame, text="6 H", command=lambda: click_card("6 H"))
h7=Button(hearts_frame, text="7 H", command=lambda: click_card("7 H"))
h8=Button(hearts_frame, text="8 H", command=lambda: click_card("8 H"))
h9=Button(hearts_frame, text="9 H", command=lambda: click_card("9 H"))
hT=Button(hearts_frame, text="T H", command=lambda: click_card("T H"))
hJ=Button(hearts_frame, text="J H", command=lambda: click_card("J H"))
hQ=Button(hearts_frame, text="Q H", command=lambda: click_card("Q H"))
hK=Button(hearts_frame, text="K H", command=lambda: click_card("K H"))
hA=Button(hearts_frame, text="A H", command=lambda: click_card("A H"))

spades_frame = LabelFrame(root, padx=5, pady=5)
s2=Button(spades_frame, text="2 S", command=lambda: click_card("2 S"))
s3=Button(spades_frame, text="3 S", command=lambda: click_card("3 S"))
s4=Button(spades_frame, text="4 S", command=lambda: click_card("4 S"))
s5=Button(spades_frame, text="5 S", command=lambda: click_card("5 S"))
s6=Button(spades_frame, text="6 S", command=lambda: click_card("6 S"))
s7=Button(spades_frame, text="7 S", command=lambda: click_card("7 S"))
s8=Button(spades_frame, text="8 S", command=lambda: click_card("8 S"))
s9=Button(spades_frame, text="9 S", command=lambda: click_card("9 S"))
sT=Button(spades_frame, text="T S", command=lambda: click_card("T S"))
sJ=Button(spades_frame, text="J S", command=lambda: click_card("J S"))
sQ=Button(spades_frame, text="Q S", command=lambda: click_card("Q S"))
sK=Button(spades_frame, text="K S", command=lambda: click_card("K S"))
sA=Button(spades_frame, text="A S", command=lambda: click_card("A S"))

clubs_frame = LabelFrame(root, padx=5, pady=5)
c2=Button(clubs_frame, text="2 C", command=lambda: click_card("2 C"))
c3=Button(clubs_frame, text="3 C", command=lambda: click_card("3 C"))
c4=Button(clubs_frame, text="4 C", command=lambda: click_card("4 C"))
c5=Button(clubs_frame, text="5 C", command=lambda: click_card("5 C"))
c6=Button(clubs_frame, text="6 C", command=lambda: click_card("6 C"))
c7=Button(clubs_frame, text="7 C", command=lambda: click_card("7 C"))
c8=Button(clubs_frame, text="8 C", command=lambda: click_card("8 C"))
c9=Button(clubs_frame, text="9 C", command=lambda: click_card("9 C"))
cT=Button(clubs_frame, text="T C", command=lambda: click_card("T C"))
cJ=Button(clubs_frame, text="J C", command=lambda: click_card("J C"))
cQ=Button(clubs_frame, text="Q C", command=lambda: click_card("Q C"))
cK=Button(clubs_frame, text="K C", command=lambda: click_card("K C"))
cA=Button(clubs_frame, text="A C", command=lambda: click_card("A C"))

diamonds_frame = LabelFrame(root, padx=5, pady=5)
d2=Button(diamonds_frame, text="2 D", command=lambda: click_card("2 D"))
d3=Button(diamonds_frame, text="3 D", command=lambda: click_card("3 D"))
d4=Button(diamonds_frame, text="4 D", command=lambda: click_card("4 D"))
d5=Button(diamonds_frame, text="5 D", command=lambda: click_card("5 D"))
d6=Button(diamonds_frame, text="6 D", command=lambda: click_card("6 D"))
d7=Button(diamonds_frame, text="7 D", command=lambda: click_card("7 D"))
d8=Button(diamonds_frame, text="8 D", command=lambda: click_card("8 D"))
d9=Button(diamonds_frame, text="9 D", command=lambda: click_card("9 D"))
dT=Button(diamonds_frame, text="T D", command=lambda: click_card("T D"))
dJ=Button(diamonds_frame, text="J D", command=lambda: click_card("J D"))
dQ=Button(diamonds_frame, text="Q D", command=lambda: click_card("Q D"))
dK=Button(diamonds_frame, text="K D", command=lambda: click_card("K D"))
dA=Button(diamonds_frame, text="A D", command=lambda: click_card("A D"))

kill=Button(root, text="Exit", command=root.quit)



#---position---
welcome.pack()
e.pack()
buttons_frame.pack()
enter.pack(side=RIGHT)
clear_button.pack()

#hearts
hearts_frame.pack(padx=5, pady=5)
h2.grid(row=0, column=0)
h3.grid(row=0, column=1)
h4.grid(row=0, column=2)
h5.grid(row=0, column=3)
h6.grid(row=0, column=4)
h7.grid(row=0, column=5)
h8.grid(row=0, column=6)
h9.grid(row=1, column=0)
hT.grid(row=1, column=1)
hJ.grid(row=1, column=2)
hQ.grid(row=1, column=3)
hK.grid(row=1, column=4)
hA.grid(row=1, column=5)

#spades
spades_frame.pack(padx=5, pady=5)
s2.grid(row=0, column=0)
s3.grid(row=0, column=1)
s4.grid(row=0, column=2)
s5.grid(row=0, column=3)
s6.grid(row=0, column=4)
s7.grid(row=0, column=5)
s8.grid(row=0, column=6)
s9.grid(row=1, column=0)
sT.grid(row=1, column=1)
sJ.grid(row=1, column=2)
sQ.grid(row=1, column=3)
sK.grid(row=1, column=4)
sA.grid(row=1, column=5)

#clubs
clubs_frame.pack(padx=5, pady=5)
c2.grid(row=0, column=0)
c3.grid(row=0, column=1)
c4.grid(row=0, column=2)
c5.grid(row=0, column=3)
c6.grid(row=0, column=4)
c7.grid(row=0, column=5)
c8.grid(row=0, column=6)
c9.grid(row=1, column=0)
cT.grid(row=1, column=1)
cJ.grid(row=1, column=2)
cQ.grid(row=1, column=3)
cK.grid(row=1, column=4)
cA.grid(row=1, column=5)

#diamonds
diamonds_frame.pack(padx=5, pady=5)
d2.grid(row=0, column=0)
d3.grid(row=0, column=1)
d4.grid(row=0, column=2)
d5.grid(row=0, column=3)
d6.grid(row=0, column=4)
d7.grid(row=0, column=5)
d8.grid(row=0, column=6)
d9.grid(row=1, column=0)
dT.grid(row=1, column=1)
dJ.grid(row=1, column=2)
dQ.grid(row=1, column=3)
dK.grid(row=1, column=4)
dA.grid(row=1, column=5)

kill.pack()

root.mainloop()