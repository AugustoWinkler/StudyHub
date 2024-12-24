package controller;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import model.TextModel;

public class ControllerCNC {
	@FXML
    private TextField inputField;
	
	@FXML
    private Label displayLabel;

    private TextModel textModel;
	
	
	
    @FXML
    public void initialize() {
        this.textModel = new TextModel(); // Inicializa o modelo aqui
    }
    
	@FXML
	public void updateText(ActionEvent event)  {
		// Obtém o valor do TextField e atualiza o Model
        textModel.setText(inputField.getText());

        // Atualiza o Label com o valor do Model
        displayLabel.setText(textModel.getText());
			
		}
}
