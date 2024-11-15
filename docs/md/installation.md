This guide provides instructions for installing the **dual_autodiff** package and its CPython extension, along with steps to build the package as wheels for distribution.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.10 or 3.11
- [Docker](https://www.docker.com/) (for building wheels on Linux)
- [pip](https://pip.pypa.io/en/stable/installation/)
- (Optional) Virtual environment manager (e.g., `venv` or `virtualenv`)

## Installation Steps

### Step 1: Set up a Virtual Environment (Recommended)

It’s recommended to create a virtual environment to isolate dependencies.

```bash
python3 -m venv env
source env/bin/activate
```

### Step 2: Install the Main Package
To install the **dual_autodiff** package in "editable" mode:

```bash
pip install -e .
```

For development purposes, you may also install additional dependencies:

```bash
pip install -e ".[dev]"
```

### Step 3: Install the CPython Extension (dual_autodiffx)

The **dual_autodiffx** directory contains the CPython extension for dual_autodiff. Navigate to this directory and install it in "editable" mode as well:
```bash
cd dual_autodiffx
pip install -e .
cd ..
```

## Building Wheels for Distribution

To build the wheels for different Python versions, use the **cibuildwheel** tool within a Docker environment. This process will generate the wheels in the dist directory.

Run the Wheel Build Script
A shell script (**buildwheels.sh**) is provided in the **dual_autodiffx** directory. This script will build wheels for the specified Python versions using Docker.

1) Ensure Docker is running on your system.
2) Run the script:

```bash
cd dual_autodiffx
./buildwheels.sh
```

To give permissions for this script to run you need to first run the below command. *BUT*, before you do, you should always read the script and understand it. 

```bash
chmod +x buildwheels.sh
```