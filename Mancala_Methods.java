import edu.princeton.cs.algs4.*;

public class Mancala_Methods {

	private class pit
	{
		int index;
		int count;
		pit next;
		pit(int k, int i, pit n)
		{
			index = k;
			count = i;
			next = n;
		}
	}
	
	
	
	pit end1 = new pit(0, 0, null);
	pit end2 = new pit(7, 0, null);
	
	pit pit1 = new pit(1, 4, end2);
	pit pit2 = new pit(2, 4, pit1);
	pit pit3 = new pit(3, 4, pit2);
	pit pit4 = new pit(4, 4, pit3);
	pit pit5 = new pit(5, 4, pit4);
	pit pit6 = new pit(6, 4, pit5);
	
	pit pit7 = new pit(8, 4, end2);
	pit pit8 = new pit(9, 4, pit7);
	pit pit9 = new pit(10, 4, pit8);
	pit pit10 = new pit(11, 4, pit9);
	pit pit11 = new pit(12, 4, pit10);
	pit pit12 = new pit(13, 4, pit11);
	
	//pit[] pitA = new pit[] {end1, pit12, pit11, pit10, pit9, pit8, pit7, end2, pit6, pit5, pit4, pit3, pit2, pit1};
	
	int move(pit a)
	{
		int k = a.count;
		a.count = 0;
		while(k > 0)
		{
			pit s = a.next;
			a.next.count++;
			k--;
			if(k == 0 && s.count > 0 && s != end1 || s != end2)
			{
				StdOut.println(s.index);
				move(s);
			}
		}
	return end2.count;
	}
	
	void begin()
	{
		
		end1.next = pit12;
		
		
	}
	
	
	
	
	
	public static void main(String[] args) {
		
		Mancala_Methods M = new Mancala_Methods();
		M.begin();
		M.move(M.pit11);
	}

}
