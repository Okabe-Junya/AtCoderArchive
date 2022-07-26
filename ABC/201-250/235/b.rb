N = gets.to_i
H = gets.split(' ').map(&:to_i)

ans = H[0]

idx = 0
while idx < N - 1
    if H[idx + 1] > H[idx] 
        idx += 1
    else
        break
    end
end
puts H[idx]