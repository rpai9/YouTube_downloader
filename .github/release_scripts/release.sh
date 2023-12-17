#!/bin/bash
local_file_path=$1
build_path=$2

# installing the pyinstaller
pip install pyinstaller

# Create a zip of package. (main-zip)
pyinstaller youtube_conv.py --onefile
zip -rm $local_file_path dist/ build/ youtube_converter.spec

# Create a directory called build
mkdir $build_path

# move the file created to the build directory
mv $local_file_path ./$build_path/$local_file_path
