package dioambiente.desafio9;

public class Tarefa {

	private String descricao;
	private Boolean concluida;

	public Tarefa(String descricao) {
		this.descricao = descricao;
		this.concluida = false;
	}

	public Boolean getConcluida() {
		return concluida;
	}

	public void setConcluida(Boolean concluida) {
		this.concluida = concluida;
	}

	public String getDescricao() {
		return descricao;
	}

	@Override
	public String toString() {
		return String.format("Descricao: %s Concluida: %s%n", descricao, concluida);
	}

}
