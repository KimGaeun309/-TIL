package Week4;

// 인수와 매개변수 예제

class Math_sum {
	int add(int x, int y) {
		return x + y;
	}
}


public class Ex04_07 {
	
	public static void main(String[] args) {
		int sum;
		Math_sum obj = new Math_sum();
		sum = obj.add(2, 3);
		System.out.println("2와 3의 합은 " + sum);
		sum = obj.add(7, 8);
		System.out.println("7과 8의 합은 " + sum);

	}

}
