package Week3;
import java.util.*;
// 최대공약수 구하기

public class Ex03_02c {

	public static void main(String[] args) {
		int x, y, r;
		
		System.out.print("두개의 정수를 입력하시오(큰수, 작은수)");
		Scanner scan = new Scanner(System.in);
		
		x = scan.nextInt();
		y = scan.nextInt();
		
		while(y != 0) {
			r = x % y;
			x = y;
			y = r;
		}
		
		System.out.println("최대공약수는 " + x);
		
		scan.close();
	}

}
