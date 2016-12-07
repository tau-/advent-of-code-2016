# Advent of Code 2016

Solutions to the [Advent of Code](http://adventofcode.com/2016) calendar problems for 2016
in Python3 and Clojure.

## Write your own!

Solutions will be posted as I write them, but you can use this project to make your own.

Save your input to `input/01.txt`, `input/02.txt`, etc. Then, write your solution and tests for each
day in the corresponding `.clj` and `.py` files.

## Development

### Build Environment

Leiningen 2.7.1 on Java 1.8.0_66 OpenJDK 64-Bit Server VM. Python 3.5.1.

### Python 3

Use the included `solve.py` script to run one or all of the python solutions. Display all solutions with

```
$ python3 solve.py
```

Compute the solution for a single day with 

```
$ python3 solve.py 1
```

### Leiningen

Generate, display, and save all solutions with

```
$ lein run
```

Compute the solutions for a single day, e.g., day 1, with

```
$ lein run 1
```

or in the REPL (`$ lein repl`) with

```clojure
(solve-day 1)
```

## License

This software is licensed under the MIT license.

## Warranty

This work is provided "as is" and without any express or
implied warranties, including, without limitation, the implied
warranties of merchantibility and fitness for a particular
purpose.
