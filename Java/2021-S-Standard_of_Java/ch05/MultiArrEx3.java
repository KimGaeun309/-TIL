package ch05;

public class MultiArrEx3 {

	public static void main(String[] args) {
		int[][] m1 = {
				{1, 2, 3},
				{4, 5, 6}
		};
		
		int[][] m2 = {
				{1, 2},
				{3, 4}, 
				{5, 6}
		};
		
		final int ROW = m1.length; // m1 행
		final int COL = m2[0].length; // m2 열
		final int M2_ROW = m2.length; // m3 행
		
		int[][] m3 = new int[ROW][COL];
		
		// 행렬곱
		for(int i=0; i<ROW; i++)
			for(int j=0; j<COL; j++)
				for(int k=0; k<M2_ROW; k++)
					m3[i][j] += m1[i][k] * m2[k][j];
		
		// 행렬 m3를 출력
		for(int i=0;i<ROW; i++) {
			for(int j=0; j<COL; j++)
				System.out.printf("%3d ", m3[i][j]);
			System.out.println();
		}
		
	}

}
