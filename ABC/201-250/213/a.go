package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	for c := 0; c < 256; c++ {
		if a^c == b {
			fmt.Printf("%d\n", c)
		}
	}
}
