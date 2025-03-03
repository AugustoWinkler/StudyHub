package dioambiente.desafio5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class OrdenarPessoas {
	private List<Pessoa> listaPessoas = new ArrayList<>();

	public void adicionarPessoa(String nome, int idade, double altura) {
		Pessoa pessoa = new Pessoa(nome, idade, altura);
		listaPessoas.add(pessoa);
	}

	public List<Pessoa> ordernarPorIdade() {

		Collections.sort(listaPessoas);
		return listaPessoas;
	}

	public List<Pessoa> ordernarPorAltura() {
		Collections.sort(listaPessoas, new CompararPorAltura());

		return listaPessoas;
	}

	public List<Pessoa> getListaPessoas() {
		return listaPessoas;
	}

	public static void main(String[] args) {
		OrdenarPessoas ordernar = new OrdenarPessoas();

		ordernar.adicionarPessoa("Augusto", 23, 1.76);
		ordernar.adicionarPessoa("Mylena", 22, 1.55);
		ordernar.adicionarPessoa("Mauro", 25, 1.74);
		ordernar.adicionarPessoa("Caio", 21, 2.10);

		System.out.println(ordernar.getListaPessoas());
		System.out.println(ordernar.ordernarPorIdade());
		System.out.println(ordernar.ordernarPorAltura());
	}

}
