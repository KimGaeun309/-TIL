package Week3;
import java.util.Scanner;

public class Ex02_11b {

	public static void main(String[] args) {
		final int TARGETSALES = 1000;
		int mySales;
		int bonus;
		String result;
		
		Scanner input = new Scanner(System.in);
		System.out.print("실적을 입력하시오(단위: 만원); ");
		mySales = input.nextInt();
		
		if (mySales >= TARGETSALES) {
			result = "실적 달성";
			bonus = (mySales - TARGETSALES) / 10;
//          bonus = (mySales - TARGETSALES) * 0.1; // 타입이 맞지 않아 에러!
			// bonus 를 double로 바꾸면 연산이 가능해진다!
		} else {
			result = "실적 달성 못함";
			bonus = 0;
		}
		
		System.out.println(result + "\n" + "보너스 : " + bonus);
		
		input.close();
	}

}
