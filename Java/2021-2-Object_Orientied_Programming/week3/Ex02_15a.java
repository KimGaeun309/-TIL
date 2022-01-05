package Week3;
import java.util.Scanner;

public class Ex02_15a {

	public static void main(String[] args) {
		int month;
		int days = 0;
		
		System.out.print("일수를 알고 싶은 달을 입력하시오: ");
		Scanner scan = new Scanner(System.in);
		
		month = scan.nextInt();
		switch (month) {
		case 4:
		case 6:
		case 11:
			days = 30;
			break;
		case 2:
			days = 28;
			break;
			default:
				days = 31;
		}
		System.out.println("월의 날수는 " + days);
		
		scan.close();

	}

}
