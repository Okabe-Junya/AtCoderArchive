N, A, X, Y = gets.split.map(&:to_i)
if A > N
    puts X * N
else
    puts X * A + Y * (N - A)
end