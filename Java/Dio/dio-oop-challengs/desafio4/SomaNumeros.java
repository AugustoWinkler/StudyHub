package dioambiente.desafio4;

import java.util.ArrayList;

import java.util.List;

public class SomaNumeros {
	private List<Integer> numList = new ArrayList<>();

	public void adicionarNumero(int num) {
		this.numList.add(num);
	}

	public int calcularSoma() {
		int soma = 0;

		for (int num : numList) {
			soma += num;
		}
		return soma;
	}

	public int encontrarMaiorNumero() {
		int maior = 0;
		for (int num : numList) {
			if (maior < num) {
				maior = num;
			}
		}
		return maior;
	}

	public int encontrarMenorNumero() {
		int menor = numList.get(0);
		for (int num : numList) {
			if (num < menor) {
				menor = num;
			}
		}
		return menor;
	}

	public void exibirNumeros() {
		System.out.println(numList.toString());
	}

}
