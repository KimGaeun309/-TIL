package weekD;

// Executors 클래스를 활용한 스레드 작성
/*
 * 새로운 Concurrency API는 ExecutorService라는 개념을 도입
 * 개발자가 스레드를 직접 생성해 실행하는 것이 아닌, 시스템이 스레드 관리를 맡도록 하는 것
 * Executor 인터페이스는 스레드 풀(thread pool)에 스레드 여러 개를 모아서 실행할 수 있다.
 * Executors 클래스는 여러 개의 팩토리 메소드(factory method)를 가지고 있다.
 */

import java.util.concurrent.Executor; // Executor interface 
import java.util.concurrent.Executors; // Executor class

public class ThreadTestExecutor {

	public static void main(String[] args) {
		Runnable r1 = () -> {
			for (int i=10; i>=0; i--)
				System.out.println("첫 번째 스레드: " + i);
		};
		Runnable r2 = () -> {
			for (int i=10; i>=0; i--)
				System.out.println("두 번째 스레드: " + i);
		};
		
		Executor executor = Executors.newCachedThreadPool();
		executor.execute(r1);
		executor.execute(r2);
	}

}
