public class MethodEx1 {

	public static void main(String[] args) { 
		
		int plusResult1 = plus(1, 2);
		int plusResult2 = plus(100, 4323);
		
		System.out.println(plusResult1);
		System.out.println(plusResult2);
		printTwice("OO-AH");

	}
	
	static void printTwice(String text) {
		System.out.println(text);
		System.out.println(text);
	}
	
	static int plus(int x, int y) {
		return x + y;
	}

}
