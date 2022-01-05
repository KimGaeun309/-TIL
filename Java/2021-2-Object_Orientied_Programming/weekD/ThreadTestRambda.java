package weekD;

// 람다식(Rambda)을 이용한 스레드 작성

// 람다 연산자 ->

public class ThreadTestRambda {

	public static void main(String[] args) {
		Runnable task = () -> {
			for(int i=10; i>=0; i--)
				System.out.print(i+" ");
		};
		
		new Thread(task).start();
	}

}
