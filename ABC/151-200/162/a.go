package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	if N/100 == 7 || (N-100*(N/100))/10 == 7 || N%10 == 7 {
		fmt.Print("Yes\n")
	} else {
		fmt.Print("No\n")
	}
}
