package ch04;

public class FlowEx24 {

	public static void main(String[] args) {
		int i = 11;
		
		System.out.println("ī���� �ٿ��� �����մϴ�.");
		
		while (i-- != 0) {
			System.out.println(i);
			
			for (long j=0; j<2_000_000_000_000_000_00L; j++) {
				;
			}
		}
		System.out.println("GAME OVER");
	}
}
