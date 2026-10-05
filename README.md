# Test Error Demo

This project demonstrates a TEST failure.

The application code is correct, but one test contains an incorrect expected value.

## Expected

BUILD -> PASS
TESTS -> FAIL

## Error

3 * 4 actually produces 12.

The test incorrectly expects 13.

## Fix

Change:

assert multiply(3, 4) == 13

to:

assert multiply(3, 4) == 12
