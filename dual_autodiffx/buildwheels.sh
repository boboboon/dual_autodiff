#!/bin/bash

BUILD_TARGETS="cp310-manylinux_x86_64 cp311-manylinux_x86_64"
OUTPUT_DIR="dist"

if ! docker info > /dev/null 2>&1; then
  echo "Error: Docker is not running. Please start Docker Desktop and try again."
  exit 1
fi

echo "Starting build process with cibuildwheel..."

CIBW_BUILD="$BUILD_TARGETS" CIBW_SKIP="cp39*" cibuildwheel --platform linux --output-dir $OUTPUT_DIR

if [ $? -eq 0 ]; then
  echo "Build completed successfully. Wheels are located in the $OUTPUT_DIR directory."
else
  echo "Error: Build failed. Please check the output above for more details."
  exit 1
fi

# You can then run it with: docker run a wheel: docker run -it --rm -v "$(pwd)":/dist python:3.11 bash from the dist directory
