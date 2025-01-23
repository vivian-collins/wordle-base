#!/usr/bin/env python3
import sys

# Error codes:
# 2: system error in the program
# 1: valid submission, not right word
# 0: correct word

# Note: this may not handle "multiple same letters" very well
# Feel free to try to improve the logic

if len(sys.argv) != 3:
  sys.exit(2)

target = sys.argv[1].upper()
guess = sys.argv[2].upper()
if len(target) != 5 or len(guess) != 5:
  sys.exit(2)

if guess == target:
  sys.exit(0)
for i in range(0,5):
  ch = guess[i]
  if ch == target[i]:
    print(f"{ch}: Correct")
  elif ch in target:
    print(f"{ch}: Wrong place")
  else:
    print(f"{ch}: Not there")
sys.exit(1)
