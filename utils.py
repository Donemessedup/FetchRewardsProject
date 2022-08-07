
##############################################
# Programmer: Aaron Miller
# Fetch Rewards Project
# 8/6/22
# Description: This file houses the utility functions for finding the equisdistant points in a grid given the number of rows, columns, and the corner points
##############################################

# find's the lowest value for a corner's x or y value in a set of corner points
# @param corners: array of corner points
# @param position: determines if function delivers x or y lowest value
# @return returns lowest x or y value in corner points
def find_lowest(corners, position):
    lowest = corners[0][position]
    for corner in corners:
        if corner[position] < lowest:
            lowest = corner[position]
    return lowest

# determines where each corner point is located based off of corner values
# @param corners: array of corner points
# @return returns each corner's value
def determine_corners(corners):
    # find lowest x and y values
    lowest_x = find_lowest(corners, 0)
    lowest_y = find_lowest(corners, 1)
    
    for corner in corners:
        if corner[0] == lowest_x and corner[1] == lowest_y:
            bot_left = corner
        elif corner[0] == lowest_x and corner[1] != lowest_y:
            top_left = corner
        elif corner[0] != lowest_x and corner[1] == lowest_y:
            bot_right = corner
        else:
            top_right = corner
    return bot_left, bot_right, top_left, top_right

# Finds all points in grid based on number of rows and columns and the corner points.
# Points have same distance vertically and horizontally from next point.
# @param num_rows: number of rows in grid
# @param num_columns: number of columns in grid
# @param corners: array of corner points
# @return returns 2D list of points that reoresent the points in the grid
def find_image_points(num_rows, num_columns, corners):
    # determine which corner is which
    bot_left, bot_right, top_left, top_right = determine_corners(corners)
    # find overall distance between corner points
    width_diff = bot_right[0] - bot_left[0]
    height_diff = top_left[1] - bot_left[1]
    # find what distance should be between each point
    width_interval = width_diff / (num_columns - 1)
    height_interval = height_diff / (num_rows - 1)
    # create solution of points based on intervals found above
    solution = []
    for row in range(num_rows):
        solution_row = []
        for column in range(num_columns):
            x = round(top_left[0] + width_interval * column, 2)
            y = round(top_left[1] - height_interval * row, 2)
            point = [x, y]
            solution_row.append(point)
        solution.append(solution_row)
    return solution
            
                
            