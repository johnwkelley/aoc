# Day 10: Factory

## Story

The Elves have discovered a factory with offline machines. The initialization manual was partially eaten by a Shiba Inu, leaving only indicator light diagrams, button schematics, and joltage requirements.

## Part 1: Minimum Button Presses

**The Core Challenge:**
Configure indicator lights on machines by pressing buttons the minimum number of times. Each machine has:
- An indicator light diagram showing the target state (`.` = off, `#` = on)
- Button schematics listing which lights each button toggles
- Buttons can be pressed any non-negative integer number of times

**Key Rules:**
- Each button lists which indicator lights it toggles
- When a button is pressed, listed lights switch states (on->off or off->on)
- Goal: Find the fewest total button presses across all machines

## Example Results

The three provided machines require 2, 3, and 2 button presses respectively, totaling 7 presses.

**Task:** Analyze each machine's indicator light diagram and button wiring schematics. What is the fewest button presses required to correctly configure the indicator lights on all of the machines?

---

[View on Advent of Code](https://adventofcode.com/2025/day/10)
