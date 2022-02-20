#!/bin/bash
while [ -n "$1" ]
do
  case "$1" in
    "--input_folder") input_folder=$2
    ;;
    "--extension") extension=$2
    ;;
    "--backup_folder") backup_folder=$2
    ;;
    "--backup_archive_name") backup_archive_name=$2
    ;;
  esac
  shift 2
done
search=`find $input_folder -type f -name "*.$extension"`
result=$search
mkdir $backup_folder
cp --parent $result $backup_folder/
tar -czf $backup_archive_name $backup_folder
echo "done"
