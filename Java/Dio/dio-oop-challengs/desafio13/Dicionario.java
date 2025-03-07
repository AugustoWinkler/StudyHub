package dioambiente.desafio13;

import java.util.HashMap;
import java.util.Map;

public class Dicionario {
	private Map<String, String> dicionario;

	public Dicionario() {
		dicionario = new HashMap<>();
	}

	public void adicionarPalavra(String palavra, String deficinao) {
		dicionario.put(palavra, deficinao);
	}

	public void removerPalavra(String palavra) {
		dicionario.remove(palavra);
	}

	public void exibirPalavras() {
		System.out.println(dicionario);
	}

	public String pesquisarPorPalavra(String palavra) {
		return dicionario.get(palavra);
	}

}
