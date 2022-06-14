# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

n = int(input())
marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    scores = sum(scores)/3
    marks[name] = scores
    query_name = input()
    
    print('%.2f'%marks[query_name])
    
