package main

import "fmt"

func main() {
	var X, Y int
	flag := true
	fmt.Scan(&X, &Y)
	for i := 0; i < X+1; i++ {
		if 2*i+4*(X-i) == Y {
			fmt.Print("Yes\n")
			flag = false
			break
		}
	}
	if flag {
		fmt.Print("No\n")
	}
}
