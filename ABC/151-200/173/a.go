package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	if N%1000 == 0 {
		fmt.Print(0, "\n")
	} else {
		fmt.Print(1000-N%1000, "\n")
	}
}
