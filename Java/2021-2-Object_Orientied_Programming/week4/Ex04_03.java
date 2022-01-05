package Week4;

import java.util.Scanner;

public class Ex04_03 {
	static int calc(int v1, int v2, int op) {
		int result;
		switch(op) {
		case 1: result = v1 + v2; break;
		case 2: result = v1 - v2; break;
		case 3: result = v1 * v2; break;
		case 4: result = v1 / v2; break;
		default: result = 0;
		}
		return result;
	}
	
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int res;
		int oper, a, b;
		System.out.printf("계산 입력 (1:+ 2:- 3:* 4:/): ");
		oper = s.nextInt();
		
		System.out.printf("첫 번째 숫자: ");
		a = s.nextInt();
		
		System.out.printf("두 번째 숫자: ");
		b = s.nextInt();
		
		res = calc(a, b, oper);
		
		System.out.printf("계산 결과는 : %d\n", res);
		s.close();
	}

}
