N, X = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
for i in 0..N-1
    if i % 2 == 1
        A[i] -= 1
    end
end
if A.sum <= X
    puts 'Yes'
else
    puts 'No'
end