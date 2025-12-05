# Day 5: Cafeteria

## Narrative

The Elves discover a cafeteria behind a broken wall but face a crisis: their new inventory management system won't let them determine which ingredients are fresh versus spoiled. You're given a database to solve this problem.

## Part 1

**Input Structure:**
The database contains:
1. A list of fresh ingredient ID ranges (inclusive)
2. A blank line separator
3. A list of available ingredient IDs to check

**Rules:**
- Ranges like "3-5" mean IDs 3, 4, and 5 are fresh
- Ranges can overlap; an ID is fresh if it matches *any* range
- Spoiled IDs don't fall into any fresh range

**Task:** Count how many available ingredient IDs are fresh.

## Example

Given ranges 3-5, 10-14, 16-20, 12-18 and available IDs 1, 5, 8, 11, 17, 32:
- Fresh: 5, 11, 17 (count = 3)
- Spoiled: 1, 8, 32

---

[View on Advent of Code](https://adventofcode.com/2025/day/5)
