#!/bin/bash
source ../BaseStack/bin/setup_run.sh
PYTHONPATH=`pwd`/src:`pwd`/mcp:${PYTHONPATH}
export PYTHONPATH
source ccd/bin/activate
