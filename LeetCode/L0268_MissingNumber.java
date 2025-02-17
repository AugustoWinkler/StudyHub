package leetcode.metods;

import java.util.Arrays;

public class L0268_MissingNumber {

	public int missingNumber(int[] nums) {
		Arrays.sort(nums);
		int c = -1;
		for (int num : nums) {
			if (c++ < num - 1)
				return c;
		}
		return nums.length;
	}
}
