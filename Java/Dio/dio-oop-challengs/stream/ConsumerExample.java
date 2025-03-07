package dioambiente.stream;

import java.util.Arrays;
import java.util.List;

public class ConsumerExample {
	public static void main(String[] args) {
		List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5);

		numeros.stream().filter(s -> s % 2 == 0).forEach(System.out::println);

	}

}
