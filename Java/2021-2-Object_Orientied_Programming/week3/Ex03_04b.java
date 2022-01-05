package Week3;

public class Ex03_04b {

	public static void main(String[] args) {
		for (int x = 0; x < 5; x++) {
			for(int y = 0; y < 5 - (x + 1); y++)
				System.out.print(" ");
			for(int y = 0; y < (2 * x) + 1; y++)
				System.out.print("+");
			System.out.println();
		}

	}

}
