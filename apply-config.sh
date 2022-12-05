#!/bin/bash

curl -X POST -H Authorization: Bearer $API_TOKEN -H Content-Type: application/json \
    https://api.github.com/repos/PricerAB/{repo}/actions/runs/{run_id}/pending_deployments \
    -d \ 
    {"environment_ids":['12313'],"state":"approved","comment":"Ship it!"}