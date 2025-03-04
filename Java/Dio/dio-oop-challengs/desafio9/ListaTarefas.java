package dioambiente.desafio9;

import java.util.HashSet;
import java.util.Set;

public class ListaTarefas {
	Set<Tarefa> tarefas = new HashSet<>();

	public void adicionarTarefa(String descricao) {
		Tarefa tarefa = new Tarefa(descricao);
		tarefas.add(tarefa);
	}

	public void removerTarefa(String descricao) {
		tarefas.removeIf(t -> t.getDescricao().equals(descricao));
	}

	public void exibirTarefa() {
		System.out.println(tarefas.toString());
	}

	public int contarTarefas() {
		return tarefas.size();
	}

	public Set<Tarefa> tarefasConcluidas() {
		Set<Tarefa> concluidas = new HashSet<>();

		if (!tarefas.isEmpty()) {
			for (Tarefa t : tarefas) {
				if (t.getConcluida().equals(true)) {
					concluidas.add(t);
				}
			}
		}
		return concluidas;
	}

	public Set<Tarefa> tarefasPendentes() {
		Set<Tarefa> pendentes = new HashSet<>();

		if (!tarefas.isEmpty()) {
			for (Tarefa t : tarefas) {
				if (t.getConcluida().equals(false)) {
					pendentes.add(t);
				}
			}
		}
		return pendentes;
	}

	public void marcarConcluida(String descricao) {
		for (Tarefa x : tarefas) {
			if (x.getDescricao().equalsIgnoreCase(descricao)) {
				x.setConcluida(true);
			}
		}
	}

	public void marcarPendente(String descricao) {
		for (Tarefa x : tarefas) {
			if (x.getDescricao().equalsIgnoreCase(descricao)) {
				x.setConcluida(false);
			}
		}
	}

	public void limparTarefas() {
		this.tarefas = new HashSet<>();
	}

}
