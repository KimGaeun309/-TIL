// 겜팔이의 안드로이드 세뇌교실 핸드아웃 001

import java.util.Date;
import java.util.Random;

public class LotteryMachine {

	public static void main(String[] args) {
		
		Date date = new Date();
		
		char myChar = 'A';
		
		System.out.println("GAMEPARI LOTTO");
		System.out.println(date);
		System.out.println("--------------------------------");
		for (int i = 0; i < 5; i++) {
			System.out.printf("%c : ", myChar++);
			PrintLottoNum();
		}
		System.out.println("--------------------------------");
		
	}
	
	static void PrintLottoNum() {
		Random random = new Random();
		int number = 0;
		for (int i = 0; i < 6; i++) {
			number = random.nextInt(45) + 1;
			System.out.printf("%d ", number);
		}
		System.out.println();
	}
	
}
