package ch04;

public class Q3 {

	public static void main(String[] args) {
		int sum = 0;
		int totalSum = 0;
		for(int i=1; i<=10; i++) {
			sum += i;
			totalSum += sum;
		}
		
		System.out.println(totalSum);
	}

}



/*

		int sum = 0;
		
		for (int i=1; i<=10; i++) {
			for (int j=1; j<=i; j++) {
				sum += j;
			}
		}
		
		System.out.println(sum);

*/