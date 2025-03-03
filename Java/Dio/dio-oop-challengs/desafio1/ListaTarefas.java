package dioambiente.desafio1;

import java.util.ArrayList;

public class ListaTarefas {
	private ArrayList<Tarefa> lista = new ArrayList<>();
	
	public void adicionarTarefa(String descricao) {
		Tarefa novaTarefa = new Tarefa(descricao);
		this.lista.add(novaTarefa);
	}
	
	public void removerTarefa(String descricao) {
		lista.removeIf(t -> t.getDescricao().equalsIgnoreCase(descricao));
	}
	
	public int obterNumeroTotalTarefas() {
		return lista.size();
	}
	
	public void obterDescricaoTarefas() {
		int contador = 0;
		for(Tarefa t : lista) {
			contador++;
			System.out.printf("Tarefa numero: %d Descrição: %s%n", contador, t.getDescricao());
		}
	}

}
