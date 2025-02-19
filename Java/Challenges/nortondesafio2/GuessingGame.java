package guessing;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class GuessingGame {

	// Min and Max value for random generated number.
	static int min = 0;
	static int max = 10;

	static Scanner s = new Scanner(System.in);

	static List<Integer> guessingHistory = new ArrayList<>();

	public static void main(String[] args) {
		String choice;

		while (true) {
			System.out.println("Type (Y) to start game or type (X) to exit.");
			choice = s.nextLine().trim().toUpperCase();

			switch (choice) {
			case "Y":
				guessingHistory.clear();
				initGame();
				break;
			case "X":
				System.out.println("Exiting the game. Bye!");
				return;
			default:
				System.out.println("Invalid choice. Please type (Y) to start or (X) to exit.");
				break;
			}

		}
	}

	public static void initGame() {
		Random random = new Random();
		int maxAttempts = (int) Math.ceil(Math.log(max) / Math.log(2));
		int attempts = 0;
		int randomNumber = min + random.nextInt(max);
		int guess;

		System.out.println(String.format("I think in a number between %d and %d", min, max));
		while (attempts <= maxAttempts) {
			guess = guess();

			if (guessingHistory.contains(guess)) {
				System.out.println(String.format("You already tried %d. Try a different number.", guess));
				continue;
			}

			guessingHistory.add(guess);
			attempts++;

			if (guess == randomNumber) {
				System.out.println(
						String.format("Congratulations! You guessed the correct number in %d attempts.", attempts));
				System.out.println("Your guess history: " + guessingHistory);
				break;
			} else if (guess < randomNumber) {
				System.out.println("The number is higher. Try again.");
			} else {
				System.out.println("The number is lower. Try again.");
			}

			if (attempts == maxAttempts - 1) {
				System.out.println("Last attempt.");
			} else if (attempts == maxAttempts) {
				System.out.println(
						"Sorry, you've reached the maximum number of attempts. The correct number was " + randomNumber);
				System.out.println("and you tried: " + guessingHistory);
				break;
			}
		}

	}

	public static int guess() {
		System.out.print("Guess: ");
		while (true) {
			try {
				int guessAttempt = Integer.parseInt(s.nextLine());
				if (guessAttempt >= min && guessAttempt <= max) {
					return guessAttempt;
				} else {
					System.out.println(
							String.format("Invalid guess, you should guess a number between %d and %d", min, max));
				}
			} catch (NumberFormatException e) {
				System.out.println(
						String.format("Invalid guess, you should guess a integer number between %d and %d", min, max));
			}
		}

	}
}
