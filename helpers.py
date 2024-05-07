# Averages Calculation and Display
def calculate_average(numerator, denominator):
    try:
        value = float(numerator) / float(denominator)
        return value
    except (ValueError, ZeroDivisionError):
        return None


def add_table(doc, column_titles, data_dict):
    """Helper function to add a table to the document. Row=1, cols=2"""
    table = doc.add_table(rows=1, cols=2)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = column_titles[0]
    hdr_cells[1].text = column_titles[1]
    for key, value in data_dict.items():
        row_cells = table.add_row().cells
        row_cells[0].text = key
        row_cells[1].text = str(value)
    return doc
