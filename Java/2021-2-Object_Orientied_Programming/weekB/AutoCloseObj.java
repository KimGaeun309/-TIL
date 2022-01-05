package weekB;

public class AutoCloseObj implements AutoCloseable {
	// AutoCloseable은 close()를 호출하지 않아도 자동으로 close 처리를 해준다.
	
	@Override
	public void close() throws Exception {
		System.out.println("리소스가 close()되었다.");
	}
}
