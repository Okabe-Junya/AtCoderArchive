A, B = gets.split.map(&:to_i)
if B - A + 1 >= 0
    puts B - A + 1
else
    puts 0
end