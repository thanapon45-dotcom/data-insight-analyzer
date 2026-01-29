def sales_trend(sales):
    if sales[-1] > sales[0]:
        return "upward"
    elif sales[-1] < sales[0]:
        return "downward"
    else:
        return "stable"
