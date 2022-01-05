package weekA;

public class ExceptionTestStack {

	public static void main(String[] args) {
		try {
			String obj = "¹°°Ç";
			int objCnt = Integer.valueOf(obj);
			System.out.println(objCnt);
		} catch (Exception e) {
			System.out.println("1. " + e.getMessage());
			System.out.println("2. " + e.toString());
			e.printStackTrace();
		}
	}

}
