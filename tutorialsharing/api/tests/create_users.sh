#!/bin/bash
curl -H "Content-Type: application/json" -X POST -d '@user.json' http://localhost:4000/users
curl -H "Content-Type: application/json" -X POST -d '@user_2.json' http://localhost:4000/users
