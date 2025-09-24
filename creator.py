import os
import shutil
import sys
from PIL import Image

def create_vmat_content(map_name, index):
    """
    Generates the content for a .vmat file.
    """
    content = f'''// THIS FILE IS AUTO-GENERATED

Layer0
{{
    shader "csgo_composite_generic.vfx"

    g_flAlphaBlend "0.000"

    //---- Options ----
    TextureA "panorama/images/map_icons/screenshots/1080p/{map_name}_{index}_png.png"
    TextureB ""


    VariableState
    {{
        "Options"
        {{
        }}
    }}
}}
'''
    return content

def create_map_files():
    """
    Automates the process of organizing map-related files for a Source 2 map,
    including image conversion and resizing.
    """
    # Always prompt the user for the map name
    map_name = input("Please enter the map name (e.g., kz_jakke): ")
    if not map_name:
        print("Map name cannot be empty. Exiting.")
        return

    source_dir = os.getcwd()
    
    # Define destination folder paths relative to the current working directory
    loading_screen_dir = os.path.join(source_dir, 'panorama', 'images', 'map_icons', 'screenshots', '1080p')
    map_icon_dir = os.path.join(source_dir, 'panorama', 'images', 'map_icons')
    maps_dir = os.path.join(source_dir, 'maps')

    # Create destination directories if they don't exist
    for directory in [loading_screen_dir, map_icon_dir, maps_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
    
    files_to_process = os.listdir(source_dir)
    
    # Process loading screen images
    image_extensions = ('.jpg', '.jpeg', '.png', '.tga', '.bmp')
    image_files = sorted([f for f in files_to_process if f.lower().endswith(image_extensions)])
    
    for i, source_image_name in enumerate(image_files, 1):
        dest_image_name = f"{map_name}_{i}_png.png"
        dest_image_path = os.path.join(loading_screen_dir, dest_image_name)

        try:
            with Image.open(os.path.join(source_dir, source_image_name)) as img:
                img = img.resize((1920, 1080), Image.LANCZOS)
                img.save(dest_image_path, "PNG")
            print(f"Converted and saved {source_image_name} to {dest_image_path} (1920x1080 PNG)")
        except Exception as e:
            print(f"Error processing {source_image_name}: {e}")

        # Generate the corresponding vmat file
        dest_vmat_name = f"{map_name}_{i}_png.vmat"
        dest_vmat_path = os.path.join(loading_screen_dir, dest_vmat_name)
        vmat_content = create_vmat_content(map_name, i)
        
        with open(dest_vmat_path, 'w') as f:
            f.write(vmat_content)
        print(f"Generated and saved {dest_vmat_name} to {dest_vmat_path}")
            
    # Process map icon file
    found_icon = False
    for f in files_to_process:
        if f.endswith('.svg'):
            icon_source_name = f
            found_icon = True
            break
            
    if found_icon:
        dest_icon_name = f"map_icon_{map_name}.svg"
        dest_icon_path = os.path.join(map_icon_dir, dest_icon_name)
        shutil.copy(os.path.join(source_dir, icon_source_name), dest_icon_path)
        print(f"Copied {icon_source_name} to {dest_icon_path} and renamed to {dest_icon_name}")

    # Process map description file
    description_file_name = f"{map_name}.txt"
    description_file_path = os.path.join(maps_dir, description_file_name)
    
    # Find and move an existing .txt file, or create a new empty one
    txt_files = [f for f in files_to_process if f.lower().endswith('.txt') and f.lower() != 'readme.txt' and f != os.path.basename(sys.argv[0])]
    
    if txt_files:
        source_txt_path = os.path.join(source_dir, txt_files[0])
        shutil.move(source_txt_path, description_file_path)
        print(f"Moved and renamed {txt_files[0]} to {description_file_path}")
    else:
        with open(description_file_path, 'w') as f:
            f.write('') # Create an empty file
        print(f"No existing .txt file found. Created new empty file: {description_file_path}")

    print("\nProcess completed.")

if __name__ == "__main__":
    create_map_files()