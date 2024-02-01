# CSVision

Data visualization tool designed to render data from CSV files into interactive line charts

This module contains the GUI implementation for a CSV plotter application. It provides a graphical user interface built with customtkinter that allows users to load data from CSV files, visualize the data in a plot, and interact with the data using various controls.

## Structure overview

To enhance maintainability, scalability, and testability of the application a Model-View-Controller (MVC) pattern will be used, which decouples the business logic from the UI.

CSVision/  
├── controllers/                    # Contains classes that act as intermediaries between models and views. They handle user input, update models, and reflect changes in views.  
│ └── main_controller.py            #  
├── models/                         # Contains classes that represent the data and business logic of the application.  
├── resources/                      # Images, test files, etc.  
├── unittests/                      # Automated tests for the application.  
├── views/                          # Contains classes that define the visual representation of the application.  
├── app.py                          # Entry point of the application.  
├── README.md                       # README  
└── requirements.txt                # Project dependencies.  

## Features

## Author

- [@Samer Kharabish](<kharabishsamer@outlook.com>)
