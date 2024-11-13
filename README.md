# COMP_1110

Welcome to the COMP_1110 repository! This repository contains the assignments and projects for the COMP_1110 course. The course focuses on fundamental concepts in computer science and programming, providing students with hands-on experience through various assignments and projects.

## Contents

- **Assignments**: Imported assignments that need to be converted to autograder
- **Seminars**: Imported assignments that need  to be converted to autograder

## Generating autograded assignemnts

To get started with the assignments and projects in this repository, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/COMP_1110.git
2. **Set up conda environment (Do this once)**:
   ```bash
   conda env create -f comp1110_env.yaml
3. **Activate conda environment**:
   ```bash
   conda activate comp1110
4. **Create your assignment using the template in `source/template` folder**:
   - `template.ipynb` is a Jupyter notebook that instructor used to create the assignment
   - `data` folder is where you can save datasets that you want students to use in the assignment
   - `img` folder is where you can save images that you want students to use in the assignment
   - `requirements.text` is where you can specify libraries that students need in this assignments, these libraries will be installed on Gradescope's Docker image
5. **Generate student's version and autograder zip files**:
Replace the path and folder's name as appropriate. In this example, I run the command `otter assign` by retrieving the file from `source/template/template.ipynb` and the results will be exported to `release/template` folder
   ```bash
   otter assign source/template/template.ipynb release/template
