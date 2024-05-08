import unittest
import pandas as pd
import os
from PIL import Image

from test_charts import save_player_stats_chart

#  NOTE save_player_stats_chart passed at 11:20am Wed 8th May


class TestSavePlayerStatsChart(unittest.TestCase):
    def setUp(self):
        """Create a sample DataFrame."""
        self.data = {
            'Tries': [5],
            'Try Assists': [2],
            'Total Points': [15],
            'All Run Metres': [120]
        }
        self.df = pd.DataFrame(self.data)
        self.filename = 'test_player_stats.png'

    def tearDown(self):
        """Remove files created during the test."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_player_stats_chart(self):
        """Test if the chart is created and saved properly."""
        # Call the function to create and save the chart
        save_player_stats_chart(self.df, self.filename)

        # Check if the file was created
        self.assertTrue(os.path.exists(self.filename),
                        "The chart image file was not created.")

        # Check if the file is not empty
        with Image.open(self.filename) as img:
            self.assertGreater(img.size[0], 0, "The image width is zero.")
            self.assertGreater(img.size[1], 0, "The image height is zero.")


if __name__ == '__main__':
    unittest.main()
