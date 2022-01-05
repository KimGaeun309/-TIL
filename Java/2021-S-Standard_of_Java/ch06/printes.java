package ch06;

public class printes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 13;
        double b = 0.165;
        
        System.out.printf("%d * %6lf = %6lf", a, (Math.round(b * 1000000)/1000000.0), Math.round(a*b * 1000000)/1000000.0);
	}

}
