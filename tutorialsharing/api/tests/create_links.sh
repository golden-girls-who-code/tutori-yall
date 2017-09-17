#!/bin/bash
curl -H "Content-Type: application/json" -X POST -d '@link.json' http://localhost:4000/links/8423
curl -H "Content-Type: application/json" -X POST -d '@link_2.json' http://localhost:4000/links/0
