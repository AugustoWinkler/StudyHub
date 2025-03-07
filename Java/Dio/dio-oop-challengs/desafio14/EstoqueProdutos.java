package dioambiente.desafio14;

import java.util.HashMap;
import java.util.Map;

public class EstoqueProdutos {
	private Map<Long, Produto> estoque = new HashMap<>();

	public void adicionarProduto(long cod, String nome, double preco, int quantidade) {
		estoque.put(cod, new Produto(nome, preco, quantidade));
	}

	public void exibirProdutos() {
		System.out.println(estoque);
	}

	public Double calcularValorEstoque() {
		double estoqueTotal = 0d;
		if (!estoque.isEmpty()) {
			for (Produto p : estoque.values()) {
				estoqueTotal += p.getQuantidade() * p.getPreco();
			}
		}
		return estoqueTotal;
	}

	public Produto obterProdutoMaisCaro() {
		Produto produto = null;
		double maiorPreco = Double.MIN_VALUE;
		for (Produto p : estoque.values()) {
			if (p.getPreco() > maiorPreco) {
				maiorPreco = p.getPreco();
				produto = p;
			}
		}
		return produto;
	}

	public Produto obterProdutoMaisBarato() {
		Produto produto = null;
		double menorPreco = Double.MAX_VALUE;
		for (Produto p : estoque.values()) {
			if (p.getPreco() < menorPreco) {
				menorPreco = p.getPreco();
				produto = p;
			}
		}
		return produto;
	}

	public Produto obterProdutoMaiorQuantidadeValorTotal() {
		Produto produto = null;
		double preco = Double.MIN_VALUE;
		for (Produto p : estoque.values()) {
			if ((p.getPreco() * p.getQuantidade()) > preco) {
				preco = (p.getPreco() * p.getQuantidade());
				produto = p;
			}
		}
		return produto;
	}

	public static void main(String[] args) {
		EstoqueProdutos estoque = new EstoqueProdutos();

		// Adicionando produtos
		estoque.adicionarProduto(1L, "Produto A", 10.50, 20);
		estoque.adicionarProduto(2L, "Produto B", 30.00, 10);
		estoque.adicionarProduto(3L, "Produto C", 5.00, 50);

		// Exibindo produtos
		System.out.println("Produtos no estoque:");
		estoque.exibirProdutos();

		// Calculando valor total do estoque
		System.out.println("\nValor total do estoque: R$ " + estoque.calcularValorEstoque());

		// Obtendo produto mais caro
		Produto maisCaro = estoque.obterProdutoMaisCaro();
		System.out.println("\nProduto mais caro: " + maisCaro);

		// Obtendo produto mais barato
		Produto maisBarato = estoque.obterProdutoMaisBarato();
		System.out.println("\nProduto mais barato: " + maisBarato);

		// Produto com maior valor total no estoque
		Produto maiorValorTotal = estoque.obterProdutoMaiorQuantidadeValorTotal();
		System.out.println("\nProduto com maior valor total no estoque: " + maiorValorTotal);
	}

}
