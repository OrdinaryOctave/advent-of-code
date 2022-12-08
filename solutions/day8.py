#input loaded and ready to go at 13:22:26

def checkVisible(row, column):
    if row == 0 or row == ROW_END_INDEX or column == 0 or column == COLUMN_END_INDEX:
        return True
    
    comparisonRow = row + 1
    while trees[comparisonRow][column]<trees[row][column]:
        if comparisonRow == ROW_END_INDEX:
            return True
        comparisonRow += 1
        
    comparisonRow = row - 1
    while trees[comparisonRow][column]<trees[row][column]:
        if comparisonRow == 0:
            return True
        comparisonRow -= 1
    
    comparisonColumn = column + 1
    while trees[row][comparisonColumn]<trees[row][column]:
        if comparisonColumn == COLUMN_END_INDEX:
            return True
        comparisonColumn += 1
    
    comparisonColumn = column - 1
    while trees[row][comparisonColumn]<trees[row][column]:
        if comparisonColumn == 0:
            return True
        comparisonColumn -= 1

    return False

def getViewingScore(row, column):
    if row == 0 or row == ROW_END_INDEX or column == 0 or column == COLUMN_END_INDEX:
        return 0
    directionScores = [1] * 4
    
    comparisonRow = row + 1
    while trees[comparisonRow][column]<trees[row][column]:
        if comparisonRow == ROW_END_INDEX:
            break
        directionScores[0] += 1
        comparisonRow += 1
    
    comparisonRow = row - 1
    while trees[comparisonRow][column]<trees[row][column]:
        if comparisonRow == 0:
            break
        directionScores[1] += 1
        comparisonRow -= 1
    
    comparisonColumn = column + 1
    while trees[row][comparisonColumn]<trees[row][column]:
        if comparisonColumn == COLUMN_END_INDEX:
            break
        directionScores[2] += 1
        comparisonColumn += 1
    
    comparisonColumn = column - 1
    while trees[row][comparisonColumn]<trees[row][column]:
        if comparisonColumn == 0:
            break
        directionScores[3] += 1
        comparisonColumn -= 1
    
    return directionScores[0] * directionScores[1] * directionScores[2] * directionScores[3]
    
    


with open('inputs/day8') as f:
    input = f.read()

rows = input.split('\n')
rows.pop(-1)
trees = [None] * len(rows)
for i in range(len(rows)):
    trees[i] = [*rows[i]]

ROW_END_INDEX = len(trees[1])-1
COLUMN_END_INDEX = len(trees)-1
visible = 0
maxViewingScore = 0

for row in range(len(trees)):
    for column in range(len(trees[row])):
        if checkVisible(row, column):
            visible += 1
        viewingScore = getViewingScore(row, column)
        if viewingScore > maxViewingScore:
            maxViewingScore = viewingScore

print(visible)
print(maxViewingScore)