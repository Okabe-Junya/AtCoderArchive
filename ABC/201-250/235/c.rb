N, Q = gets.split(' ').map(&:to_i)
a = gets.split(' ').map(&:to_i)

hash = Hash.new([])

for i in 0..Q-1 do
    if hash.key?(a[i])
        hash[a[i]].append(i)
    else
        hash[a[i]] = [i]
    end
end

for i in 1..Q do
    x, k = gets.split(' ').map(&:to_i)
    if hash[x].count >= k
        puts hash[x][k - 1] + 1
    else
        print("-1\n")
    end
end