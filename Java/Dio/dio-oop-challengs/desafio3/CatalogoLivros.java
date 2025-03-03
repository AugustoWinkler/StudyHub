package dioambiente.desafio3;

import java.util.ArrayList;

public class CatalogoLivros {
	private ArrayList<Livro> catalogo = new ArrayList<>();

	public void adicionarLivro(String titulo, String autor, int ano) {
		Livro livro = new Livro(titulo, autor, ano);
		this.catalogo.add(livro);
	}

	public void pesquisarPorAutor(String autor) {
		catalogo.forEach(t -> {
			if (t.getAutor().equals(autor)) {
				System.out.println(t.toString());
			}
		});
	}

	public void pesquisarPorIntervalo(int inicio, int fim) {
		for (Livro l : catalogo) {
			if (l.getAno() >= inicio && l.getAno() <= fim) {
				System.out.println(l.toString());
			}
		}
	}

	public void pesquisarPorTitulo(String titulo) {
		for (Livro l : catalogo) {
			if (l.getTitulo().equalsIgnoreCase("Narnia")) {
				System.out.println(l.toString());
				break;
			}
		}
	}


}
