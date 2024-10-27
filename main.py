import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
import seaborn as sns
import ssl

def load_tic_tac_toe_data(n_rows=100):
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data"
    context = ssl._create_unverified_context()
    column_names = ['top-left', 'top-middle', 'top-right', 'middle-left', 'middle-middle', 'middle-right', 'bottom-left', 'bottom-middle', 'bottom-right', 'result']
    df = pd.read_csv(urlopen(url, context=context), header=None, names=column_names)
    df = df.head(n_rows)

    return df

def check_win(board, player):
    """Check if the player ('x' or 'o') has a winning combination in the board."""
    win_conditions = [
        [board['top-left'], board['top-middle'], board['top-right']],  # Top row
        [board['middle-left'], board['middle-middle'], board['middle-right']],  # Middle row
        [board['bottom-left'], board['bottom-middle'], board['bottom-right']],  # Bottom row
        [board['top-left'], board['middle-left'], board['bottom-left']],  # Left column
        [board['top-middle'], board['middle-middle'], board['bottom-middle']],  # Middle column
        [board['top-right'], board['middle-right'], board['bottom-right']],  # Right column
        [board['top-left'], board['middle-middle'], board['bottom-right']],  # Diagonal 1
        [board['top-right'], board['middle-middle'], board['bottom-left']]  # Diagonal 2
    ]

    return any(
        [line == [player, player, 'b'] or line == ['b', player, player] or line == [player, 'b', player] for line in
         win_conditions])


def replace_b_values(df):
    """Replace 'b' (blank) with the appropriate value ('x' or 'o') ensuring X's win for positive results."""
    board_columns = ['top-left', 'top-middle', 'top-right',
                     'middle-left', 'middle-middle', 'middle-right',
                     'bottom-left', 'bottom-middle', 'bottom-right']

    def fill_row(row):
        # Check for X and O count
        x_count = (row[board_columns] == 'x').sum()
        o_count = (row[board_columns] == 'o').sum()
        blanks = [col for col in board_columns if row[col] == 'b']

        # If result is positive, X must win
        if row['result'] == 'positive':
            for col in blanks:
                # First priority: Can X win in this move?
                row[col] = 'x'
                if check_win(row, 'x'):
                    return row

                # Otherwise, try blocking O if O can win in the next move
                row[col] = 'o'
                if check_win(row, 'o'):
                    row[col] = 'o'  # Block O
                else:
                    row[col] = 'b'  # Reset blank if no win

            # After trying to block O and looking for X's win, fill remaining blanks with X
            for col in blanks:
                if row[col] == 'b':
                    row[col] = 'x'
        else:
            # If the result is negative, prioritize O's win or blocking X
            for col in blanks:
                row[col] = 'o' if x_count > o_count else 'x'
                x_count += 1 if row[col] == 'x' else 0
                o_count += 1 if row[col] == 'o' else 0

        return row

    df = df.apply(fill_row, axis=1)

    return df


def print_dataset_info(df, stage="Initial", n_rows = 100):
    """Print dataset info and show occurrences of 'b' (blank) cells."""
    print(f"\n--- {stage} Dataset Info ---")

    print(df[['top-left', 'top-middle', 'top-right', 'middle-left', 'middle-middle', 'middle-right', 'bottom-left', 'bottom-middle', 'bottom-right', 'result']].head(n_rows))

    print(f"\nDataset Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("\n'b' (blank) values per column:")

    # Count the number of 'b' values in each column
    b_counts = (df == 'b').sum()
    print(b_counts)

    print("\n--- End of Info ---")


def plot_tic_tac_toe_analysis(df):
    """Display multiple plots for Tic-Tac-Toe game data in the same window."""

    # Create a grid of subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))

    # 1. Game Result Distribution
    result_counts = df['result'].value_counts()
    axs[0, 0].bar(result_counts.index, result_counts.values)
    axs[0, 0].set_title('Distribution of Game Results')
    axs[0, 0].set_xlabel('Game Result')
    axs[0, 0].set_ylabel('Frequency')

    # 2. Frequency of X and O Placements
    board_columns = ['top-left', 'top-middle', 'top-right',
                     'middle-left', 'middle-middle', 'middle-right',
                     'bottom-left', 'bottom-middle', 'bottom-right']

    x_frequencies = (df[board_columns] == 'x').sum()
    o_frequencies = (df[board_columns] == 'o').sum()

    frequency_df = pd.DataFrame({'X': x_frequencies, 'O': o_frequencies})
    frequency_df.plot(kind='bar', ax=axs[0, 1], title='Frequency of X and O Placements')
    axs[0, 1].set_ylabel('Count')
    axs[0, 1].set_xlabel('Position')

    # 3. Heatmap of X Placements
    x_heatmap_data = (df[board_columns] == 'x').sum().values.reshape(3, 3)
    sns.heatmap(x_heatmap_data, annot=True, fmt='d', cmap='Blues', ax=axs[1, 0])
    axs[1, 0].set_title('Heatmap of X Placements')
    axs[1, 0].set_xticklabels(['Left', 'Middle', 'Right'])
    axs[1, 0].set_yticklabels(['Top', 'Middle', 'Bottom'])

    # 4. Heatmap of O Placements
    o_heatmap_data = (df[board_columns] == 'o').sum().values.reshape(3, 3)
    sns.heatmap(o_heatmap_data, annot=True, fmt='d', cmap='Reds', ax=axs[1, 1])
    axs[1, 1].set_title('Heatmap of O Placements')
    axs[1, 1].set_xticklabels(['Left', 'Middle', 'Right'])
    axs[1, 1].set_yticklabels(['Top', 'Middle', 'Bottom'])

    # Adjust layout
    plt.tight_layout()
    plt.show()

def main(n_rows=100):
    """Main function to load, process, and visualize the Tic-Tac-Toe dataset."""
    df = load_tic_tac_toe_data(n_rows)

    print_dataset_info(df, "Initial", n_rows)

    df = replace_b_values(df)

    print_dataset_info(df, "After Replacing 'b' Values", n_rows)

    plot_tic_tac_toe_analysis(df)

if __name__ == "__main__":
    main(n_rows=1000)
