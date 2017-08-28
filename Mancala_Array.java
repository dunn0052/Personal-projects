import edu.princeton.cs.algs4.*;
public class Mancala_Array {

	
	
	public static int pick(int[] j, int m)
	{
		int[] s = new int[14];
		
		StdOut.println(m + "P");
		if(j[m] != 0)
		{
			int n = j[m];
			j[m] = 0;
			move(j, (m+1)%14 , n);
		}
		return m;
	}
	
	
	public static void move(int[] j, int m, int n )
	{
		if(n == 1 && j[m] != 0 && (m != 0 || m != 7))
		{	
			j[m]++;
			pick(j, m);
		}
		else if(n != 0)
		{
			StdOut.println(m + "M");
			j[m]++;
			move(j, (m+1)%14 , n-1);
		}
	}
	
	public static void print_array(int[] j)
	{
		for(int i = 0; i < j.length; i++)
		{
			if(i == 7)
			{
			StdOut.println(j[i] + "S");
			}
			else
			{
			StdOut.println(j[i]);
			}
			
		}
	}
	
	public static int[] again(int[] a, int m)
	{
		for(int i = 1; i < 7; i++)
		{
			
		}
		
		return a;
	}
	public static void main(String[] args) {
		
		int[] M = new int[] {0,4,4,4,4,4,4,0,4,4,4,4,4,4};
		pick(M, 3);
		print_array(M);
	}

}
