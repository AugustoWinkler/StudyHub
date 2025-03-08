package dio.sudoku.model;

public enum GameStatusEnum {
	NON_STARTED("Não iniciado"), INCOMPLETE("Incompleto"), COMPLETE("Completo");

	private String label;

	GameStatusEnum(final String label) {
		this.label = label;
	}

	public String getLabel() {
		return label;
	}

}
