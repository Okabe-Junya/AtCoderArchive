D, T, S = gets.split.map(&:to_i)
if D.to_f / S <= T
    puts 'Yes'
else
    puts 'No'
end