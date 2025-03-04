package dioambiente.desafio7;

import java.util.HashSet;
import java.util.Set;

public class ConjuntoPalavrasUnicas {
	private Set<String> palavrasSet;

	public ConjuntoPalavrasUnicas() {
		palavrasSet = new HashSet<>();
	}

	public void adicionarPalavra(String palavra) {
		palavrasSet.add(palavra);
	}

	public void removerPalavra(String palavra) {
		palavrasSet.remove(palavra);
	}

	public Boolean verificarPalavra(String palavra) {
		return palavrasSet.contains(palavra);
	}

	public void exibirPalavrasUnicas() {
		System.out.println(palavrasSet.toString());
	}

}
