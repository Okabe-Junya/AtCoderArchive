N = gets.to_i
W = gets.split(' ').map(&:to_i)
ans = []
(1..N-1).each do |i|
    prev = []
    post = []
    (0..N-1).each do |j|
        if j < i
            prev << W[j]
        else
            post << W[j]
        end
    end
    ans << (prev.sum - post.sum).abs
end
puts ans.min
