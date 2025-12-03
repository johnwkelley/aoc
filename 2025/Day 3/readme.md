# Day 3: Lobby

## Narrative

You've entered a vast lobby where all elevators are offline due to an electrical surge. An Elf suggests using an escalator to reach the printing department, but it also needs power. Nearby batteries can provide emergency power, each labeled with a joltage rating from 1 to 9.

## Part 1: The Challenge

**Problem Setup:**
Each line of input represents a "bank" of batteries. Within each bank, you must select exactly two batteries to activate. The joltage produced equals the number formed by concatenating the digits of those two batteries in their original positions.

**Task:** Find the maximum joltage possible from each bank; what is the total output joltage?

## Example

Given four battery banks:
- `987654321111111` -> activate positions with `9` and `8` = `98` jolts
- `811111111111119` -> activate `8` and `9` = `89` jolts
- `234234234234278` -> activate `7` and `8` = `78` jolts
- `818181911112111` -> activate `9` and `2` = `92` jolts

Sum: 98 + 89 + 78 + 92 = **357 jolts**

---

[View on Advent of Code](https://adventofcode.com/2025/day/3)
