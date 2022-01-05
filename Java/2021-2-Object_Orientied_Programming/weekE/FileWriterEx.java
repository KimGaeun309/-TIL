package WeekE;
import java.io.*;
import java.util.*;

/*
* ���� ���� ����
FileWriter fout = new FileWriter("c:\\Temp\\text.txt");
fout.write('A'); // ���� 'A' ���
fout.close();

* ��� ���� ����
char [] buf = new char [1024];
// buf[]�迭�� ó������ �迪 ũ��(1024�� ����)��ŭ ����
fout.write(buf, 0, buf.length);
 */

public class FileWriterEx {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		FileWriter fout = null;
		int c;
		try {
			fout = new FileWriter("c:\\Temp\\test.txt");
			while(true) {
				String line = scanner.nextLine();
				if(line.length() == 0)
					break;
				fout.write(line, 0, line.length());
				fout.write("\r\n", 0, 2);
			}
			fout.close();
		}
		catch(IOException e) {
			System.out.println("����� ����");
		}
		scanner.close();
	}

}
