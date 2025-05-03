# Python Async Comprehension

This project demonstrates the use of asynchronous programming in Python, specifically focusing on async generators and async comprehensions.

## Requirements

- Python 3.9
- Ubuntu 20.04 LTS
- pycodestyle (version 2.5.x)

## Files

### 0-async_generator.py
An asynchronous generator that yields random numbers between 0 and 10. The generator:
- Yields a random float between 0 and 10
- Does this 10 times
- Waits 1 second between each yield

### 1-async_comprehension.py
A coroutine that uses async comprehension to collect random numbers. The function:
- Takes no arguments
- Uses async comprehension to collect 10 random numbers from async_generator
- Returns a list of 10 random numbers between 0 and 10

## Usage

To run the example:

```bash
./1-main.py
```

Example output:
```
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
```

## Author
Nour Kasmi 