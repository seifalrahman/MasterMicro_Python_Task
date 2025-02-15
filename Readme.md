# Master Equation Solver Application

### Quick Start

1. Download the `.zip` file from the [Releases](https://github.com/seifalrahman/MasterMicro_Python_Task/releases) page.
2. Unzip The folder
3. Run the `.exe` file to launch the application.


Overview

The Equation Solver Application is a powerful tool designed to solve various types of mathematical equations. Whether you're dealing with linear equations, quadratic equations, or systems of equations, this application provides an intuitive interface and accurate solutions.
## Features

    Get Solution points of two single variable Equations
    User-Friendly Interface: Simple and intuitive interface for easy input and output.
    The info Button gets the Differentiated equation and the  inegrated equation 
### After pressing Info Button for both equations
![image](https://github.com/user-attachments/assets/919d7b89-0bde-4d14-8b17-93816b851c67)
### Solve Button gets the solution points and
![image](https://github.com/user-attachments/assets/fd5db199-18ba-4ae4-b603-37007c951005)

## Technologies Used

        Programming Language: Python

  ### Libraries:
        sympy
        matplotlib 
        numpy 
        PySide2
        Testing :  Pytest 
                   Pytest-qt
# Supported Operations 
    + - / * ^ log10() sqrt().
        Note : You can write log operations in two ways  log10(x) and log(x,10)

# Input violations 
    Only 'x' variable is allowed 
        - Info Button is disabled if you entered another variable 
        - Warning appears If You tried to press Info while having illegal variables 
![image](https://github.com/user-attachments/assets/7676a71b-008b-4b0f-8055-f603f83ea49d)     
![image](https://github.com/user-attachments/assets/79fe2c96-a667-48d6-9748-4b4cd516f1b7)




# Logical Test Results 
![image](https://github.com/user-attachments/assets/f2d512b0-b8ab-499b-82d7-95f9e393781a)
![image](https://github.com/user-attachments/assets/c175b4cf-60ea-49c1-9e43-12f42a4eab7d)


# Gui Test Results
![image](https://github.com/user-attachments/assets/d1e97564-3041-4e06-9931-1719159402ab)
![image](https://github.com/user-attachments/assets/79918106-dd77-482e-9d75-6e5f50fdf691)
![image](https://github.com/user-attachments/assets/7469b242-1425-4238-a6ae-7a2717210aa3)
![image](https://github.com/user-attachments/assets/73262cbf-913a-439c-8ee2-7a2d9cf8f615)
![image](https://github.com/user-attachments/assets/303628f3-1159-47ff-9c35-bcdc58ade972)
![image](https://github.com/user-attachments/assets/84e4bd65-ea7c-4286-b98c-88cc107d06d3)
#### The only not fully automated test

![image](https://github.com/user-attachments/assets/3c80bf21-fd1b-4dc2-b63b-0ca0ab5410c5)





# SnapShots of Working examples

![image](https://github.com/user-attachments/assets/46da0618-dc12-4392-9f50-102a9ab84e88)

![image](https://github.com/user-attachments/assets/676a54dc-9537-45d2-9bc9-b34b9e26cfbb)

![image](https://github.com/user-attachments/assets/6797b47c-c9ff-49df-a0b2-6e5304ca088d)


![image](https://github.com/user-attachments/assets/2c57d346-3523-4a45-a119-38c83b2d67c1)



# Note If Equation is to be solved numerically and only one solution is found while in fact it has larger number of solutions , this could be partially solved by providing more initial guesses
