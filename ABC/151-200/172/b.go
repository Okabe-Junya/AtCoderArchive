package main

import (
	"bufio"
	"fmt"
	"os"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	var S, T string
	if sc.Scan() {
		S = sc.Text()
	}
	if sc.Scan() {
		T = sc.Text()
	}

	var ans int64
	for i := 0; i < len(S); i++ {
		if S[i] != T[i] {
			ans += 1
		}
	}
	fmt.Print(ans, "\n")
}
