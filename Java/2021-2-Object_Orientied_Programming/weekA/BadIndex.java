package weekA;

public class BadIndex {

	public static void main(String[] args) {
		int[] array = new int[10];
		for(int i=0; i<10; i++)
			array[i] = 0;
		try {
			int result = array[12];
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("배역의 인덱스 잘못됨");
		}
		
		//int result = array[12]; // ArrayIndexOutOfBoundsException
		System.out.println("과연 이 문장이 실행될까요?");
		// 예외처리를 해주었기때문에 이 문장이 실행됩니다.

	}

}
