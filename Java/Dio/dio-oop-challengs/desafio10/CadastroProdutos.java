package dioambiente.desafio10;

import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class CadastroProdutos {
	Set<Produto> produtos = new HashSet<>();

	public void adicionarProduto(long cod, String nome, double preco, int quantidade) {
		Produto produto = new Produto(cod, nome, preco, quantidade);
		produtos.add(produto);
	}

	public Set<Produto> exibirProdutosPorNome() {
		Set<Produto> produtoPorNome = new TreeSet<>(new ExibirPorNome());
		produtoPorNome.addAll(produtos);
		return produtoPorNome;

	}

	public Set<Produto> exibirProdutosPorPreco() {
		Set<Produto> produtoPorPreco = new TreeSet<>(new ExibirPorPreco());
		produtoPorPreco.addAll(produtos);
		return produtoPorPreco;
	}

}
