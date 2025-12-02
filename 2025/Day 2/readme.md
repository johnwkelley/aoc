# Day 2: Gift Shop

## Narrative

You're in the North Pole gift shop and an Elf needs help removing invalid product IDs from their database. A younger Elf accidentally added IDs following a specific pattern while playing on a computer.

## Part 1: Invalid ID Pattern

An ID is invalid if it consists of "a sequence of digits repeated twice." Examples include:
- `55` (5 repeated)
- `6464` (64 repeated)
- `123123` (123 repeated)

**Important Constraint:** Numbers have no leading zeroes, so `0101` isn't valid, but `101` is a legitimate ID to ignore.

**Task:** Given ranges of product IDs separated by commas (format: `start-end`), identify all invalid IDs within those ranges and sum them.

## Example Walkthrough

From the provided ranges, invalid IDs are found in:
- `11-22`: contains `11`, `22`
- `95-115`: contains `99`
- `998-1012`: contains `1010`
- `1188511880-1188511890`: contains `1188511885`
- `222220-222224`: contains `222222`
- `446443-446449`: contains `446446`
- `38593856-38593862`: contains `38593859`

The example's total: **1227775554**

## Part 2

Part 2 extends the pattern - an ID is invalid if it consists of *any* repeating pattern (not just doubled).

---

[View on Advent of Code](https://adventofcode.com/2025/day/2)
