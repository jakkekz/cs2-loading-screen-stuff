# cs2-loading-screen-stuff
Semi automate the making of loading screen images, map icon and description. 

0. create a folder (for example on your desktop), place `creator.exe` inside it. This is your "main" folder.

1. convert your image into a `svg file` !!! NOT all svg files are created equal and i recommend this one https://www.pngtosvg.com/ !!!

2. place the `svg` and `image files` in the main folder (it will automatically convert other image formats to png 1080p)

3. create a `.txt` file with any name (not README.txt) and write your description in there. ("Loading..." cant be removed i think)

4. run `creator.exe`

5. it will create all the necessary files in the correct place.

6. place the `panorama` folder directly into `content/csgo_addons/YOURADDON/`
7. place the `maps` folder directly into `game/csgo_addons/YOURADDON/`

8. open the "loading screen material" that was just made inside hammer for it to compile them to `.vtex_c` format. Theyll be named like `yourmapname_x_png.vmat`

9. go to: `GAME/csgo_addons/YOURADDON/panorama/images/map_icons/screenshots/1080p` and remove the extra `_png` and `mumbo jumbo` before `.vtex_c`

   for example: `kz_tikkaat_1_png_png_de8eb162.vtex_c` would be `kz_tikkaat_1_png.vtex_c`

10. Ready! load the map (no recompile needed)


[#WAD](https://steamcommunity.com/groups/ckzwad)

<img width="112" height="112" alt="Image" src="https://github.com/user-attachments/assets/6bc1c38d-9330-41fe-9f0f-b7d25b59aabf" />
