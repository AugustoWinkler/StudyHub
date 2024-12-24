module teste {
	requires javafx.controls;
	requires javafx.fxml;
	requires javafx.base;
	requires javafx.graphics;
	
	opens model to javafx.graphics, javafx.fxml;
	opens controller to javafx.fxml;
}
