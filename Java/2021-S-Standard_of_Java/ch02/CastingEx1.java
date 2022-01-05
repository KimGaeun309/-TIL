package ch02;

public class CastingEx1 {

	public static void main(String[] args) {
		double d = 85.4;
		int score = (int)d;
		
		System.out.println("score="+score);
		System.out.println("d="+d);
	}

}
// float -> int 형변환할 때 소수점 이하의 값은 버림으로 처리된다!!
