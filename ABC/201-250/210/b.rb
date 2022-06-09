N = gets.to_i
S = gets.split('')
i = 0
while S[i] != '1'
    i += 1
end
if i % 2 == 0
    puts 'Takahashi'
else
    puts 'Aoki'
end