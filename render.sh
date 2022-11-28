#!/bin/bash

for f in raw-configs/*/*.yaml ; do
  # name="$(basename -- $f)"
  cp $f manifests/"$(basename -- $f)"
done