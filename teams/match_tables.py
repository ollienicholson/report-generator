

def create_match_tables(data: dict, doc):
    '''
    will need to pass the rounds into this report\
        '''
    print('running create_match_tables...\n\n')
    round_1 = data['NRL'][0]  # this works if you only want round 1

    try:
        # for rounds in data['NRL']: # this works for all rounds
        for week, games in round_1.items():
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

    except Exception as e:
        print(f"could not create match tables: {e}")
