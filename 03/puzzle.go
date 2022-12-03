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

func intersect(a, b string) string {
	var result string
	for _, c := range a {
		if strings.ContainsRune(b, c) {
			if !strings.ContainsRune(result, c) {
				result += string(c)
			}
		}
	}
	return result
}

func getPriority(char byte) int {
	if char >= 'a' && char <= 'z' {
		return int(char - 'a') + 1
	} else if char >= 'A' && char <= 'Z' {
		return int(char - 'A') + 27
	}
	return 0
}

func run() error {
	var total int
	bags := []string{}

	if err := doLines(os.Args[1], func(line string) error {
		// Save the rucksacks for Part 2
		bags = append(bags, line)

		l := len(line)
		cp1 := line[:l/2]
		cp2 := line[l/2:]

		idx := strings.IndexAny(cp2, cp1)
		if idx >= 0 {
			total += getPriority(cp2[idx])
		}

		return nil
	}); err != nil {
		return err
	}

	fmt.Println("Part 1:", total)

	// Part 2
	total = 0
	for i := 0; i < len(bags); i += 3 {
		result := intersect(bags[i], intersect(bags[i+1], bags[i+2]))
		if len(result) != 1 {
			panic(result)
		}
		total += getPriority(result[0])
	}
	fmt.Println("Part 2:", total)

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
