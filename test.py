import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path

# Define paths and check for custom style
current_dir = Path.cwd()
parent_dir = current_dir.parent
style_path = os.path.join(parent_dir, 'publication.mplstyle')

if os.path.exists(style_path):
    plt.style.use(style_path)
else:
    print('No publication mplstyle found!')

# Define theme and utility functions
def theme_publication(ax=None, grid=True):
    """
    Apply a consistent theme to the plot.

    Parameters:
    - ax: The matplotlib Axes object to customize
    - grid: Boolean or string specifying grid type ('major', 'minor', or 'all')
    """
    if ax is None:
        ax = plt.gca()
    if grid:
        ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    ax.set_facecolor('white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_linewidth(0.5)
    ax.tick_params(direction='out', length=6, width=0.5)

def save_figure(output_path, size=(3, 3), dpi=300):
    """
    Save the current matplotlib figure to a file with a specified figure size.

    Parameters:
    - output_path: Path to save the figure
    - size: Predefined size ('small', 'medium', 'large', etc.) or 'custom'
    - width: Custom width (used if size is 'custom')
    - height: Custom height (used if size is 'custom')
    - dpi: Resolution of the saved figure
    - overwrite: Prevent overwriting existing files (default: True)
    """
    size_mapping = {
        'small': (2.5, 2.5),
        'medium': (5, 5),
        'large': (10, 10),
        'small_wide': (4, 2.5),
        'medium_wide': (8, 5),
        'large_wide': (16, 10),
        'small_long': (2.5, 4),
        'medium_long': (5, 8),
        'large_long': (10, 16),
        'super': (20, 20)
    }
    if size in size_mapping:
        width, height = size_mapping[size]

    plt.gcf().set_size_inches(width, height)
    plt.tight_layout()

    if not overwrite and os.path.exists(output_path):
        base, ext = os.path.splitext(output_path)
        i = 1
        while os.path.exists(f"{base}_{i}{ext}"):
            i += 1
        output_path = f"{base}_{i}{ext}"

    plt.savefig(output_path, dpi=dpi)
    plt.close()
    print(f"Figure saved to {output_path}")

# Example usage
if __name__ == "__main__":
    import pandas as pd
    import numpy as np

    # Example DataFrame
    np.random.seed(42)
    df = pd.DataFrame({
        'x': np.random.choice(['A', 'B', 'C'], size=100),
        'y': np.random.randn(100),
        'hue': np.random.choice(['Group1', 'Group2'], size=100)
    })

    # Create the plot
    sns.boxplot(data=df, x='x', y='y', hue='hue', palette='Set2')

    # Apply theme
    theme_publication()

    # Save the figure
    save_figure("example_plot.pdf", size='medium')
