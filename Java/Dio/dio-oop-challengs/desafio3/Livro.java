package dioambiente.desafio3;


public class Livro {
	private String titulo;
	private String autor;
	private int ano;

	public Livro(String titulo, String autor, int ano) {
		super();
		this.titulo = titulo;
		this.autor = autor;
		this.ano = ano;
	}

	@Override
	public String toString() {
		return "Livro [titulo=" + titulo + ", autor=" + autor + ", ano=" + ano + "]";
	}

	public String getTitulo() {
		return titulo;
	}

	public String getAutor() {
		return autor;
	}

	public int getAno() {
		return ano;
	}

}
