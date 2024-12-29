import matplotlib.pyplot as plt
from pathlib import Path



def theme_publication(style, grid=False):
    """
    Apply a custom matplotlib style for publication-quality plots.
    """
    # Determine the directory paths
    current_dir = Path.cwd()
    parent_dir = current_dir.parent
    # print(f"Parent Directory: {parent_dir}")

    # Check if a custom style file exists and apply it
    mplstyles = list(parent_dir.glob('styles/*.mplstyle'))
    if mplstyles:
        for style in mplstyles:
            print(f"Applying style: {style}")
            plt.style.use(str(style))
    else:
        print('No .mplstyle files were found!')

    # Get a list of colors from the style's color cycle
    try:
        colors = plt.rcParams['axes.prop_cycle'].by_key().get('color', [])
        print('Available Colors:')
        print('\n'.join(color for color in colors))
    except KeyError:
        print('No color cycle found in the current style.')

    try:
        plt.style.use([style])
    except OSError as e:
        print(f"Error: Could not apply style '{style}'. {e}")
    if grid:
        plt.gca().grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

        