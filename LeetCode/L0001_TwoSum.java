package leetcode.metods;

public class L0001_TwoSum {

	public int[] twoSum(int[] nums, int target) {
		int[] result = new int[2];
		int tempNumIndex = 0;

		while (true) {
			for (int i = 1; i < nums.length; i++) {
				if (i == tempNumIndex)
					continue;
				if (nums[i] + nums[tempNumIndex] == target) {
					result[0] = tempNumIndex;
					result[1] = i;
					return result;
				}
			}
			tempNumIndex++;
		}

	}
}
