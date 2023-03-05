# papo-club/resources

This is a repository containing mapping and course setting resources for PAPO club members.
## Cosmetics
This folder contains cosmetic images for final map layout after course setting. This includes legends, logos, punch boxes and scale bars.

To use the cosmetics, just navigate to the image you want to download, and `Right click > Save image as...` Then inside Condes, go to `Objects > Graphics Objects > Graphics` and click on the map. Then select your downloaded .png file.

### Legends
The legends folder includes legends for all common symbol sets (*ISOM*, *ISSprOM* and *ISMTBOM*). They come in single or double column image forms, depending on what will fit the map layout better. The *ISSprOM* symbol set also includes a more compact legend containing just the essential symbols.

### Logos
The logos folder includes the PAPO logo, vith variations with and without the papo.org.nz URL. It also includes logos for series events in the `/series` subfolder such as the Summer Sprint series.

### Punch boxes
The punch-boxes folder includes Sport ident reserve boxes. These only needed to be added to the map layout at major events, if the event is a club event they are not necessary.

### Scale bars
The scale bars in the scale-bars folder should be imported based on the map scale, not the print scale. This means if you are printing a map at 1:10,000, but the map scale is 1:15,000, then use the scale bars in the 1:15,000 folder. (Basically, if you have a forest map, use 1:15,000, sprint use 1:4,000. **Do not resize the scale bars** as they have been exported at the correct image size for the corresponding map scale.

## Scripts
This folder contains scripts for help with mapping.

### Rotate_symbol
This script rotates all instances of a particular symbol in an `.xmap` file by a particular amount of degrees. Requires Python 3.6 or greater.

Usage: `python3 rotate_symbol.py <path/to/xmap/file.xmap>`

## Specifications
This folder contains the current IOF mapping specification documents.

## Symbol sets
This folder contains the current symbol sets that PAPO is using, in `.xmap` format. If you are creating a new map for PAPO, start your map by downloading the blank symbol set file that corresponds with your mapping specification.
