package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime/pprof"
	"strings"
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

	var total int
	if err := doLines(os.Args[1], func(line string) error {
		l := len(line)
		cp1 := line[:l/2]
		cp2 := line[l/2:]

		idx := strings.IndexAny(cp2, cp1)
		if idx >= 0 {
			var prio int
			char := cp2[idx]
			if char >= 'a' && char <= 'z' {
				prio = int(char - 'a') + 1
			} else if char >= 'A' && char <= 'Z' {
				prio = int(char - 'A') + 27
			}
			total += prio
		}

		return nil
	}); err != nil {
		return err
	}

	fmt.Println("Part 1:", total)

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
