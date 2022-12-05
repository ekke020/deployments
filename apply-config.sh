#!/bin/bash
curl -v \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $TEST" \
  https://api.github.com/repos/ekk020/Kuber/actions/runs/3593891925/pending_deployments \
  -d '{"environment_ids":[743920904],"state":"approved","comment":"Ship it!"}'