N, X = gets.split(' ').map(&:to_i)
S = gets.split('')
ans = X
for i in 0..N-1
    if S[i] == 'o'
        ans += 1
    elsif ans > 0
        ans -= 1
    end
end
puts ans