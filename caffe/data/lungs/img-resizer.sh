#!/bin/bash

for filename in resizedData/*/*; do
	convert -resize 256x256\! $filename $filename
done
