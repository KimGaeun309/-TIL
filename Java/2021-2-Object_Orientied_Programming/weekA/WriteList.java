package weekA;
import java.io.FileWriter;
import java.io.PrintWriter;

public class WriteList {
	
	static int[] list;

	public static void main(String[] args)  throws IOException
	{
		PrintWriter out = new PrintWriter(new FileWriter("outfile.txt"));
		// unhandled exception type IOException
		
		list = new int[10];
		for(int i= 0; i<10; i++)
			out.println("배열 원소 " + i + " = " + list[i]);
		out.close();
	}

}
