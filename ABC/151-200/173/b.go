package main

import (
	"bufio"
	"fmt"
	"os"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	var N int
	fmt.Scan(&N)
	dict := map[string]int{"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
	for {
		if sc.Scan() {
			S := sc.Text()
			dict[S] += 1
		} else {
			break
		}
	}
	fmt.Printf("AC x %d\n", dict["AC"])
	fmt.Printf("WA x %d\n", dict["WA"])
	fmt.Printf("TLE x %d\n", dict["TLE"])
	fmt.Printf("RE x %d\n", dict["RE"])
}
