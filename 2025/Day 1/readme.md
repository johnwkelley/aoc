# Day 1: Secret Entrance

## Problem Summary

**Narrative:** The Elves have discovered project management but face a critical issue: no one has time to decorate the North Pole by December 12th. You must help by solving puzzles to collect stars. At the secret entrance, you encounter a safe with a dial (numbered 0-99) that requires opening using a sequence of rotations.

## Part 1: The Dial Puzzle

**The Challenge:**
The dial starts pointing at 50. You receive a list of rotations, each formatted as a direction (L for left/lower numbers, R for right/higher numbers) followed by a distance value.

**Key Rules:**
- Rotating left from 0 wraps to 99
- Rotating right from 99 wraps to 0
- The dial is circular with 100 positions

**The Twist:**
The actual password is not the final dial position. Instead, it's "the number of times the dial is left pointing at 0 after any rotation in the sequence."

**Example:**
With rotations like L68, L30, R48, L5, R60, L55, L1, L99, R14, L82, the dial reaches 0 three times, making the password 3.

**Your Task:** Analyze your puzzle input and determine the password by counting how many times the dial points to 0.

## Part 2

Part 2 extends the challenge to count how many times the dial *passes through* 0 during rotations, not just lands on it.

---

[View on Advent of Code](https://adventofcode.com/2025/day/1)
