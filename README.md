# Project 3: Bug Fixing (C++)

Two common bugs, how to spot them, and the corrected code with tests.

## Description
The file contains the buggy functions in comments, an explanation of each bug, and the fixed versions. A `main` function runs `assert` tests that would fail on the buggy code and pass on the fixed code.

## Bugs Found and Fixed
| Bug | Cause | Fix |
|---|---|---|
| Wrong sum, possible crash | Loop used `i <= size`, reading one element past the end of the array | Use `i < arr.size()` |
| Wrong maximum for negative numbers | Maximum started at `0`, so an all-negative array returned `0` | Start from the first element, `arr[0]` |

## Technologies
- C++17
- Standard library: `iostream`, `vector`, `cassert`

## Setup and Run
```
g++ -std=c++17 project3_bug_fixing.cpp -o bugfix
./bugfix
```

## Example Output
```
Sum of {1,2,3,4}: 10
Max of {-8,-3,-15}: -3
All tests passed.
```

## Notes
The bugs are example bugs that demonstrate the debugging process. If your assignment requires the specific buggy program you fixed in class, replace the examples with it.

## Author
Prathvi Singh
