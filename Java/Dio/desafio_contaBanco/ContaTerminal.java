package ContaBanco;

import java.util.Scanner;

public class ContaTerminal {

	public static void main(String[] args) {
		int numeroConta;
		String agenciaBanco;
		String nomeCliente;
		double saldo;

		Scanner t = new Scanner(System.in);

		System.out.println("Por favor, digite o número da Conta !");
		numeroConta = t.nextInt();
		System.out.println("Por favor, digite o número da Agência !");
		agenciaBanco = t.next();
		System.out.println("Por favor, digite o seu nome ! ");
		nomeCliente = t.nextLine();
		System.out.println("Por favor, digite o valor do saldo ! ");
		saldo = t.nextDouble();
		
		t.close();

		String format = String.format(
				"Olá %s, obrigado por criar uma conta em nosso banco, " + "sua agência é %s, conta %d e "
						+ "seu saldo %.2f já está disponível para saque",
				nomeCliente, agenciaBanco, numeroConta, saldo);
		System.out.println(format);
		
		
	}

}