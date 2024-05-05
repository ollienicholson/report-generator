import json
import warnings
from docx import Document
from docx.shared import Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import os

# Suppress specific deprecation warnings
warnings.filterwarnings('ignore', category=UserWarning,
                        message='.*style lookup by style_id is deprecated.*')


def create_word_document():
    # Create a new Document
    doc = Document()

    # Add a heading
    doc.add_heading('NRL Report', level=0)

    para = doc.add_paragraph()
    para.add_run('')

    # Add a centered image
    para_image = doc.add_paragraph()
    run_image = para_image.add_run()
    run_image.add_picture('nrl_image.jpg', width=Cm(12))
    para_image.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # Center-align the paragraph

    # add a page
    doc.add_page_break()

    doc.add_paragraph('The History of NRL')

    # add content to the second page
    history_text = (
        "The National Rugby League (NRL) is the top league of professional rugby league men's clubs in Australasia. "
        "Run by the Australian Rugby League Commission, the NRL's main competition is known as the Telstra Premiership "
        "due to sponsorship from Telstra Corporation and is contested by sixteen teams, fifteen of which are based in "
        "Australia with one based in New Zealand. NRL games are played throughout Australia and New Zealand from March "
        "to October. The season culminates in the premiership-deciding game, the NRL Grand Final, traditionally one of "
        "Australia's most popular sporting events and one of the largest attended club championship events in the world."
    )

    doc.add_paragraph(history_text, style='BodyText')

    # Align paragraph
    for paragraph in doc.paragraphs:
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

    # add a page
    doc.add_page_break()

    doc.add_paragraph('Here is some NRL data:')

    # Load JSON data
    with open('game_stats.json', 'r') as file:
        data = json.load(file)

    # Iterate over each item in the JSON data to create tables
    for year_data in data['NRL']:
        for year, matches in year_data.items():
            doc.add_heading(f'Year: {year}', level=2)
            for match_week, games in matches[0].items():
                doc.add_heading(f'Week {match_week}', level=3)
                for game in games:
                    table = doc.add_table(rows=1, cols=6)
                    hdr_cells = table.rows[0].cells
                    hdr_cells[0].text = 'Match Details'
                    hdr_cells[1].text = 'Date'
                    hdr_cells[2].text = 'Home Team'
                    hdr_cells[3].text = 'Home Score'
                    hdr_cells[4].text = 'Away Team'
                    hdr_cells[5].text = 'Away Score'

                    row_cells = table.add_row().cells
                    row_cells[0].text = game['Details']
                    row_cells[1].text = game['Date']
                    row_cells[2].text = game['Home']
                    row_cells[3].text = game['Home_Score']
                    row_cells[4].text = game['Away']
                    row_cells[5].text = game['Away_Score']

    filename = 'test.docx'

    # Save the document
    doc.save(filename)

    # Open the doc with the default application
    os.system(f"open '{filename}'")


# Run the function to create the document
create_word_document()


# Additional Features
# python-docx offers many features to enrich your Word documents:

# Adding more sections: You can add multiple paragraphs, headings, and even tables.
# Formatting text: Apply different styles, fonts, and colors.
# Inserting images: You can add images to the document.
# Creating tables: Add tables with multiple rows and columns.
# Here’s an example of adding a table:
