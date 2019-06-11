import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class Hangman {

	public static void main(String[] args) throws FileNotFoundException, IOException {
		printSplash();
		String word;
		word = getWordFromFile();
		start(word);
	}

	private static String getWord() {
		String[] words = { "book", "business", "company", "government", "home", "student", "water", "people", "money",
				"group", "child", "newspaper", "comprehension", "conversation", "communicate", "vocabulary" };

		Random rand = new Random();
		int index = rand.nextInt(words.length);

		return words[index];
	}

	private static String getWordFromFile() throws FileNotFoundException, IOException {
		String fileName = "words.txt";
		File file = new File(fileName);
		FileReader fr;
		fr = new FileReader(file);
		BufferedReader br = new BufferedReader(fr);
		String line = br.readLine();
		String[] words = line.split(",");

		Random rand = new Random();
		int index = rand.nextInt(words.length);

		return words[index];
	}

	private static void printSplash() {
		System.out.println(" _                                             \r\n"
				+ "| |                                            \r\n"
				+ "| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  \r\n"
				+ "| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ \r\n"
				+ "| | | | (_| | | | | (_| | | | | | | (_| | | | |\r\n"
				+ "|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|\r\n"
				+ "                    __/ |                      \r\n" + "                   |___/      ");
		System.out.println(" ___________.._______\r\n" + "| .__________))______|\r\n" + "| | / /      ||\r\n"
				+ "| |/ /       ||\r\n" + "| | /        ||.-''.\r\n" + "| |/         |/  _  \\\r\n"
				+ "| |          ||  `/,|\r\n" + "| |          (\\\\`_.'\r\n" + "| |         .-`--'.\r\n"
				+ "| |        /Y . . Y\\\r\n" + "| |       // |   | \\\\\r\n" + "| |      //  | . |  \\\\\r\n"
				+ "| |     ')   |   |   (`\r\n" + "| |          ||'||\r\n" + "| |          || ||\r\n"
				+ "| |          || ||\r\n" + "| |          || ||\r\n" + "| |         / | | \\\r\n"
				+ "\"\"\"\"\"\"\"\"\"\"|_`-' `-' |\"\"\"|\r\n" + "|\"|\"\"\"\"\"\"\"\\ \\       '\"|\"|\r\n"
				+ "| |        \\ \\        | |\r\n" + ": :         \\ \\       : :  sk\r\n"
				+ ". .          `'       . .\r\n" + "");

	}

	private static void start(String word) {
		int attempts = 10;
		String asteWord = new String();

		for (int i = 0; i < word.length(); i++) {
			asteWord += "*";
		}

		while (true) {
			System.out.println("You have " + attempts + " guesses");
			System.out.println("The word is:");
			System.out.println(asteWord);

			boolean isValidate;
			String guess = null;
			do {
				System.out.println("What is your guess?");
				Scanner in = new Scanner(System.in);
				guess = in.nextLine();
				isValidate = validateChar(guess);

				if (!isValidate)
					System.out.println("Invaild guess... try again...");

			} while (!isValidate);

			guess = guess.toLowerCase();

			if (word.contains(guess)) {
				char guessLatter = guess.toLowerCase().charAt(0);
				asteWord = replaceAll(asteWord.toCharArray(), word.toCharArray(), guessLatter);

			} else {
				attempts--;
			}

			if (attempts <= 0) {
				System.out.println("You loser! Bye Bye");
				break;
			}

			if (!asteWord.contains("*")) {
				System.out.println("Wow you are good!!");
				break;
			}

		}
	}

	private static String replaceAll(char[] asteWord, char[] word, char latter) {

		for (int i = 0; i < word.length; i++) {
			if (word[i] == latter)
				asteWord[i] = latter;

		}

		return String.valueOf(asteWord);

	}

	private static boolean validateChar(String guess) {
		char[] charArr = guess.toCharArray();

		if (charArr.length > 1)
			return false;

		if ('a' <= charArr[0] && charArr[0] <= 'z')
			return true;

		if ('A' <= charArr[0] && charArr[0] <= 'Z')
			return true;

		return false;
	}

}