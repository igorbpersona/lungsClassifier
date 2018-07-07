#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/lungs
DATA=data/lungs
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/lungs_train_lmdb \
  $DATA/lungs_mean.binaryproto

echo "Done."
