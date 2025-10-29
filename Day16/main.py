# from turtle import Screen, Turtle, done
# jimmy = Turtle()
# myScreen = Screen()
# jimmy.shape("turtle")
# jimmy.color("white")
# jimmy.fillcolor("blue")
# jimmy.forward(100)
# jimmy.right(90)
# jimmy.forward(100)
# jimmy.right(90)
# print(myScreen.canvheight)
# myScreen.exitonclick()
# # This code creates a turtle graphics window and draws a blue square.

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["City Name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide",1295, 1158259, 600.5])
table.add_row(["Brisbane",5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])
table.align="l"

print(table)
# This code creates and displays a table of Australian cities with their area, population, and annual