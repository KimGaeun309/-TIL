package WeekE;
import java.io.*;
import java.util.*;

/*
* 문자 단위 쓰기
FileWriter fout = new FileWriter("c:\\Temp\\text.txt");
fout.write('A'); // 문자 'A' 출력
fout.close();

* 블록 단위 쓰기
char [] buf = new char [1024];
// buf[]배열의 처음부터 배역 크기(1024개 문자)만큼 쓰기
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
			System.out.println("입출력 오류");
		}
		scanner.close();
	}

}
