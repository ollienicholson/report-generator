# Averages Calculation and Display
def calculate_average(numerator, denominator):
    try:
        value = float(numerator) / float(denominator)
        return value
    except (ValueError, ZeroDivisionError):
        return None


def add_table(doc, column_titles=None, data_dict=None):
    """
    Helper function to add a table to the document. Row=1, cols=2.\n
    Function takes doc, column titles and a dict.\n
    Returns the doc object.
    """
    table = doc.add_table(rows=1 if column_titles else 0, cols=2)
    if column_titles:
        # table = doc.add_table(rows=1, cols=2)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = column_titles[0]
        hdr_cells[1].text = column_titles[1]

    for key, value in data_dict.items():
        row_cells = table.add_row().cells
        row_cells[0].text = key
        row_cells[1].text = str(value)
    return doc
