# ModSim-Gruppe15
Simulation about Evolution of Blood Types

This project models the evolution of blood types in a population using an Agent-Based Model (ABM) implemented in Python. It simulates inheritance, mutation, and reproduction processes based on Mendelian genetics to explore how blood type distributions evolve over time.
Features

  +Agent-Based Design: Each individual is represented as an object with attributes like genotype, phenotype, sex, and fitness.
  +Inheritance Rules: Implements Mendelian genetics for allele inheritance.
  +Evolutionary Dynamics: Simulates key processes:
        -Random reproduction based on agent fitness.
        -Mutation to introduce new blood types.
        -Death events to remove agents dynamically.
  +Scalability: Efficient population management with Python data structures.

## Setup Instructions
1. Install [Python](https://www.python.org/downloads/) (Version 3.11 or higher required)
1. Create a Virtual Environment: Use the venv module (comes with Python) to create a virtual environment.
      ``` bash
      python -m venv mesa_env
      ```
1. Activate the Virtual Environment:
      - On Windows:
      ``` bash
      mesa_env\Scripts\activate
      ```
      - On macOS/Linux:
      ``` bash
      source mesa_env/bin/activate
      ```

1. Upgrade pip: Before installing dependencies, ensure pip is up to date.
      ``` bash
      pip install --upgrade pip
      ```

1. Install Dependencies from `requirements.txt`: Run the following command after activation:
      ``` bash
      pip install -r requirements.txt
      ```

1. Start Jupyter in browser:
      ``` bash
      jupyter lab
      ```

      OR

      When using VS code install [Jupyter Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) and open Juypter notebook `model_template.ipynb`.