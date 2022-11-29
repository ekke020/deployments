#!/bin/bash

for f in raw-configs/*/*.yaml ; do
  cp $f manifests/"$(basename -- $f)"
done