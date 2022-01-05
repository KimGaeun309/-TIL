package Week5;

public class Ex05_08 {

	public static void main(String[] args) {
		int[] deck = new int[52];
		String[] suits = {"Spades", "Hearts", "Diamonds", "Clubs"};
		String[] ranks = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9",
				"10", "Jack", "Queen", "King"};
		
		// initialize cards
		for (int i = 0; i < deck.length; i++)
			deck[i]  = i;
		
		// shuffle cards
		for (int i = 0; i < deck.length; i ++) {
			int index = (int)(Math.random() * deck.length);
			int temp = deck[i];
			deck[i] = deck[index];
			deck[index] = temp;
		}
		
		// display the first four cards
		for (int i=0; i<4; i++) {
			String suit = suits[deck[i]/13];
			String rank = ranks[deck[i]%13];
			System.out.println("Card number " + deck[i] + ": " + rank + " of " + suit);
		}
		

	}

}
