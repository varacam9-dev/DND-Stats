import random
import time
from tkinter import *

minimum = 1
maximum = 6

# Stat #1
print("Rolling First Stat")

# rolling 4 dies for stats

die1 = random.randint(minimum, maximum)
print("Die 1 is " + str(die1))


die2 = random.randint(minimum, maximum)
print("Die 2 is " + str(die2))


die3 = random.randint(minimum, maximum)
print("Die 3 is " + str(die3))

die4 = random.randint(minimum, maximum)
print("Die 4 is " + str(die4))


total_roll = die1+die2+die3+die4

# Seeing which one is the lowest roll
low = die1
if die2 < low:
  low = die2
if die3 < low:
  low = die3
if die4 < low:
  low = die4

print("Lowest Roll is " + str(low))


# drop the lowest roll

stat1 = total_roll - low

#print final stat
print("Final Stat #1 is " + str(stat1))

# Stat #2

print("Rolling Second Stat")

# rolling 4 dies for stats

die1 = random.randint(minimum, maximum)
print("Die 1 is " + str(die1))


die2 = random.randint(minimum, maximum)
print("Die 2 is " + str(die2))


die3 = random.randint(minimum, maximum)
print("Die 3 is " + str(die3))

die4 = random.randint(minimum, maximum)
print("Die 4 is " + str(die4))


total_roll = die1+die2+die3+die4

# Seeing which one is the lowest roll
low = die1
if die2 < low:
  low = die2
if die3 < low:
  low = die3
if die4 < low:
  low = die4

print("Lowest Roll is " + str(low))


# drop the lowest roll

stat2 = total_roll - low

#print final stat
print("Final Stat #2 is " + str(stat2))

# Stat #3
print("Rolling Thrid Stat")

# rolling 4 dies for stats

die1 = random.randint(minimum, maximum)
print("Die 1 is " + str(die1))


die2 = random.randint(minimum, maximum)
print("Die 2 is " + str(die2))


die3 = random.randint(minimum, maximum)
print("Die 3 is " + str(die3))

die4 = random.randint(minimum, maximum)
print("Die 4 is " + str(die4))


total_roll = die1+die2+die3+die4

# Seeing which one is the lowest roll
low = die1
if die2 < low:
  low = die2
if die3 < low:
  low = die3
if die4 < low:
  low = die4

print("Lowest Roll is " + str(low))


# drop the lowest roll

stat3 = total_roll - low

#print final stat
print("Final Stat #3 is " + str(stat3))


# Stat #4
print("Rolling First Stat")

# rolling 4 dies for stats

die1 = random.randint(minimum, maximum)
print("Die 1 is " + str(die1))


die2 = random.randint(minimum, maximum)
print("Die 2 is " + str(die2))


die3 = random.randint(minimum, maximum)
print("Die 3 is " + str(die3))

die4 = random.randint(minimum, maximum)
print("Die 4 is " + str(die4))


total_roll = die1+die2+die3+die4

# Seeing which one is the lowest roll
low = die1
if die2 < low:
  low = die2
if die3 < low:
  low = die3
if die4 < low:
  low = die4

print("Lowest Roll is " + str(low))


# drop the lowest roll

stat4 = total_roll - low

#print final stat
print("Final Stat #4 is " + str(stat4))


# Stat #1
print("Rolling First Stat")

# rolling 4 dies for stats

die1 = random.randint(minimum, maximum)
print("Die 1 is " + str(die1))


die2 = random.randint(minimum, maximum)
print("Die 2 is " + str(die2))


die3 = random.randint(minimum, maximum)
print("Die 3 is " + str(die3))

die4 = random.randint(minimum, maximum)
print("Die 4 is " + str(die4))


total_roll = die1+die2+die3+die4

# Seeing which one is the lowest roll
low = die1
if die2 < low:
  low = die2
if die3 < low:
  low = die3
if die4 < low:
  low = die4

print("Lowest Roll is " + str(low))


# drop the lowest roll

stat5 = total_roll - low

#print final stat
print("Final Stat #5 is " + str(stat5))

# Stat #1
print("Rolling First Stat")

# rolling 4 dies for stats

die1 = random.randint(minimum, maximum)
print("Die 1 is " + str(die1))


die2 = random.randint(minimum, maximum)
print("Die 2 is " + str(die2))


die3 = random.randint(minimum, maximum)
print("Die 3 is " + str(die3))

die4 = random.randint(minimum, maximum)
print("Die 4 is " + str(die4))


total_roll = die1+die2+die3+die4

# Seeing which one is the lowest roll
low = die1
if die2 < low:
  low = die2
if die3 < low:
  low = die3
if die4 < low:
  low = die4

print("Lowest Roll is " + str(low))


# drop the lowest roll

stat6 = total_roll - low

#print final stat
print("Final Stat #6 is " + str(stat6))


print("Your stats are "+ str(stat1)+ " " +str(stat2)+" " +str(stat3)+" " +str(stat4)+" " +str(stat5)+" " +str(stat6))

print("")

window = Tk()
window.title("Rolling Starting Stats")

top_frame = Frame(window)
top_frame.pack()

bottom_frame = Frame(window)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="First Stat", fg="red")
button1.pack()

window.mainloop()

