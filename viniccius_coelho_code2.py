# Viniccius Lucca Florindo Coelho
# CS 1410
# 09/29/2023

'''
This is code 2. It is design to take 2 data sets with specific
values and create a line chart. It labels each data set names,
each point value, min and max of the 2 lines, and years for each 
value (starting in 1978 and increasing 10 years per value).
'''

# Importing Module turtle.
import turtle

# The data sets for each line.
WELL_OF = [59, 74, 73, 77]
MEANING = [60, 43, 44, 51]

# Each data set title.
GOALS = ['Well Off Financially', 'Meaningful Philosophy of Life']

# X and Y axis titles.
TITLE = ['Freshmen Life Goals', '% of Students Commited to Goal']

# color of each data set.
COLOR = ['hotpink', 'cyan']

# Starting year and increment.
YEAR = (1978, 10)

# Variables that will be used on functions.
WO_LEN = len(WELL_OF)
MEAN_LEN = len(MEANING)
COMBINED = WELL_OF + MEANING


def reset_turtle(faith, colorp='red'):
    """
    It will reset the specific turtle to be ready to use in function

    Args:
        faith: faith will be our main turtle. It will be sub by turtle name.
        colorp: Set the default color for the turtle. Defaults to 'red'.

    Returns:
        Faith: Turtle with all specifications 
    """
    # The basic Turtle will be set for this standards
    # speed 0 to be fast.
    faith.speed(0)

    # Will not show the turtle.
    faith.hideturtle()

    # Set the standard color.
    faith.color(colorp)

    # pen up to be ready to go to its specific position.
    faith.up()

    # return the Turtle ready.
    return faith


def draw_line(line, x_value1, y_value1, x_value2, y_value2):
    """
    Basic funtion to create a straight line

    Args:
        line: Call Turtle
        x_value1: first x position the turtle will go to
        y_value1: first y position the turtle will go to
        x_value2: second x position the turtle will go to
        y_value2: second y position the turtle will go to
    """

    # Make Turtle with standard values.
    reset_turtle(line)

    # will go to specific position and draw a line
    # to a second specific position.
    line.goto(x_value1, y_value1)
    line.down()
    line.goto(x_value2, y_value2)


def draw_graph_line(line, x_value1, y_value1, x_value2, y_value2):
    """
    Basic function to create a line with dots on the beginning (x1,y1)
    and at the end (x2,y2)

    Args:
        line: Call Turtle
        x_value1: first x position the turtle will go to
        y_value1: first y position the turtle will go to
        x_value2: second x position the turtle will go to
        y_value2: second y position the turtle will go to
    """
    # Pen up to get ready to go to a position.
    line.up()

    # Send turtle to a position and leave a dot.
    line.goto(x_value1, y_value1)
    line.dot(5)

    # Start the line and go to a second position, leaving a dot there.
    line.down()
    line.goto(x_value2, y_value2)
    line.dot(5)


def draw_axis(char):
    """
    Function will draw the x-axis and y-axis of the chart.
    x-axis will be based on whichever data set has more values.
    y-axis will be default 200.

    Args:
        char: Call Turtle
    """

    # reset turtle to standard.
    reset_turtle(char)

    # go to our graph (0,0).
    char.goto(-200, 0)
    char.down()

    # check whhich data set is longer and set x-axis to fit that data set.
    if WO_LEN > MEAN_LEN:
        char.forward(WO_LEN*100)
        char.backward(WO_LEN*100)
    else:
        char.forward(MEAN_LEN*100)
        char.backward(MEAN_LEN*100)

    # turtle will turn 90° and draw y-axis.
    char.left(90)
    char.forward(200)


def draw_x(line):
    """
    Function will draw X-axis tick marks according to whichever data set
    has more values.

    Args:
        line: Call Turtle
    """

    # set turtle to standard.
    reset_turtle(line)

    # check which data set is longer and will draw x-axis tick marks
    # with the specific amount of values the longer data set contains.
    if WO_LEN > MEAN_LEN:
        for i in range(WO_LEN):

            # call function to draw a line (turtle, x1,y1,x2,y2)
            draw_line(line, -150 + (100*i), -10, -150 + (100*i), 10)
    else:
        for i in range(MEAN_LEN):

            # call function to draw a line (turtle, x1,y1,x2,y2)
            draw_line(line, -150 + (100*i), -10, -150 + (100*i), 10)


def draw_y(line):
    """
    Function will draw y-axis tick marks according to the maximum and
    minimum values of both data set combined.

    Args:
        line: Call Turtle
    """

    # set turtle to standard.
    reset_turtle(line)

    # call function that draws a line. draw y-axis tick marks on the
    # minimum and maximun level of the data sets combined.
    draw_line(line, -210, min(COMBINED)*2, -190, min(COMBINED)*2)
    draw_line(line, -210, max(COMBINED)*2, -190, max(COMBINED)*2)


def x_tick_values(x_turtle):
    """
    Function will write the specific years for each x-axis
    tick marks. By default is starting in 1978 and increasing
    10 years per tick mark.

    Args:
        x_turtle: Call Turtle
    """

    # set turtle to standard.
    reset_turtle(x_turtle)

    # put turtle in the first x-axis tick mark position
    # and write the first year value.
    x_turtle.goto(-160, -30)
    x_turtle.down()
    x_turtle.write(int(YEAR[0]))
    x_turtle.up()

    # check which data set is longer and will write each year
    # in the specific x-axis tick mark spot.
    if WO_LEN > MEAN_LEN:
        for i in range(WO_LEN):
            x_turtle.goto(-160+(100*i), -30)
            x_turtle.write(int(YEAR[0] + (YEAR[1] * i)))
    else:
        for i in range(MEAN_LEN):
            x_turtle.goto(-160+(100*i), -30)
            x_turtle.write(int(YEAR[0] + (YEAR[1] * i)))


def y_tick_values(y_turtle):
    """
    Function will write the minimum and maximum values of both
    data set combined onto its respectives tick marks.

    Args:
        y_turtle: Call Turtle
    """

    # set turtle to standard.
    reset_turtle(y_turtle)

    # Turtle will go to y-axis minimum and maximum tick marks
    # and write its specific values. First minimum then maximum.
    y_turtle.goto(-220, (min(COMBINED)*2)+5)
    y_turtle.write(min(COMBINED))
    y_turtle.goto(-220, (max(COMBINED)*2)+5)
    y_turtle.write(max(COMBINED))


def graph_well(graph_value):
    """
    Function will draw the line char for our first data set.
    Each point will follow each data set value and x-axis 
    tick mark position.

    Args:
        graph_value: Call Turtle
    """

    # set turtle to standard.
    reset_turtle(graph_value, f'{COLOR[0]}')

    # Will check the length of our first data set and subtract 1 so
    # for loop fit the whole list length.
    for i in range(WO_LEN-1):
        # Call function that draw graph lines with dots (turtle, x1,y1,x2,y2).
        draw_graph_line(graph_value, -150+(100*i),
                        WELL_OF[i]*2, -150+(100*i)+100, WELL_OF[i+1]*2)


def graph_mean(graph_value):
    """
    Function will draw the line for our second data set.
    Each point will follow each data set value and x-axis 
    tick mark position.

    Args:
        graph_value: Call Turtle
    """
    # set turtle to standard.
    reset_turtle(graph_value, f'{COLOR[1]}')

    # Will check the length of our second data and subtract 1 so
    # for loop fit the whole list length.
    for i in range(MEAN_LEN-1):

        # Call function that draw graph lines with dots (turtle, x1,y1,x2,y2).
        draw_graph_line(graph_value, -150+(100*i),
                        MEANING[i]*2, -150+(100*i)+100, MEANING[i+1]*2)


def graph_well_numbers(graph_value):
    """
    Function will write the values of our first data set on top
    of each point and on the respective point.

    Args:
        graph_value: Call Turtle
    """

    # set turtle to standard.
    reset_turtle(graph_value, f'{COLOR[0]}')

    # send turtle to first value's point and write specific value.
    graph_value.goto(-160, (WELL_OF[0]*2)+10)
    graph_value.write(f'{WELL_OF[0]}')

    # Will check the length of our first data and subtract 1 so
    # for loop fit the whole list length.
    for i in range(WO_LEN-1):

        # send turtle to other points and write their values according to
        # our data set index numbers and values that it represents.
        graph_value.goto(-160+(100*(i+1)), (WELL_OF[i+1]*2)+10)
        graph_value.write(f'{WELL_OF[i+1]}')


def graph_mean_numbers(graph_value):
    """
    Function will write the values of our second data set under
    each point and on the respective point.

    Args:
        graph_value: Call Turtle
    """
    # set turtle to standard.
    reset_turtle(graph_value, f'{COLOR[1]}')

    # send turtle to first value's point and write specific value.
    graph_value.goto(-160, (MEANING[0]*2)-15)
    graph_value.write(f'{MEANING[0]}')

    # Will check the length of our first data and subtract 1 so
    # for loop fit the whole list length.
    for i in range(MEAN_LEN-1):

        # send turtle to other points and write their values according to
        # our data set index numbers and values that it represents.
        graph_value.goto(-160+(100*(i+1)), (MEANING[i+1]*2)-15)
        graph_value.write(f'{MEANING[i+1]}')


def legend(leg_pen):
    """
    Function will write the chart legend under the chart. it will
    get the data set's names from a list, and set the color from
    another list.

    Args:
        leg_pen: Call Turtle
    """
    # set turtle to standard
    reset_turtle(leg_pen)

    # send turtle to where I want the legend to be based on graph (0,0)
    # which is (-200, 0) in turtle screen.
    leg_pen.goto(-200, -70)
    leg_pen.down()

    # set color and start to fill the polynomial. Color is according to a list.
    leg_pen.color(f'{COLOR[0]}')
    leg_pen.begin_fill()

    # for loop to create a little 4 sides polynomial. This example, a square.
    for _ in range(4):
        leg_pen.forward(10)
        leg_pen.left(90)

    # end fill to stop filling everything
    leg_pen.end_fill()

    # up and go to where I want the title to be based on the square position
    leg_pen.up()
    leg_pen.goto(-185, -73)

    # write title for first data set according to a list
    leg_pen.write(f'{GOALS[0]}')

    # Up we go to the next data set legend
    leg_pen.goto(-200, -80)
    leg_pen.down()

    # set color and start filling a polynomial. Color is according to a list.
    leg_pen.color(f'{COLOR[1]}')
    leg_pen.begin_fill()

    # for loop to create a little 4 sides polynomial. This example, a square.
    for _ in range(4):
        leg_pen.forward(10)
        leg_pen.right(90)

    # end fill to stop filling everything
    leg_pen.end_fill()

    # up and go to where I want the title to be based on the square position
    leg_pen.up()
    leg_pen.goto(-185, -93)

    # write title for first data set according to a list
    leg_pen.write(f'{GOALS[1]}')


def title_name(leg_pen):
    """
    Funciton will write the title of the graph. The position of
    the title will be according to how long the x-axis is.

    Args:
        leg_pen: Call Turtle
    """
    # set turtle to standard
    reset_turtle(leg_pen)

    # will check what data set is longer to determine the length of x-axis.
    if WO_LEN > MEAN_LEN:

        # Pen will go to /2 of the x-axis - 100 and 30 characters over our y-axis limit.
        # It will write the title based on a list.
        leg_pen.goto((WO_LEN*100/2)-100, 230)
        leg_pen.write(f'{TITLE[0]}\n ({TITLE[1]})', align='right')

    else:

        # Pen will go to /2 of the x-axis - 100 and 30 characters over our y-axis limit.
        # it will write the title based on a list.
        leg_pen.goto((MEAN_LEN*100/2)-100, 230)
        leg_pen.write(f'{TITLE[0]}\n ({TITLE[1]})', align='right')


def screen_size(screen_turtle):
    '''Set screen size according to the legth
    of data provided and corrects screen to fit
    graoh perfectly.

    Args:
        screen_turtle: Call Turtle
    '''
    # check which data set is longer
    if WO_LEN > MEAN_LEN:
        # will set screen X value to perfect fit the graph, no matter how long your data set is.
        size = (len(WELL_OF)*150)+100

    else:

        # will set screen X value to perfect fit the graph, no matter how long your data set is.
        size = (len(MEANING)*150)+100

    # will get our created X value and add a standard 800 for Y value.
    # That's how long our screen will be. Set screen to be black.
    screen_turtle.setup(width=size, height=800)
    screen_turtle.bgcolor('black')

    # This will make sure our screen is always at -300 on the left, and follow the X value size
    # on the right, with some adjustments. To better fit the chart no matter how long the data
    # set will be. Will also set the bottom y value to -150 and top y value to 300.
    screen_turtle.setworldcoordinates(-300, -150, size-250, 300)


def main():
    """
    Main function that will set every turtle that are being used, call and organize every
    function to create the line chart. 

    """
    # Call all the turtle used to create the chart
    screen_turtle = turtle.Screen()
    line = turtle.Turtle()
    x_turtle = turtle.Turtle()
    y_turtle = turtle.Turtle()
    char = turtle.Turtle()
    graph_value = turtle.Turtle()
    leg_pen = turtle.Turtle()

    # Call screen Function
    screen_size(screen_turtle)

    # call function to draw x-axis
    draw_axis(char)

    # function to write chart title. Called now for style purposes.
    title_name(leg_pen)

    # functions to draw x-tick marks and y-tick marks
    draw_x(line)
    draw_y(line)

    # function to write tick marks year value.
    x_tick_values(x_turtle)

    # functions to draw the lines of each data set
    graph_well(graph_value)
    graph_mean(graph_value)

    # functions to write the values on each point of data sets
    graph_well_numbers(graph_value)
    graph_mean_numbers(graph_value)

    # function to write min and max values. Called later for style purposes.
    y_tick_values(y_turtle)

    # function to write leegend
    legend(leg_pen)

    # make sure turtle window doesn't close when turtles are done.
    turtle.done()


if __name__ == '__main__':
    main()

# Thoughts

# this is a giant code that I'm sure I did more than I should've. I took too long
# because was trying to prove myself that I can do something enjoyable and the way
# I thought was the best. This code can be changed by many ways, the data set could
# increase or decrease values, the data set color could change, etc. You could change
# all that by simply changing a list, and that's what I liked about this. It was extremely
# challanging and stressful, but I got to what I think is acceptable (not that I'm trying
# to be harsh on myself). My creative element is that no matter how long your data sets are,
# the screen will be always centering the graph and not having any values unseen.
