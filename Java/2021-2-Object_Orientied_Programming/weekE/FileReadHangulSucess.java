package WeekE;
import java.io.*;

public class FileReadHangulSucess {

	public static void main(String[] args) {
		InputStreamReader in = null;
		FileInputStream fin = null;
		try {
			fin = new FileInputStream("c:\\Temp\\hangul.txt");
			in = new InputStreamReader(fin, "MS949"); // MS���� ���� �ѱ� Ȯ�� �ϼ��� ���� ����
			// US_ASCII �� ó���ϸ� ???????????..�߸��� ���� ���� ����!
			int c;
			
			System.out.println("���ڵ� ���� ������ " + in.getEncoding());
			while((c = in.read()) != -1) {
				System.out.print((char)c);
			}
			in.close();
			fin.close();
		}
		catch(IOException e) {
			System.out.println("����� ����");
		}
	}

}
