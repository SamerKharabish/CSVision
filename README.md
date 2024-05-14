# CSVision

Data visualization tool designed to render data from CSV files into interactive line charts

This module contains the GUI implementation for a CSV plotter application. It provides a graphical user interface built with customtkinter that allows users to load data from CSV files, visualize the data in a plot, and interact with the data using various controls.

![Files](https://tokei.rs/b1/github/SamerKharabish/CSVision?category=files)
![Code](https://tokei.rs/b1/github/SamerKharabish/CSVision?category=code)
![Lines](https://tokei.rs/b1/github/SamerKharabish/CSVision?category=lines)

## Structure overview

To enhance maintainability, scalability, and testability of the application a Model-View-Controller (MVC) architecture pattern is used, which decouples the business logic from the UI.

```bash
CSVision/
├── controllers/                    # Contains classes that act as intermediaries
                                    # between models and views. They handle user
                                    # input, update models, and reflect changes
                                    # in views.
│ ├── main_controller.py            # Handles interactions in the main window.
│ ├── plot_frame_controller.py      # Handles interactions in the plot frame.
│ ├── header_frame_controller.py    # Handles interactions in the header frame.
│ └── statusbar_frame_controller.py # Handles interactions in the status bar frame.
├── models/                         # Contains classes that represent the data
                                    # and business logic of the application.
│ ├── csv_data_manager.py           # Handles CSV file related operations.
│ └── yaml_manager.py               # Handles YAML file related operations.
├── resources/                      # Images, test files, etc.
├── unittests/                      # Automated tests for the application.
│ ├── test_csv_data_manager.py      # Tests the CSV file related operations.
│ └── test_yaml_manager.py          # Tests the YAML file related operations.
├── utils/                          # Utility functions and classes
│ ├── helper_functions.py           # General helper functions
│ ├── input_entry_list.py           # Custom input entry
│ ├── observer_publisher.py         # Observer pattern
│ └── tristate_button.py            # Custom tristate button
├── views/                          # Contains classes that define the visual
                                    # representation of the application.
│ ├── configurations_view.py        # The visual configuration of all views.
│ ├── main_view.py                  # The visual representation of main window.
│ ├── plot_frame_view.py            # The visual representation of the plot frame.
│ ├── header_frame_view.py          # The visual representation of the header
                                    # frame.
│ └── statusbar_frame_view.py       # The visual representation of the status bar
                                    # frame.
├── app.py                          # Entry point of the application.
├── README.md                       # README
└── requirements.txt                # Project dependencies.
```

## Features

- ```Accessibility```: Application is closable by pressing the "exit/close" button or the ESC-key
- ```Accessibility```: The header frame can be toggled by pressing 'Ctrl + B' or the button in the sidebar.
- ```Functionality```: CSV files can be selected and loaded with the "Open file button" in the File Explorer section.
- ```Functionality```: CSV files can be exported to xslx files with the "Export to excel button" in the File Explorer section.
- ```Feedback```: Processes are being displayed by a progressbar in the statusbar.
- ```Feedback```: File sizes are being displayed in the statusbar.

## Feedback

If you have any feedback, please reach out to me.

## Author

- [@Samer Kharabish](<kharabishsamer@outlook.com>)
