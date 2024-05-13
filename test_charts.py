import matplotlib.pyplot as plt

# this works as of 08 May 2024
# testing


def player_stats_chart(df, filename='player_stats.png'):
    """
    Generates a bar chart for player stats and saves it as an image.
    """
    player_info = df.iloc[0]
    stats = ['Tries', 'Try Assists', 'Total Points', 'All Run Metres']
    values = [player_info[stat] for stat in stats]

    fig, ax = plt.subplots()
    ax.bar(stats, values, color='blue')
    ax.set_xlabel('Stats')
    ax.set_ylabel('Values')
    ax.set_title('Player Statistics')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to make room for rotated x-axis labels
    plt.savefig(filename)
    plt.close()
