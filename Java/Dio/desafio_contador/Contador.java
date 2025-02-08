package desafio_contador;

import java.util.Scanner;

public class Contador {
	public static void main(String[] args) {
		Scanner terminal = new Scanner(System.in);
		System.out.println("Digite o primeiro parâmetro");
		int parametroUm = terminal.nextInt();
		System.out.println("Digite o segundo parâmetro");
		int parametroDois = terminal.nextInt();

		try {
			contar(parametroUm, parametroDois);

		} catch (ParametrosInvalidosException exception) {
			exception.printStackTrace();
			System.out.println("O segundo parâmetro deve ser maior que o primeiro");
		} finally {
			terminal.close();
		}
	}

	public static class ParametrosInvalidosException extends Exception {
		public ParametrosInvalidosException(String message) {
			super(message);
		}
	}

	static void contar(int parametroUm, int parametroDois) throws ParametrosInvalidosException {
		if (parametroUm > parametroDois) {
			throw new ParametrosInvalidosException("O segundo parâmetro deve ser maior que o primeiro");
		}

		int contagem = parametroDois - parametroUm;

		for (int i = parametroUm; i < parametroDois; i++) {
			System.out.println("Imprimindo o número " + (i - parametroUm + 1));
		}
	}
}