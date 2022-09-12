N = gets.to_i
A = gets.split(' ').map(&:to_i)

hash = {}
flag = true
(0..N-1).each do |i|
    # p hash
    unless hash[A[i]].nil?
        puts('NO')
        flag = false
        break
    else
        hash[A[i]] = 1
    end
end

if flag
    puts('YES')
end
