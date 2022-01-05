import java.util.Random;

public class BuyLotto {

	public static void main(String[] args) {
			
		Random random = new Random();
		int money = 10000;
		
		while (money >= 1000) {
			// buy lotto
			money -= 1000;
			int number = random.nextInt(100);
			int lottoMoney = buyLotto(number);
			System.out.println("My Number is " + number + " / Lotto : " + buyLotto(number));
			money += lottoMoney;
			System.out.println("My Money is"  + money);
		}
		System.out.println("Lose..");
	}
	
static int buyLotto(int number) {
	
	int[] lotto = new int[100];
	
	for(int i = 0; i < lotto.length; i++) {
		lotto[i] = 0;
	}
	lotto[2] = 100;
	lotto[77] = 3000;
	lotto[99] = 500;
	
	return lotto[number];
}

}
