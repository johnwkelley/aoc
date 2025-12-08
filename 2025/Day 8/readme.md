# Day 8: Playground

## Story/Narrative

The protagonist arrives at an underground playground where Elves are setting up a Christmas decoration project. They've suspended electrical junction boxes and plan to connect them with light strings to distribute electricity throughout the system.

## Part 1

**Objective:** Connect junction boxes using the shortest distances possible to form circuits.

**Key Requirements:**
- Given 3D coordinates for junction boxes in `X,Y,Z` format
- Calculate "straight-line distance" (Euclidean distance) between all pairs
- Connect the 1000 closest pairs sequentially
- After connections, identify the three largest circuits by size
- **Answer:** Multiply the sizes of the three largest circuits

## Example Walkthrough

The problem demonstrates that connecting `162,817,812` to `425,690,689` forms a 2-box circuit. Subsequent connections may merge circuits or create new ones. When a connection would join boxes already in the same circuit, nothing happens.

After ten connections in the example, circuits of size 5, 4, and 2 are the three largest, yielding 5 x 4 x 2 = **40**.

---

[View on Advent of Code](https://adventofcode.com/2025/day/8)
