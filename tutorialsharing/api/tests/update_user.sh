#!/bin/bash
curl -H "Content-Type: application/json" -X POST -d '@update_user.json' http://localhost:4000/users
