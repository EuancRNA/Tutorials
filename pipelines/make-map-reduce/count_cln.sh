#!/bin/bash
INFILE=$1
OUTFILE=$2

sort "${INFILE}" | uniq -c | sort -rn > "${OUTFILE}"
