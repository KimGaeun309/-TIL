package weekB;

public class AutoCloseObj implements AutoCloseable {
	// AutoCloseable�� close()�� ȣ������ �ʾƵ� �ڵ����� close ó���� ���ش�.
	
	@Override
	public void close() throws Exception {
		System.out.println("���ҽ��� close()�Ǿ���.");
	}
}
