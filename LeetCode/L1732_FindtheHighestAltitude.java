package leetcode.metods;

public class L1732_FindtheHighestAltitude {

	public int largestAltitude(int[] gain) {
		int temp = 0;
		int altitude = 0;
		for (int num : gain) {
			temp += num;
			if (temp > altitude)
				altitude = temp;
		}
		return altitude;
	}

}
