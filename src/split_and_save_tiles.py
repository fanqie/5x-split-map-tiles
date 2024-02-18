from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = None


def split_and_save_tiles(image_path, level, output_folder):
    # Open the image
    img = Image.open(f"{image_path}/{level}.tif")

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get image dimensions
    width, height = img.size

    # Calculate number of rows and columns for this level
    # rows = cols = (level - 1) ** 2
    rows = cols = 2 ** (level - 1)
    # print(level,cols)
    # return
    # Calculate tile size
    tile_width = width // cols
    tile_height = height // rows

    # Iterate through each column
    for c in range(cols):
        col_folder = os.path.join(output_folder, str(c))
        if not os.path.exists(col_folder):
            os.makedirs(col_folder)
        # Iterate through each row
        for r in range(rows):
            # Define bounding box for each tile
            left = c * tile_width
            upper = r * tile_height
            right = (c + 1) * tile_width
            lower = (r + 1) * tile_height

            # Crop the tile
            tile = img.crop((left, upper, right, lower))

            # Save the tile
            tile_name = f"{r}.jpg"  # You can adjust the filename format as needed
            tile_path = os.path.join(col_folder, tile_name)
            tile.save(tile_path)

            print(f"Saved {tile_name} in level {level}, row {r}, column {c}")
