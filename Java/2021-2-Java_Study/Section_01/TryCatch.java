package Section_01;

public class TryCatch {
	
	// try catch finally
	
	public static void main(String[] args) {
		
		try {
			boolean isSuccess = login("g82", "11111112");
			if (isSuccess) System.out.println("Login success");
			else System.out.println("Login failed");
		}
		
		catch (Exception e) {
			System.out.println(e.getMessage());
		}
		finally {
			System.out.println("Copyright g82 2015");
		}
	}
	
	static boolean login(String id, String pw) throws Exception {
		
		// Client(Android) -> "g82", "11111112" -> Server
		
		boolean isNetworkFailed = false;
		boolean isNoId = false;
		boolean isPasswordWrong = false;		
		boolean isPWExpired = false;
		
		if (isNetworkFailed) throw new Exception("Network Failed");
		else if (isNoId) throw new Exception("user ID no exist");
		else if (isPasswordWrong) throw new Exception("Password Wrong");
		else if (isPWExpired) throw new Exception("Need change password");
		
		return true;
	}

}
