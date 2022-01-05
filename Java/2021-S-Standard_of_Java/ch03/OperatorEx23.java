package ch03;

public class OperatorEx23 {

	public static void main(String[] args) {
		String str1 = "abc";
		String str2 = new String("abc");
		
		System.out.printf("\"abc\"==\"abc\" ? %b%n", "abc"=="abc"); // true
		System.out.printf(" str1==\"abc\" ? %b%n", str1 == "abc"); // true
		System.out.printf(" str2==\"abc\" ? %b%n", str2 == "abc"); // false. 내용은 같지만 서로 다른 객체이기 때문.
		System.out.printf("str1.equals(\"abc\") ? %b%n", str1.equals("abc")); // true
		System.out.printf("str2.equals(\"abc\") ? %b%n", str2.equals("abc")); // true
		System.out.printf("str2.equals(\"ABC\") ? %b%n", str2.equals("ABC")); // false
		System.out.printf("str2.equalsIgnoreCase(\"ABC\") ? %b%n", str2.equalsIgnoreCase("ABC")); // true
	}

}
// 두 문자열을 비교할 때는, equals()라는 메서드를 사용해야 한다.
// equals()는 객체가 달라도 내용이 같으면 true 반환.
// equalsIgnoreCase()는 대소문자 구별하지 않고 비교.