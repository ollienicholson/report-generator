# import requests


def create_match_tables(data, doc):
    for week_data in data['NRL']:
        for week, games in week_data.items():
            doc.add_heading(f"Week {week}", level=2)
            table = doc.add_table(rows=1, cols=6)
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Match Details'
            hdr_cells[1].text = 'Date'
            hdr_cells[2].text = 'Home Team'
            hdr_cells[3].text = 'Home Score'
            hdr_cells[4].text = 'Away Team'
            hdr_cells[5].text = 'Away Score'

            for game in games:
                row_cells = table.add_row().cells
                row_cells[0].text = game['Details']
                row_cells[1].text = game['Date']
                row_cells[2].text = game['Home']
                row_cells[3].text = game['Home_Score']
                row_cells[4].text = game['Away']
                row_cells[5].text = game['Away_Score']
