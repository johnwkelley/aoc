# Day 12: Christmas Tree Farm

## Narrative

The puzzle is set in a North Pole cavern filled with Christmas trees. Elves need to place presents of various shapes under trees before a deadline. The challenge is determining whether presents can physically fit into designated regions without overlapping.

## Part 1 Requirements

The puzzle provides:
1. **Present shapes**: Six unique 2D shapes made of unit squares, labeled 0-5
2. **Regions**: Multiple rectangular areas with specified dimensions and required present quantities

**Key constraints:**
- Presents can be "rotated and flipped as necessary to make them fit"
- Presents cannot overlap (the solid parts cannot share grid spaces)
- The `.` portions of shapes don't block other presents from occupying that space
- Presents must align perfectly to the grid

**Task:** How many of the regions can fit all of the presents listed?

In the provided example with three regions, exactly two regions successfully accommodate all required presents, while the third region cannot fit one additional present despite having enough total area.

---

[View on Advent of Code](https://adventofcode.com/2025/day/12)
