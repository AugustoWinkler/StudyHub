package dioambiente.stream;

import java.util.Arrays;
import java.util.List;

public class PrecidateExample {
	public static void main(String[] args) {
		List<String> palavras = Arrays.asList("Java", "Kotlin", "Python", "JavaScript", "C", "Go");

		palavras.stream().filter(palavra -> palavra.length() > 5).forEach(System.out::println);
	}

}
