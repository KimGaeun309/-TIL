package weekA;
import java.io.FileWriter; //파일 만들어줌
import java.io.IOException;
import java.io.PrintWriter; // 파일에 텍스트를 쓰는걸 도와줌
// 이건 3차시에서 배울 내용.

public class FileError {
	private int[] list;
	private static final int SIZE = 10;
	
	public FileError() {
		list = new int[SIZE];
		for(int i=0; i<SIZE; i++)
			list[i] = i;
		writeList();
	}
	
	public void writeList() {
		PrintWriter out = null;
		try {
			out = new PrintWriter(new FileWriter("outfile.txt"));
			for (int i=0; i<SIZE; i++)
				out.println("배열 원소 " + i + " = " + list[i]);
		} catch (ArrayIndexOutOfBoundsException e) {
			out.println("ArrayIndexOutOfBoundsException;");
		} catch (IOException e) {
			System.err.println("IOException;");
		} finally {
			if (out != null)
				out.close();
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
