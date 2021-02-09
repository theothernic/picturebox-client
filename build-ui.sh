#! /usr/bin/env bash
src_dir="./src/ui";
dest_dir="./ui";

if [ ! -d ${dest_dir} ]; then
  mkdir -p ${dest_dir};
fi


for file in "${src_dir}"/*.ui;
do
  src_filename=$(basename -- "${file}")
  dest_filename=$(basename "${file}" ".ui")
  /usr/bin/pyuic5 "${src_dir}/${src_filename}" -o "${dest_dir}/${dest_filename}.py"
done;