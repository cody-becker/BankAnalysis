package edu.okcu.changefx;

import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class ChangeController {
    @FXML
    private Label welcomeText;

    @FXML
    protected void onHelloButtonClick() {
        welcomeText.setText("Welcome to JavaFX Application!");
    }
}