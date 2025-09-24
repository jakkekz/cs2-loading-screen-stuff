0. convert your image into a svg. !!! NOT all svg files are created equal and i recommend this one https://www.pngtosvg.com/ !!!

1. place the svg and image files here in the main folder (it will automatically convert other image formats to png 1080p)

2. write whatever you want as the loading screen description inside the "description.txt" file.

3. it will create all the necessary files in the correct place.

4. place the /panorama folder into content/csgo_addons/YOURADDON/
5. place the /maps folder into game/csgo_addons/YOURADDON/

6. open the "loading screen material" inside hammer for it to compile them to .vtex_c format. Theyll be named like "yourmapname_x_png.vmat"

7. go to: GAME/csgo_addons/YOURADDON/panorama/images/map_icons/screenshots/1080p and remove the extra _png and mumbo jumbo before .vtex_c

for example: "kz_tikkaat_1_png_png_de8eb162.vtex_c" should be "kz_tikkaat_1_png.vtex_c"

8. Ready! load the map (no recompile needed)

#WAD