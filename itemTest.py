from item import Items
from datetime import date

items = Items()
items.addItem(1, date(2014, 2, 15))
items.addItem(1, date(2014, 2, 17))
items.addItem(2, date(2014, 2, 15))


print("Count of items: " + str(items.getCountOfItems()))
print("Position of item 1: " + str(items.getPositionOfItem(1)))
print("Number of counts of item 1 with 7 days of 2014-02-23: " + str(items.getCountOfViewsForItemWithin7Days(1, date(2014, 2, 23))))