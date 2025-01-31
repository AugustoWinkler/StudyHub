package leetcode.metods;

public class L1929_ConcatenationOfArray {

	public static int[] getConcatenation(int[] nums) {
		int[] temp = new int[(nums.length * 2)];
		int i = 0;
		int j = 0;

		while (i++ < 2) {
			for (int num : nums) {
				temp[j++] = num;
			}
		}
		return temp;
	}

}
