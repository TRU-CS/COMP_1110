# COMP_1110

Welcome to the COMP_1110 repository! This repository contains the assignments and projects for the COMP_1110 course. The course focuses on fundamental concepts in computer science and programming, providing students with hands-on experience through various assignments and projects.

## Documentations:
- [Otter-grader](https://otter-grader.readthedocs.io/en/latest/otter_assign/notebook_format.html). This is a library to generate autograder zip file from a jupyter notebook.
- [Gradescope](https://gradescope-autograders.readthedocs.io/en/latest/specs/). This is a platform to host the autograder and run autotest againsts students submissions

## Contents

- **Assignments**: Imported assignments that need to be converted to autograder
- **Seminars**: Imported assignments that need  to be converted to autograder
- **source**: A folder that contains all the assignment solutions
- **release**: A folder that contains the students' version (without solutions), and the autograder zip file to be uploaded on Gradescope.
- **autograder**: ????

## Generating autograded assignemnts

To get started with the assignments and projects in this repository, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/COMP_1110.git
2. **Set up conda environment (Do this once)**:
   ```bash
   cd COMP_1110
   conda env create -f comp1110_env.yaml
3. **Activate conda environment**:
   ```bash
   conda activate comp1110

Now you have two options to generate autograded assignments depending on which format you use (jupyter notebook or python script)

<style>
summary {
  font-size: 1.5em;
  font-weight: bold;
}
</style>

<details>
<summary>Option 1: Jupyter Notebook</summary>
<br>

4. **Create your assignment using the template in `source/template` folder**:
   - `template.ipynb` is a Jupyter notebook that instructor used to create the assignment
   - `data` folder is where you can save datasets that you want students to use in the assignment
   - `img` folder is where you can save images that you want students to use in the assignment
   - `requirements.text` is where you can specify libraries that students need in this assignments, these libraries will be installed on Gradescope's Docker image
5. **Generate student's version and autograder zip files**:
   ```bash
   otter assign source/template/template.ipynb release/template

Replace the path and folder's name as appropriate. In this example, I run the command `otter assign` by retrieving the file from `source/template/template.ipynb` and the results will be exported to `release/template` folder

6. **Check your student version**:
    - You will be able to see the student's version under `release/template/student/template.ipynb`. Open this and make sure no solutions were included here
    - You can even type some answers and run the auto test cells to see if it works
    - There are two type of test cells: 
      - **visible** tests where students can see it directly in their notebook, and  
      - **hidden** tests where students cannot see it and it will only apply after they submit their work to Gradescope
    - Distribute work to students: Everything in the `release/template/student` folder including data, img, and the ipynb files will need to be shared with the students.
7. **Upload the autograder zip file to Gradescope**
    - Under `release/template/autograder` folder, you will see a `.zip` file which contains the autograder. Please upload them to Gradescope
</details>


<style>
summary {
  font-size: 1.5em;
  font-weight: bold;
}
</style>

<details>
<summary>Option 2: Python scripts</summary>
<br>

Insert here

</details>