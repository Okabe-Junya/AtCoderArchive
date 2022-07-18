package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	idxmap := make(map[int]int)
	for i := 0; i < N; i++ {
		var a int
		fmt.Scan(&a)
		A[i] = a
		idxmap[a] = i
	}
	sort.Ints(A)
	fmt.Print(idxmap[A[N-2]]+1, "\n")
}
