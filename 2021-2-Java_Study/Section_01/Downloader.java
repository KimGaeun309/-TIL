package Section_01;
import java.lang.Thread;

//interface part 2 

public class Downloader {
	
	private OnDownloadListener mListener;
	
	public Downloader(OnDownloadListener listener) {
		mListener = listener;
	}
	
	public void Start() {
		
		System.out.println("Download Start");
		
		try {
			Thread.sleep(5000); // ������ ���ɼ��� ���� try catch ����ؾ�.
		}
		catch (InterruptedException e){
			System.out.println(e.getMessage());
		}
		mListener.onDownFinish();
		
	}
}
