# Section_00

* 변수
* 연산자
* 조건문 (if ~ else if ~ else)
* 배열
* 반복문 (for, while)

***

1강 핸드아웃 코드

``` java

// 로또 자동 발급 프로그램 만들기

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

```




