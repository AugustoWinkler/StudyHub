package dioambiente.desafio8;

import java.util.HashSet;
import java.util.Set;

public class AgendaContato {
	private Set<Contato> contatoSet = new HashSet<>();

	public void adicionarContato(String nome, int telefone) {
		contatoSet.add(new Contato(nome, telefone));
	}

	public void exibirContato() {
		System.out.println(contatoSet);
	}

	public Set<Contato> pesquisarPorNome(String nome) {
		Set<Contato> contatosPorNome = new HashSet<>();
		for (Contato c : contatoSet) {
			if (c.getNome().startsWith(nome))
				;
			contatosPorNome.add(c);
		}

		return contatosPorNome;
	}

	public void atualizerNumeroContato(String nome, int telefone) {
		for (Contato c : contatoSet) {
			if (c.getNome().equals(nome)) {
				c.setTelefone(telefone);
				break;
			}
		}
	}
}
