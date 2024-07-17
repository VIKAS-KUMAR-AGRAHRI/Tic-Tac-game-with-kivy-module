
# Color Tic-Tac-Game

This project is a simple and straightforward game similar to Tic-Tac-Game, developed in Python using the Kivy module for the GUI. Instead of using X and O, this game uses the colors red and green.

## Features
- Interactive GUI built with Kivy
- Two-player gameplay with color markers
- Simple and intuitive interface

## Requirements
- Python 3.x
- Kivy

## Installation

1. Clone this repository to your local machine:
    ```https://github.com/VIKAS-KUMAR-AGRAHRI/Tic-Tac-game-with-kivy-module
    cd Tic-Tac-Game
    ```

2. Install the required dependencies:
    ```bash
    pip install kivy
    ```

3. Run the game:
    ```bash
    python main.py
    ```

## How to Play

1. The game board consists of a 3x3 grid.
2. Two players take turns clicking on the grid to place their color (red or green).
3. The first player to get three of their colors in a row (horizontally, vertically, or diagonally) wins.
4. If all nine squares are filled without any player getting three in a row, the game is a draw.

## APK

An APK of the game is also provided for Android users. You can download and install the APK file on your Android device to play the game.
download link 
https://drive.google.com/file/d/1xHm8pfHzRO0U8lANvlqRryGCNEezr4Qg/view?usp=drivesdk

## Building the APK

To build the APK yourself, you can use Buildozer. Follow these steps:

1. Install Buildozer:
    ```bash
    pip install buildozer
    ```

2. Initialize Buildozer in your project directory:
    ```bash
    buildozer init
    ```

3. Edit the `buildozer.spec` file to configure your build settings.

4. Build the APK:
    ```bash
    buildozer android debug
    ```

5. The APK file will be located in the `bin` directory.

## Screenshots

Include screenshots of your game here.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Kivy](https://kivy.org) for providing an excellent framework for building the GUI.

## Contact

If you have any questions or feedback, feel free to contact me at jpvikash7237@gmail.com
