package ch04;

public class Q4 {

	public static void main(String[] args) {
		int num = 1;
		int sum = 0;
		
		for (num = 1; true; num++) {
			if (num % 2 == 1) {
				sum += num;
			} else {
				sum += (-num);
			}
			
			if (sum >= 100)
				break;
		}
		
		System.out.println(num);
	}

}

/*

		int num = 1;
		int sum = 0;
		
		for (num = 1; sum < 100; num++) {
			if (num % 2 == 1) {
				sum += num;
			} else {
				sum += (-num);
			}
		}
		
		System.out.println(num-1);



		int sum = 0;
		int s = 1;
		int num = 0;
		
		for(int i=1; true; i++, s=-s) {
			num = s*i;
			sum += num;
			
			if(sum >= 100)
				break;
		}
		
		System.out.println(num);
*/