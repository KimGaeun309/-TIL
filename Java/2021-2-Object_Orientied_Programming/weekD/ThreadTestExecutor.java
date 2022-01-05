package weekD;

// Executors Ŭ������ Ȱ���� ������ �ۼ�
/*
 * ���ο� Concurrency API�� ExecutorService��� ������ ����
 * �����ڰ� �����带 ���� ������ �����ϴ� ���� �ƴ�, �ý����� ������ ������ �õ��� �ϴ� ��
 * Executor �������̽��� ������ Ǯ(thread pool)�� ������ ���� ���� ��Ƽ� ������ �� �ִ�.
 * Executors Ŭ������ ���� ���� ���丮 �޼ҵ�(factory method)�� ������ �ִ�.
 */

import java.util.concurrent.Executor; // Executor interface 
import java.util.concurrent.Executors; // Executor class

public class ThreadTestExecutor {

	public static void main(String[] args) {
		Runnable r1 = () -> {
			for (int i=10; i>=0; i--)
				System.out.println("ù ��° ������: " + i);
		};
		Runnable r2 = () -> {
			for (int i=10; i>=0; i--)
				System.out.println("�� ��° ������: " + i);
		};
		
		Executor executor = Executors.newCachedThreadPool();
		executor.execute(r1);
		executor.execute(r2);
	}

}
