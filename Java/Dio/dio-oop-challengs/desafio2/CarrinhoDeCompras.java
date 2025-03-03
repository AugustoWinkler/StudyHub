package dioambiente.desafio2;

import java.util.ArrayList;

public class CarrinhoDeCompras {
	private ArrayList<Item> carrinho = new ArrayList<>();

	public void adicionarItem(String nome, double preco, int quantidade) {
		Item item = new Item(nome, preco, quantidade);
		carrinho.add(item);
	}

	public void removerItem(String nome) {
		carrinho.removeIf(i -> i.getNome().equalsIgnoreCase(nome));
	}

	public Double calcularValorTotal() {
		double total = 0;

		for (Item i : carrinho) {
			total += i.getPreco() * i.getQuantidade();
		}
		return total;
	}
	
	public void exibirItems() {
		System.out.println(carrinho);
	}
	

	public static void main(String[] args) {
		CarrinhoDeCompras carrinho =  new CarrinhoDeCompras();
		
		carrinho.adicionarItem("Pasta de dente", 45.50, 2);
		carrinho.adicionarItem("Bolacha", 12.70, 8);
		carrinho.adicionarItem("Salgadinho", 5, 3);
		
		carrinho.exibirItems();
		System.out.println(carrinho.calcularValorTotal());
		
		carrinho.removerItem("pasta de dente");
		
		carrinho.exibirItems();
		System.out.println(carrinho.calcularValorTotal());
	}

}
