# Final Project for Software Development Retraining
This project was the final assignment for the first semester of my retraining as an application development specialist. 
The goal of the project was to implement Python structure and organization, collaborate with a system integrator, and create a program in Python that works with a MySQL database on a Raspberry Pi.

## Project Goal
The number converter program allows users to convert a given number into different number types. The conversions can be from Decimal to Binary or Hexadecimal, from Binary to Decimal or Hexadecimal, or from Hexadecimal to Decimal or Binary.

## Requirements
The program runs only after a successful user login through a database check. After logging in, the user selects a conversion type and enters a number, which is then validated for errors. If the input is correct, the conversion is performed, and the result is displayed. 
The program will keep running until the user either exits through a prompt or presses a specific key. A safety confirmation will always appear before exiting.
The program can optionally be installed on a Raspberry Pi, with access to a database that stores and verifies user login credentials.

## Program Structure
The program is modular and consists of several files to separate tasks and simplify maintenance:

- main.py: Central control unit that imports functions from other modules and orchestrates the process (e.g., login, conversion, program control).
- login.py: Manages user login and registration, using functions from authentifizierung.py for verification or creating new users.
- authentifizierung.py: Provides authentication logic (e.g., db_connect(), login(), register()).
- zahlenkonverter.py: Contains the conversion logic, number input handling, and actual conversions (e.g., dez_zu_hex(), bin_zu_dez()).
- beenden.py: Manages program controls (e.g., weiter_machen(), sicherheitsabfrage()).

## Special Notes
The program is written in German, including most of the comments in the code. Additionally, each file contains the statement if __name__ == "__main__": to ensure that functions are only executed in main.py, not when the files are imported.
