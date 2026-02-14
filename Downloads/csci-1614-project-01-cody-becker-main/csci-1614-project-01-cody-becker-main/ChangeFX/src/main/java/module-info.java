module edu.okcu.changefx {
    requires javafx.controls;
    requires javafx.fxml;


    opens edu.okcu.changefx to javafx.fxml;
    exports edu.okcu.changefx;
}