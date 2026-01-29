def sales_summary(sales):
    return {
        "total": sum(sales),
        "average": sum(sales) / len(sales),
        "max": max(sales),
        "min": min(sales)
    }
