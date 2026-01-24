package com.mycompany.sample;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

public class Main extends Application {
    boolean showingResult = false; //# replaces not adds on to calc
    int firstNumber; //Stores first #
    int secondNumber; //Stores second #
    String operator; //Stores operation that is chosen
    int result; //Stores result

    @Override
    public void start(Stage stage) {
        TextField display = new TextField();
        display.setEditable(false);

        // Number buttons
        Button zeroButton = new Button("0");
        zeroButton.setOnAction(e -> {
            if (showingResult) {
                display.setText("0");
                showingResult = false;
            } else {
                display.setText(display.getText() + "0");
            }
        });

        Button oneButton = new Button("1");
        oneButton.setOnAction(e -> {
            if (showingResult) {
                display.setText("1");
                showingResult = false;
            } else {
                display.setText(display.getText() + "1");
            }
        });

        Button twoButton = new Button("2");
        twoButton.setOnAction(e -> {
           //Makes it so display cant be added to, either resets calc or operation is required
            if (showingResult) {
                display.setText("2");
                showingResult = false;
            } else {
                display.setText(display.getText() + "2");
            }
        });

        Button threeButton = new Button("3");
        threeButton.setOnAction(e -> {
            if (showingResult) {
                display.setText("3");
                showingResult = false;
            } else {
                display.setText(display.getText() + "3");
            }
        });

        Button fourButton = new Button("4");
        fourButton.setOnAction(e -> {
            if (showingResult) {
                display.setText("4");
                showingResult = false;
            } else {
                display.setText(display.getText() + "4");
            }
        });

        Button fiveButton = new Button("5");
        fiveButton.setOnAction(e -> {
            if (showingResult) {
                display.setText("5");
                showingResult = false;
            } else {
                display.setText(display.getText() + "5");
            }
        });

        Button sixButton = new Button("6");
        sixButton.setOnAction(e -> {
            if (showingResult) {
                display.setText("6");
                showingResult = false;
            } else {
                display.setText(display.getText() + "6");
            }
        });

        Button sevenButton = new Button("7");
        sevenButton.setOnAction(e -> {
            if (showingResult) {
                display.setText("7");
                showingResult = false;
            } else {
                display.setText(display.getText() + "7");
            }
        });

        Button eightButton = new Button("8");
        eightButton.setOnAction(e -> {
            if (showingResult) {
                display.setText("8");
                showingResult = false;
            } else {
                display.setText(display.getText() + "8");
            }
        });

        Button nineButton = new Button("9");
        nineButton.setOnAction(e -> {
            if (showingResult) {
                display.setText("9");
                showingResult = false;
            } else {
                display.setText(display.getText() + "9");
            }
        });

        // Operator buttons, sets first # and operation
        Button plusButton = new Button("+");
        plusButton.setOnAction(e -> {
            firstNumber = Integer.parseInt(display.getText());
            operator = "+";
            display.clear();
        });

        Button minusButton = new Button("-");
        minusButton.setOnAction(e -> {
            firstNumber = Integer.parseInt(display.getText());
            operator = "-";
            display.clear();
        });

        Button multiplyButton = new Button("*");
        multiplyButton.setOnAction(e -> {
            firstNumber = Integer.parseInt(display.getText());
            operator = "*";
            display.clear();
        });

        Button divideButton = new Button("/");
        divideButton.setOnAction(e -> {
            firstNumber = Integer.parseInt(display.getText());
            operator = "/";
            display.clear();
        });

        Button modulus = new Button("%");
        modulus.setOnAction(e -> {
            firstNumber = Integer.parseInt(display.getText());
            operator = "%";
            display.clear();
        });




        Button clearButton = new Button("C");
        clearButton.setOnAction(e -> display.clear());

        // Equals button, perform the chosen operation
        Button equalButton = new Button("=");
        equalButton.setOnAction(e -> {
            secondNumber = Integer.parseInt(display.getText());

            if (operator.equals("+")) {
                result = CalculatorLogic.add(firstNumber, secondNumber);
            } else if (operator.equals("-")) {
                result = CalculatorLogic.subtract(firstNumber, secondNumber);
            } else if (operator.equals("*")) {
                result = CalculatorLogic.multiply(firstNumber, secondNumber);
            } else if (operator.equals("/")) {
                if (secondNumber != 0) {
                    result = CalculatorLogic.divide(firstNumber, secondNumber);
                } else {
                    display.setText("Error");
                    return;
                }
            } else if (operator.equals("%")) {
                result = CalculatorLogic.modulus(firstNumber, secondNumber);
            }


            display.setText(String.valueOf(result));
            firstNumber = result;
            showingResult = true;
        });

        // Layout grid
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);

        // First row (display)
        grid.add(display, 0, 0, 4, 1);

        // Second row (7, 8, 9, +)
        grid.add(sevenButton, 0, 1);
        grid.add(eightButton, 1, 1);
        grid.add(nineButton, 2, 1);
        grid.add(plusButton, 3, 1);

        // Third row (4, 5, 6, -)
        grid.add(fourButton, 0, 2);
        grid.add(fiveButton, 1, 2);
        grid.add(sixButton, 2, 2);
        grid.add(minusButton, 3, 2);

        // Fourth row (1, 2, 3, *)
        grid.add(oneButton, 0, 3);
        grid.add(twoButton, 1, 3);
        grid.add(threeButton, 2, 3);
        grid.add(multiplyButton, 3, 3);

        // Fifth row (0, /, =, C)
        grid.add(zeroButton, 0, 4);
        grid.add(divideButton, 1, 4);
        grid.add(equalButton, 2, 4);
        grid.add(clearButton, 3, 4);
        grid.add(modulus, 0, 5);

        // Scene setup
        Scene scene = new Scene(grid, 300, 300);
        stage.setScene(scene);
        stage.setTitle("Cody's Calculator 9000");
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
