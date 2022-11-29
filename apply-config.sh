#!/bin/bash

gcloud beta container fleet config-management apply \
    --membership=kuar-cluster \
    --config=config-management-spec.yaml \
    --project=endless-upgrade-368914