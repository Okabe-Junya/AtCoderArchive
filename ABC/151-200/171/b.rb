N, K = gets.split(' ').map(&:to_i)
p = gets.split(' ').map(&:to_i)
p.sort!
ans = 0
for i in 0..K-1
    ans += p[i]
end
p ans