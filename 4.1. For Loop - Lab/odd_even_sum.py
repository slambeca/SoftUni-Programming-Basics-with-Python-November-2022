number = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, number + 1):
    current_number = int(input())
    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

diff = abs(even_sum - odd_sum)

if odd_sum == even_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    print(f"No\nDiff = {diff}")