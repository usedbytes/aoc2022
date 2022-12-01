package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime/pprof"
	"sort"
	"strconv"
)

func doLines(filename string, do func(line string) error) error {
	f, err := os.Open(filename)
	if err != nil {
		return err
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		if err := do(line); err != nil {
			return err
		}
	}

	if err := scanner.Err(); err != nil {
		return err
	}

	return nil
}

func run() error {
	elves := []int{}
	elf := 0

	if err := doLines(os.Args[1], func(line string) error {
		if len(line) == 0 {
			elves = append(elves, elf)
			elf = 0
			return nil
		}

		v, err := strconv.Atoi(line)
		if err != nil {
			return err
		}

		elf += v

		return nil
	}); err != nil {
		return err
	}

	// No trailing blank line
	elves = append(elves, elf)

	sort.Ints(elves)

	fmt.Println("Part 1:", elves[len(elves)-1])
	fmt.Println("Part 2:", elves[len(elves)-1] + elves[len(elves)-2] + elves[len(elves)-3])

	return nil
}

func main() {
	profileEnv := os.Getenv("PROFILE")
	if profileEnv != "" {
		f, err := os.Create(profileEnv)
		if err != nil {
			fmt.Println("ERROR:", err)
			os.Exit(1)
		}

		pprof.StartCPUProfile(f)
		defer pprof.StopCPUProfile()
	}

	err := run()
	if err != nil {
		fmt.Println("ERROR:", err)
		os.Exit(1)
	}
}
